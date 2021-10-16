import argparse

def main(args: argparse.Namespace) -> None:
    inp = args.inp
    outg = args.outg
    outp = args.outp

    with open(inp,"r") as source:
        with open(outg,"w") as sinkg:
            with open(outp,"w") as sinkp:
                for row in source:

                    row = row.split("\t")
                    word = row[0]
                    ipa = row[1]
                    spaced = ""

                    for w in word:
                        if w == word[-1]:
                            spaced = spaced + w
                        else:
                            spaced = spaced + w + " "

                    print(spaced,file=sinkg)
                    print(ipa,file=sinkp)





if __name__ == "__main__":
    parser = argparse.ArgumentParser() 
    
    parser.add_argument(
        "inp", help="input"
    )
    
    parser.add_argument(
        "outg", help="output for icelandic word"
    )

    parser.add_argument(
        "outp", help="output for ipa transcription"
    )



main(parser.parse_args())