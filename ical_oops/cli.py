import os
import argparse

def add_status_cancelled(file_path, output_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    in_event = False

    for line in lines:
        updated_lines.append(line)
        if line.strip() == "BEGIN:VEVENT":
            in_event = True
        elif line.strip() == "END:VEVENT":
            if in_event:
                updated_lines.insert(-1, "STATUS:CANCELLED\n")
            in_event = False

    with open(output_path, 'w') as file:
        file.writelines(updated_lines)

def main():
    parser = argparse.ArgumentParser(description="Update iCal files with STATUS:CANCELLED for each event.")
    parser.add_argument('input', help="Path to the input iCal file")
    parser.add_argument('output', help="Path to save the updated iCal file")
    args = parser.parse_args()

    add_status_cancelled(args.input, args.output)
    print(f"Updated {args.input} with STATUS:CANCELLED for each event and saved to {args.output}.")

if __name__ == "__main__":
    main()