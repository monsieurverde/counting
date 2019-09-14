def counter(s):
   
    alphaDict = dict.fromkeys(s,0)
    return(alphaDict)

def main():

    s="Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    print(counter(s))

if __name__ == "__main__":
    main()