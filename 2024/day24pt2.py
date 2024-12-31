## Copied from Luskan (Github). I did not understand part 2.


GATE_AND = 0
GATE_OR = 1
GATE_XOR = 2
GATE_NOTE = 3  # Not a gate, contains some msg as tuple element 1

LogicGate = tuple[str, int, str, str]
LogicGateGroup = list[LogicGate]


class ParsedData:
    __slots__ = ["wires", "gates"]

    def __init__(self):
        self.wires: dict[str, int] = {}
        self.gates: LogicGateGroup = []


def find_switched_outputs(data: ParsedData) -> list[tuple[str, str]]:
    wrong_outputs: list[tuple[str, str]] = []

    # Count number of x and y input bits
    x_bits = sum(1 for w in data.wires if w.startswith("x"))

    prev_output_name_carry_out = "?"
    output_name_carry_out = "?"

    for gate_index in range(x_bits):
        group: LogicGateGroup = []
        # Create a group of joined elements (a clique) which are connected to the same inputs
        for gate in data.gates:
            if f"x{gate_index:02d}" in gate or f"y{gate_index:02d}" in gate:
                group.append(gate)
                if gate_index > 0:
                    for gate2 in data.gates:
                        if gate[3] in gate2 and gate2 != gate:
                            gate2_new = gate2
                            if gate2_new[2] == gate[3]:
                                gate2_new = (
                                    gate2_new[2],
                                    gate2_new[1],
                                    gate2_new[0],
                                    gate2_new[3],
                                )
                            if gate2 in group:
                                group.remove(gate2)
                            if gate2_new not in group:
                                group.append(gate2_new)

                            for gate3 in data.gates:
                                if (
                                    gate2[3] == gate3[0] or gate2[3] == gate3[2]
                                ) and gate2[1] == GATE_AND:
                                    if (
                                        gate3 not in group
                                        and gate2 != gate3
                                        and gate3 != gate2_new
                                        and gate != gate3
                                    ):
                                        if (
                                            gate3[2],
                                            gate3[1],
                                            gate3[0],
                                            gate3[3],
                                        ) not in group:
                                            group.append(gate3)
        # Sort elements of a group in the exact order as in the comment above

        # Helper function to move logic gates in the group to their correct indexes.
        def extract_swap(
            logic_group: LogicGateGroup,
            name: str,
            gate_type: int,
            start_index: int,
            dest_index: int,
        ):
            if dest_index >= len(logic_group):
                raise IndexError(
                    f"Destination index {dest_index} is out of range for the group list."
                )
            index = -1
            for i, gate in enumerate(logic_group):
                if (
                    i >= start_index
                    and (gate[0].startswith(name) or name == "")
                    and gate[1] == gate_type
                ):
                    index = i
                    break
            if index == -1:
                raise ValueError(
                    f"No gate with name starting with '{name}' & gate_type '{gate_type}' at index {start_index}"
                )
            logic_group[dest_index], logic_group[index] = (
                logic_group[index],
                logic_group[dest_index],
            )

        # Reorder gates to their correct indexes, as in RCA schematic.
        extract_swap(group, "x", GATE_XOR, 0, 0)
        extract_swap(group, "x", GATE_AND, 0, 1)
        if gate_index > 0:
            extract_swap(group, "", GATE_AND, 2, 2)
            extract_swap(group, "", GATE_OR, 2, 3)
            extract_swap(group, "", GATE_XOR, 2, 4)

        # Now, we now that only outputs are messed up, so having correctly ordered the group of logic units,
        # we can use their inputs to find the correct outputs (using the logic schematic from the comment at the top of file)
        #  (*) I assume that swaps are only omong the logical groups of adder, not between them

        correct_outputs: list[str]
        if gate_index == 0:
            # First group is easy to deduce, as it has only two gates, and the output is easily found from the inputs
            correct_outputs = [
                f"z{gate_index:02d}",
                group[1][3],  # Same as before (*)
            ]
            prev_output_name_carry_out = group[0][3]
        else:
            # Find the name of a new carry out, it will be used in the next logic group so in current group
            # it should not be found as an input name.
            outputs_1_to_3 = [group[1][3], group[2][3], group[3][3]]
            for test_out in outputs_1_to_3.copy():
                wrong = False
                for gate in group:
                    if test_out == gate[0] or test_out == gate[2]:
                        wrong = True
                        break
                if not wrong:
                    output_name_carry_out = test_out
                    outputs_1_to_3.remove(output_name_carry_out)
                    break
            if output_name_carry_out is None:
                raise ValueError("Error: output_name_carry_out_2 not found")

            if len(outputs_1_to_3) != 2:
                raise ValueError(
                    f"Error: outputs_1_to_3 of wrong size: {len(outputs_1_to_3)}"
                )

            correct_outputs = [
                # To find output name for the first line (XOR), we look into the:
                # 6. c0 AND t2 -> t4   (carry propagate)
                # and choose t2, (data is very messed up) since it can be on left or right of AND, we look on both sides
                (
                    group[2][2]
                    if group[2][0] == prev_output_name_carry_out
                    else group[2][0]
                ),
                outputs_1_to_3[0],  # Those two can be of any order actually
                outputs_1_to_3[1],  # <-----/
                output_name_carry_out,
                f"z{gate_index:02d}",
            ]

        diff: list[tuple[str, str]] = []
        correct_outputs: list[str]

        if gate_index == 0:
            # Only two outputs. We check only first, as if it does not match then the second one is also wrong.
            if group[0][3] != correct_outputs[0]:
                diff.append((group[0][3], correct_outputs[0]))
        else:
            # Only one swap per group is allowed. So lets choose first the most obvious ones.
            # Like the output bit first (z01,...).
            if group[4][3] != correct_outputs[4]:
                diff.append((group[4][3], correct_outputs[4]))
            # This one, the current logic group carry out is also quite easily to deduce, so its reliable
            elif group[3][3] != correct_outputs[3]:
                diff.append((group[3][3], correct_outputs[3]))
            # Then the output for first xor, which is quite reliable to find from the other outputs and previous carry out.
            elif group[0][3] != correct_outputs[0]:
                diff.append((group[0][3], correct_outputs[0]))
            else:
                # Now the two intermediate values: partial carry and carry propagate. Their names can be freely swapped,
                # as it does not change the output logic.
                s1 = [group[1][3], group[2][3]]
                s1.sort()
                s2 = [correct_outputs[1], correct_outputs[2]]
                s2.sort()
                if s1 != s2:
                    diff.append((s1[0], s2[0]))
                    diff.append((s1[1], s2[1]))
            wrong_outputs.extend(diff)
    return wrong_outputs


def part2(data: ParsedData) -> str:
    swithed_outputs = find_switched_outputs(data)
    array_of_outputs = []
    for output in swithed_outputs:
        array_of_outputs.append(str(output[0]))
        array_of_outputs.append(str(output[1]))
    sorted_outputs = sorted(array_of_outputs)
    # remove duplicates from sorted_outputs - probably not needed
    sorted_outputs = list(dict.fromkeys(sorted_outputs))

    return ",".join(sorted_outputs)


def parse_input(data: str) -> ParsedData:
    result: ParsedData = ParsedData()
    lines = data.strip().split("\n")
    for line in lines:
        parts = line.split(" ")
        if len(parts) == 2:
            result.wires[parts[0][:-1]] = int(parts[1])
        elif len(parts) == 5:
            # ntg XOR fgs -> mjb
            gate = (
                parts[0],
                (
                    GATE_AND
                    if parts[1] == "AND"
                    else GATE_OR if parts[1] == "OR" else GATE_XOR
                ),
                parts[2],
                parts[4],
            )

            # Do some initial ordering, x should always be on the left side, also sort output names
            ch1 = gate[0][0]
            ch2 = gate[2][0]
            if (
                (ch1 == "y" and ch2 == "x")
                or (ch2 == "y" and ch1 != "x")
                or (ch2 == "x" and ch1 != "y")
                or (gate[0] < gate[2] and ch1 not in "xy" and ch2 not in "xy")
            ):
                # Make sure x is always on the left side
                gate = (gate[2], gate[1], gate[0], gate[3])
            result.gates.append(gate)
    return result


def main(file: str):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    data = parse_input(content)
    answer = part2(data)
    return answer


res_actual = main("2024/day24_input.txt")
print(res_actual)
