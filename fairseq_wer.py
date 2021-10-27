import argparse


def main(args: argparse.Namespace) -> None:
    inp = args.inp

    gold = []
    predictions = []

    with open(inp, "r") as source:
        for line in source:
            if line[0] == "T":
                sline = line.split("\t")
                target = "".join(sline[1:])
                gold.append(target)
            if line[0] == "H":
                sline = line.split("\t")
                pred = "".join(sline[2:])
                predictions.append(pred)
    print(gold, "\n", predictions)

    correct = 0
    count = 0

    for target, prediction in zip(gold, predictions):
        count += 1
        if prediction == target:
            correct += 1

    wer = (count - correct) / count
    print(f"WER: {wer * 100}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("inp", help="input file here")

main(parser.parse_args())
