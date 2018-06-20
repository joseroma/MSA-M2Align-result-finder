import operator
import statistics
import numpy as np


def median(data_list):
    data = sorted(data_list)
    index = len(data_list)//2
    value = data[len(data)//2]
    return index, value


def print_Align(lista_var, fich_escrib, index):
    count = 0
    for i in range(0, len(lista_var)):
        if str(lista_var[i]) == '>1aab_\n':
            if count == index:
                for j in range(i, i + 8):
                    fich_escrib.write(lista_var[j])
                break
            else:
                count = count + 1
    print("File: " + str(fich_escrib) + " writted.")


class AlignAnalizer:

    # We generate the constructor
    def __init__(self, k, print):
        self.k = k
        self.print = print

    def read_and_process_max_balibase(self):
        # To upper case, just in case it is not ok the name
        k = self.k.upper()
        # Open the FUN. file in reading mode.
        archivo_FUN = open('FUN.' + k + '.tsv', 'r')
        # Open the VAR. file in reading mode.
        archivo_VAR = open('VAR.' + k + '.tsv', 'r')
        # Read all the lines.
        lista_fun = archivo_FUN.readlines()
        # Read all the lines.
        lista_var = archivo_VAR.readlines()
        # Here we are generating the different lists to store the different measures.
        strike = []
        tc = []
        sp = []
        # Here we iterate over the different lines.
        for linea in lista_fun:
            # Here we split the lines into the different lists of parameters.
            vector = linea.split('\t')
            strike.append(vector[0])
            tc.append(vector[1])
            sp.append(vector[2])
        # We open the different result directories
        f1 = open("results/Best_strike_seq.txt", "w")
        f2 = open("results/Best_tc_seq.txt", "w")
        f3 = open("results/Best_sp_seq.txt", "w")
        f4 = open("results/Best_strike_value.txt", "w")
        f5 = open("results/Best_tc_value.txt", "w")
        f6 = open("results/Best_sp_value.txt", "w")
        #Here we open the different files
        fmedian = open("results/Median_strike_seq.txt", "w")
        fmedian2 = open("results/Median_tc_seq.txt", "w")
        fmedian3 = open("results/Median_sp_seq.txt", "w")
        fmedian4 = open("results/Median_strike_value.txt", "w")
        fmedian5 = open("results/Median_tc_value.txt", "w")
        fmedian6 = open("results/Median_sp_value.txt", "w")
        #Here we calculate the median with the function implemented in the top
        res, ind = median(strike)
        res1, ind = median(sp)
        res2, ind = median(tc)
        # Calculate the maximum values for each parameter
        index, value = max(enumerate(strike), key=operator.itemgetter(1))
        index1, value1 = max(enumerate(tc), key=operator.itemgetter(1))
        index2, value2 = max(enumerate(sp), key=operator.itemgetter(1))

        # Write the different values (sequences)
        print_Align(lista_var, f1, index)
        print_Align(lista_var, f2, index1)
        print_Align(lista_var, f3, index2)
        print_Align(lista_var, fmedian, res)
        print_Align(lista_var, fmedian3, res1)
        print_Align(lista_var, fmedian2, res2)

        # Here we calculate the mean values
        st = 0
        cps = 0
        spp = 0
        for strik in strike:
            st = st + float(strik)
        mean_strike = st / len(strike)

        for tci in tc:
            cps = cps + float(tci)
        mean_tc = cps / len(tc)

        for sps in sp:
            spp = spp + float(sps)
        mean_sp = spp / len(sp)

        # Here we are writting the score values
        f4.write(
            'Strike: ' + strike[index] + ' Mean: ' + str(mean_strike) + '\n TC: ' + tc[index] + ' Mean: ' + str(mean_tc)
            + '\n SP: ' + sp[index] + ' Mean: ' + str(mean_sp))
        f5.write(
            'Strike: ' + strike[index1] + ' Mean: ' + str(mean_strike) + '\n TC: ' + tc[index1] + ' Mean: ' + str(
                mean_tc)
            + '\n SP: ' + sp[index1] + ' Mean: ' + str(mean_sp))
        f6.write(
            'Strike: ' + strike[index2] + ' Mean: ' + str(mean_strike) + '\n TC: ' + tc[index2] + ' Mean: ' + str(
                mean_tc) + '\n SP: ' + sp[index2] + ' Mean: ' + str(mean_sp))
        fmedian4.write(
            'Strike: ' + strike[len(strike) // 2] + ' Mean: ' + str(mean_strike) + '\n TC: ' + tc[
                len(strike) // 2] + ' Mean: ' + str(
                mean_tc) + '\n SP: ' + sp[len(strike) // 2] + ' Mean: ' + str(mean_sp))
        fmedian5.write(
            'Strike: ' + strike[len(sp) // 2] + ' Mean: ' + str(mean_strike) + '\n TC: ' + tc[
                len(sp) // 2] + ' Mean: ' + str(
                mean_tc) + '\n SP: ' + sp[len(sp) // 2] + ' Mean: ' + str(mean_sp))
        fmedian6.write(
            'Strike: ' + strike[len(tc) // 2] + ' Mean: ' + str(mean_strike) + '\n TC: ' + tc[
                len(tc) // 2] + ' Mean: ' + str(
                mean_tc) + '\n SP: ' + sp[len(tc) // 2] + ' Mean: ' + str(mean_sp))

        if self.print:
            # Print the different scores values
            print('Best strike: ', index, value, ' Mean value: ' + str(mean_strike))
            print('Best tc: ', index1, value1, ' Mean value: ' + str(mean_tc))
            print('Best sp: ', index2, value2, ' Mean value: ' + str(mean_sp))
            from sklearn import preprocessing
            import matplotlib.pyplot as plt
            strike_norm = preprocessing.scale(strike)
            tc_norm = preprocessing.scale(tc)
            cp_norm = preprocessing.scale(sp)
            # 'o' hace que sea dotplot sino lineas
            plt.plot(strike_norm, cp_norm, 'o')
            plt.show()
            # He elegido elegir estos dos scores en vistas de que el tc_norm aunque
            # afecta al resultado funal no resulta tan importante y esto nos permite ver
            # una curva de compromiso entre strike y cp. Para obtener el valor maximo en uno tenemos que ceder en el otro
        f1.close()
        f2.close()
        f3.close()
        f4.close()
        f5.close()
        f6.close()
        archivo_FUN.close()
        archivo_VAR.close()

    def read_and_process_min_balibase(self):
        k = self.k.upper()
        # Open the FUN. and VAR. file in reading mode.
        archivo_FUN = open('FUN.' + k + '.tsv', 'r')
        archivo_VAR = open('VAR.' + k + '.tsv', 'r')
        # Read all the lines.
        lista_fun = archivo_FUN.readlines()
        lista_var = archivo_VAR.readlines()
        # Here we are generating the different lists to store the different measures.
        strike = []
        tc = []
        sp = []
        # Here we iterate over the different lines.
        for linea in lista_fun:
            # Here we split the lines into the different lists of parameters.
            vector = linea.split('\t')
            strike.append(vector[0])
            tc.append(vector[1])
            sp.append(vector[2])
        # Create and open the different files
        fm1 = open("results/Worse_strike_seq.txt", "w")
        fm2 = open("results/Worse_tc_seq.txt", "w")
        fm3 = open("results/Worse_sp_seq.txt", "w")
        fm4 = open("results/Worse_strike_value.txt", "w")
        fm5 = open("results/Worse_tc_value.txt", "w")
        fm6 = open("results/Worse_sp_value.txt", "w")

        fmedian = open("results/Median_strike_seq.txt", "w")
        fmedian2 = open("results/Median_tc_seq.txt", "w")
        fmedian3 = open("results/Median_sp_seq.txt", "w")
        fmedian4 = open("results/Median_strike_value.txt", "w")
        fmedian5 = open("results/Median_tc_value.txt", "w")
        fmedian6 = open("results/Median_sp_value.txt", "w")
        # Calculate the minimum values for each parameter
        indexmin, valuemin = min(enumerate(strike), key=operator.itemgetter(1))
        indexmin1, valuemin1 = min(enumerate(tc), key=operator.itemgetter(1))
        indexmin2, valuemin2 = min(enumerate(sp), key=operator.itemgetter(1))
        #Here we calculate the median values
        res, ind = median(strike)
        res1, ind = median(sp)
        res2, ind = median(tc)
        # Write the different values (sequences)

        print_Align(lista_var, fm1, indexmin)
        print_Align(lista_var, fm2, indexmin1)
        print_Align(lista_var, fm3, indexmin2)
        print_Align(lista_var, fmedian, res)
        print_Align(lista_var, fmedian3, res1)
        print_Align(lista_var, fmedian2, res2)

                # Here we calculate the mean values
        st = 0
        cps = 0
        spp = 0
        for strik in strike:
            st = st + float(strik)
        mean_strike = st / len(strike)

        for tci in tc:
            cps = cps + float(tci)
        mean_tc = cps / len(tc)

        for sps in sp:
            spp = spp + float(sps)
        mean_sp = spp / len(sp)

        # Here we are writting the score values
        fm4.write(
            'Strike: ' + strike[indexmin] + ' Mean: ' + str(mean_strike) + '\n TC: ' + tc[indexmin] + ' Mean: ' + str(
                mean_tc) + '\n SP: ' + sp[indexmin] + ' Mean: ' + str(mean_sp))
        fm5.write(
            'Strike: ' + strike[indexmin1] + ' Mean: ' + str(mean_strike) + '\n TC: ' + tc[
                indexmin1] + ' Mean: ' + str(
                mean_tc) + '\n SP: ' + sp[indexmin1] + ' Mean: ' + str(mean_sp))
        fm6.write(
            'Strike: ' + strike[indexmin2] + ' Mean: ' + str(mean_strike) + '\n TC: ' + tc[
                indexmin2] + ' Mean: ' + str(
                mean_tc) + '\n SP: ' + sp[indexmin2] + ' Mean: ' + str(mean_sp))
        fmedian4.write(
            'Strike: ' + strike[len(strike)//2] + ' Mean: ' + str(mean_strike) + '\n TC: ' + tc[len(strike)//2] + ' Mean: ' + str(
                mean_tc) + '\n SP: ' + sp[len(strike)//2] + ' Mean: ' + str(mean_sp))
        fmedian5.write(
            'Strike: ' + strike[len(sp)//2] + ' Mean: ' + str(mean_strike) + '\n TC: ' + tc[len(sp)//2] + ' Mean: ' + str(
                mean_tc) + '\n SP: ' + sp[len(sp)//2] + ' Mean: ' + str(mean_sp))
        fmedian6.write(
            'Strike: ' + strike[len(tc)//2] + ' Mean: ' + str(mean_strike) + '\n TC: ' + tc[len(tc)//2] + ' Mean: ' + str(
                    mean_tc) + '\n SP: ' + sp[len(tc)//2] + ' Mean: ' + str(mean_sp))


        if self.print:
            print('Worse Strike: ', indexmin, valuemin, ' Mean value: ' + str(mean_strike))
            print('Worse tc: ', indexmin1, valuemin1, ' Mean value: ' + str(mean_tc))
            print('Worse sp: ', indexmin2, valuemin2, ' Mean value: ' + str(mean_sp))
            # Plot the strike-cp
            from sklearn import preprocessing
            import matplotlib.pyplot as plt
            strike_norm = preprocessing.scale(strike)
            tc_norm = preprocessing.scale(tc)
            cp_norm = preprocessing.scale(sp)
            # 'o' hace que sea dotplot sino lineas
            plt.plot(strike_norm, cp_norm, 'o')
            plt.show()
            # He elegido elegir estos dos scores en vistas de que el tc_norm aunque
            # afecta al resultado funal no resulta tan importante y esto nos permite ver
            # una curva de compromiso entre strike y cp. Para obtener el valor maximo en uno tenemos que ceder en el otro
        fm1.close()
        fm2.close()
        fm3.close()
        fm4.close()
        fm5.close()
        fm6.close()
        archivo_FUN.close()
        archivo_VAR.close()


k = str(input('Enter your FUN. and VAR. ID without FUN. VAR. or .tsv  (example=> BB11001): '))
align = AlignAnalizer(k, True)
align.read_and_process_max_balibase()
#align.read_and_process_min_balibase()
