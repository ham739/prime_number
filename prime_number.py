import sys
import sympy as sym

def prime(num):

        numbers = []

        if num <= 0:
                return  "{}は自然数ではありません".format(num)
        elif num == 1:
                return "素数は1より大きい自然数が対象です。1より大きい数字を入力してください"
        elif num == 2:
                return "{}は素数です".format(num)

        for a in range(2,num):
                if num % a == 0:
                        numbers.append(a)
        if not numbers:
                return "{}は素数です".format(num)
        else:
                return "{}は素数ではありません。{}で割り切れます".format(num,numbers)

def main():

        a = input("好きな自然数を入れてください:")

        try:
                b = int(a)
        except ValueError:
                print("")
                print( "{}は自然数ではありません".format(a))
                print("")
                sys.exit()

        print("")
        print(prime(b))
        print("")

        print("知りたい範囲の素数を調べます")

        try:
                str_small_number = input("知りたい範囲の小さい数字を入れてください。終了する場合はそれ以外を入れてください:")
                int_small_number = int(str_small_number)

                str_big_number = input("知りたい範囲の大きい数字を入れてください。終了する場合はそれ以外を入れてください:")
                int_big_number =  int(str_big_number)

        except ValueError:
                print("")
                print("システムを終了します")
                print("")
                sys.exit()

        all_prime_number = [i for i in sym.primerange(int_small_number, int_big_number)]

        if not all_prime_number:

                print("")
                print("{}から{}までの間の素数はありません".format(str_small_number,str_big_number))
                print("")
                sys.exit()
        else:

                print("")
                print("{}から{}までの間の素数は{}です".format(str_small_number,str_big_number,all_prime_number))
                print("")

if __name__ == '__main__':

        main()

