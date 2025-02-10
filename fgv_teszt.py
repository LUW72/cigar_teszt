import fgv

def cigar_party_teszt():
    """ Ez tartalmazza a teszteseteket, Unit tesztek, mert fügvényt tesztelünk vele """
    # fgv.cigar_party(30, False) -> False
    """
    print(f"1. Teszteset")
    cigar_num = 30
    is_weekend = False
    vart_e = False
    kapott_e = fgv.cigar_party(cigar_num, is_weekend)
    print(f"\tCigaretták száma: {cigar_num}, hétvége-e: {is_weekend} \n\tVárt eredmény: {vart_e}\n\tKapott eredmény: {kapott_e}\n\n\tJó-e? {vart_e ==kapott_e}")
    """

    cigar_num = 0
    tesztszamok = [35, 45, 70, 40, 60,
                   35, 45, 70, 40, 60]

    is_weekend = False
    vart_e = False
    i = 0
    while i < 10:
        cigar_num = tesztszamok[i]

        print(f"{i+1}. Teszteset")

        kapott_e = fgv.cigar_party(cigar_num, is_weekend)

        if i > 7:
            is_weekend = True

        if is_weekend == False and (cigar_num == 35 or 45 or 40 or 60):
            vart_e = True

        print(f"\tCigaretták száma: {cigar_num}, hétvége-e: {is_weekend} \n\tVárt eredmény: {vart_e}\n\tKapott eredmény: {kapott_e}\n\n\tJó-e? {vart_e ==kapott_e}")
        vart_e = False

        i += 1
def cigar_teszt_02():

    cigars_lista = [30, 50, 70, 30]
    is_weekend_lista = [False, False, True, True]
    vart_e_lista = [False, True, True, False]

    for i in range(len(cigars_lista)):
        print(f"{i+1}. Teszteset")
        cigar_num = cigars_lista[i]
        is_weekend = is_weekend_lista[i]
        vart_e = vart_e_lista[i]

        kapott_e = fgv.cigar_party(cigar_num, is_weekend)
        print(f"\tCigaretták száma: {cigar_num}, hétvége-e: {is_weekend} "
              f"\n\tVárt eredmény: {vart_e}"
              f"\n\tKapott eredmény: {kapott_e}"
              f"\n\n\tJó-e? {vart_e == kapott_e}")


def sum_test():
    a_lista =    [3,  9, 10, 7, 9]
    b_lista =    [4,  4, 11, 12, 1]
    vart_lista = [7, 20, 21, 20, 20]

    for i in range(len(a_lista)):
        print(f"{i + 1}. Teszteset")
        print(f"\tA: {a_lista[i]}\n\tB: {b_lista[i]}\n\tVárt eredmény: {vart_lista[i]}")
        kapott_er = fgv.hazi_test(a_lista[i], b_lista[i])
        print(f"Kapott eredmény: {kapott_er}")
        print(f"Helyes? - {vart_lista[i] == kapott_er}")