import math

# ask user for a choice
print(
    'Here\'s our advanced calculator which can facilitate you in linear algebra and sophisticated matrix operation!! \n')
# enter choice
print('0--> Eigen-values\n'
      '1--> Two-d Homogeneous\n'
      '2--> Three-d Homogeneous\n'
      '3--> Guass-seidel 3variables\n'
      '4--> Jacobi 2variables\n')

print('Enter what you would like the calculator to do for you:-')

choice_input = int(input())

# eigen values and vector
if choice_input == 0:

    print('Enter matrix elements row-wise:-')
    # creating the main input 2-d matrix
    arr = [[eval(input()) for j in range(0, 2)] for i in range(0, 2)]

    # separate containers for eigen vectors and values
    eigen_values = list()

    eigen_vector1 = list()

    eigen_vector2 = list()

    # trace of the array

    trace_arr = arr[0][0] + arr[1][1]

    # quadratic component(1)
    s1 = trace_arr * trace_arr

    # determining the determinant of the matrix

    determinant_arr = (arr[0][0] * arr[1][1]) - (arr[1][0] * arr[0][1])

    # quadratic component(2)

    s2 = 4 * determinant_arr

    # stating for complex eigen values
    if s1 - s2 < 0:
        print("Complex eigen values")
        exit()

    # appending the quadratic roots (eigen_values)

    eigen_values.append((trace_arr + math.sqrt(s1 - s2)) / 2)

    eigen_values.append((trace_arr - math.sqrt(s1 - s2)) / 2)

    print(f'Eigen Values are {eigen_values[0]} and {eigen_values[1]} ')

    # calculation complete for eigen values

    # EIGEN VECTORS

    # arrays of coefficients of  homogeneous equations

    arr1 = [[(arr[0][0] - eigen_values[0]), arr[0][1]], [arr[1][0], (arr[1][1] - eigen_values[0])]]

    arr2 = [[(arr[0][0] - eigen_values[1]), arr[0][1]], [arr[1][0], (arr[1][1] - eigen_values[1])]]

    # array of determinants of homogeneous equation matrix

    determinants = list()

    determinants.append(round((arr1[0][0] * arr1[1][1]) - (arr1[1][0] * arr1[0][1]), 9))  # 1st element

    determinants.append(round((arr2[0][0] * arr2[1][1]) - (arr2[1][0] * arr2[0][1]), 9))  # 2nd element

    # looping for determination of rank of solving equation matrix
    for i in range(2):

        if determinants[i] != 0:

            if i == 0:
                print(f'There exist no non zero eigenvector corresponding to eigen value {eigen_values[0]}')

            if i == 1:
                print(f'There exist no non zero eigenvector corresponding to eigen value {eigen_values[1]}')

        if determinants[i] == 0:

            if i == 0:

                if arr1[0] == [0, 0]:
                    if arr1[1][0] != 0 and arr1[1][1] != 0:
                        y = -arr1[1][0] / arr1[1][1]
                        eigen_vector1.append(1)
                        eigen_vector1.append(y)

                    elif arr1[1][0] != 0 and arr1[1][1] == 0:
                        eigen_vector1.append(0)
                        eigen_vector1.append(1)
                    else:
                        eigen_vector1.append(1)
                        eigen_vector1.append(0)

                elif arr1[1] == [0, 0]:
                    if arr1[0][0] != 0 and arr1[0][1] != 0:
                        y = -arr1[0][0] / arr1[0][1]
                        eigen_vector1.append(1)
                        eigen_vector1.append(y)
                    elif arr1[0][0] != 0 and arr1[0][1] == 0:
                        eigen_vector1.append(0)
                        eigen_vector1.append(1)
                    else:
                        eigen_vector1.append(1)
                        eigen_vector1.append(0)

                elif arr1[0][1] == 0 and arr1[1][1] == 0:
                    eigen_vector1.append(0)
                    eigen_vector1.append(1)
                else:
                    y = -arr1[0][0] / arr1[0][1]
                    eigen_vector1.append(1)
                    eigen_vector1.append(y)

                print(
                    f'Eigen vector corresponding to eigen value {eigen_values[0]} is [{eigen_vector1[0]},{eigen_vector1[1]}]')

            if i == 1:
                if arr2[0] == [0, 0]:
                    if arr2[1][0] != 0 and arr2[1][1] != 0:
                        y = -arr2[1][0] / arr1[1][1]
                        eigen_vector2.append(1)
                        eigen_vector2.append(y)

                    elif arr2[1][0] != 0 and arr2[1][1] == 0:
                        eigen_vector2.append(0)
                        eigen_vector2.append(1)
                    else:
                        eigen_vector2.append(1)
                        eigen_vector2.append(0)
                elif arr2[1] == [0, 0]:
                    if arr2[0][0] != 0 and arr2[0][1] != 0:
                        y = -arr2[0][0] / arr2[0][1]
                        eigen_vector2.append(1)
                        eigen_vector2.append(y)
                    elif arr2[0][0] != 0 and arr2[0][1] == 0:
                        eigen_vector2.append(0)
                        eigen_vector2.append(1)
                    else:
                        eigen_vector2.append(1)
                        eigen_vector2.append(0)

                elif arr2[0][1] == 0 and arr2[1][1] == 0:
                    eigen_vector2.append(0)
                    eigen_vector2.append(1)
                else:
                    y = -arr2[0][0] / arr2[0][1]
                    eigen_vector2.append(1)
                    eigen_vector2.append(y)

                print(
                    f'Eigen vector corresponding to eigen value {eigen_values[1]} is [{eigen_vector2[0]},{eigen_vector2[1]}]')

    exit()

if choice_input == 1:
    # coefficients of the two-d homogeneous system

    print('Enter coefficients of the system:-')

    coeff = [[eval(input()) for columns in range(2)] for rows in range(2)]

    # checks whether system is homogeneous

    determinant = (coeff[0][0] * coeff[1][1]) - (coeff[1][0] * coeff[0][1])

    # rank depends on determinant

    # if rank is equal to number of unknowns then system has trivial solutions

    if determinant != 0:
        print('(x,y) = {0,0} , Trivial Solutions')

    else:

        if coeff[0] == [0, 0]:
            if coeff[1][0] != 0 and coeff[1][1] != 0:
                y = -coeff[1][0] / coeff[1][1]
                print("(x,y)={{t,({})*t}}, where 't' belongs to real number".format(y))
            elif coeff[1][0] != 0 and coeff[1][1] == 0:
                print('(x,y)={0,t} , where t belongs to real number')
            else:
                print('(x,y)={t,0} , where t belongs to real number')

        elif coeff[1] == [0, 0]:
            if coeff[0][0] != 0 and coeff[0][1] != 0:
                y = -coeff[0][0] / coeff[0][1]
                print("(x,y)={{t,({})*t}}, where 't' belongs to real number".format(y))
            elif coeff[0][0] != 0 and coeff[0][1] == 0:
                print('(x,y)={0,t} , where t belongs to real number')
            else:
                print('(x,y)={t,0} , where t belongs to real number')

        elif coeff[0][1] == 0 and coeff[1][1] == 0:
            print('(x,y)={0,t} , where t belongs to real number')

        else:
            y = -coeff[0][0] / coeff[0][1]
            print("(x,y)={{t,({})*t}}, where 't' belongs to real number".format(y))

    exit()

if choice_input == 2:

    print('Enter coefficients of the system :- ')
    coeff_matrix = [[eval(input()) for columns in range(3)] for rows in range(3)]

    condition_determinant = coeff_matrix[0][1] * coeff_matrix[1][1] - coeff_matrix[0][1] * coeff_matrix[1][0]

    # checks for determinant of all second order matrices of our 3 by 3 matrix
    def rank_finder_for_lessThan_3_for2(main_matrix=coeff_matrix):
        def subMatrix_determinant_finder(index_row, index_col):

            Sub_matrixDeterminantHolder = list()

            for i in range(3):

                if i == index_row:
                    continue

                for j in range(3):

                    if j == index_col:
                        continue

                    Sub_matrixDeterminantHolder.append(main_matrix[i][j])

            return Sub_matrixDeterminantHolder[0] * Sub_matrixDeterminantHolder[3] - Sub_matrixDeterminantHolder[1] * \
                Sub_matrixDeterminantHolder[2]

        determinant_array = list()

        for iterator_1 in range(3):

            for iterator_2 in range(3):
                determinant_array.append(subMatrix_determinant_finder(iterator_1, iterator_2))

        if 0 in determinant_array:
            return 1

        else:
            return 2


    determinant_of_coeff_matrix = \
        (coeff_matrix[0][0] * (coeff_matrix[1][1] * coeff_matrix[2][2] - coeff_matrix[2][1] * coeff_matrix[1][2])) - \
        (coeff_matrix[0][1] * (coeff_matrix[1][0] * coeff_matrix[2][2] - coeff_matrix[2][0] * coeff_matrix[1][2])) + \
        (coeff_matrix[0][2] * (coeff_matrix[1][0] * coeff_matrix[2][1] - coeff_matrix[2][0] * coeff_matrix[1][1]))

    # if rank is 3 then trivial solutions
    if determinant_of_coeff_matrix != 0:
        print('(x,y,z)={0,0,0},Trivial Solutions')
        exit()

    rank = rank_finder_for_lessThan_3_for2()

    if rank == 2 and (condition_determinant == 0 or coeff_matrix[0][1] == 0):
        raise ValueError('Due to method calculation try with non zero distinct elements')

    if rank == 2:
        x = (coeff_matrix[0][1] * coeff_matrix[1][2] - coeff_matrix[0][2] * coeff_matrix[1][1]) / (
                coeff_matrix[0][0] * coeff_matrix[1][1] - coeff_matrix[0][1] * coeff_matrix[1][0])

        s1 = -(coeff_matrix[0][2]) / (coeff_matrix[0][1])

        s2 = -(coeff_matrix[0][0]) / (coeff_matrix[0][1])

        y = s1 + s2 * x

        print(f'(x,y,z)=[{x}*t ,{y}*t ,t] , where t belongs to real number ')
        exit()

    if rank == 1:
        s1 = -(coeff_matrix[0][1]) / (coeff_matrix[0][0])

        s2 = -(coeff_matrix[0][2]) / (coeff_matrix[0][0])

        print(f'(x,y,z)=[{s1}*m + {s2}*n ,m ,n] , where m,n belongs to real number')

    exit()

if choice_input == 3:

    # creating coeff_array
    # guass seidel numerical method
    print('Enter a coefficients of the system:-')

    arr = [[eval(input()) for columns in range(4)] for rows in range(3)]

    x = y = z = 0
    temp = list()

    if arr[0][0] < arr[0][1] + arr[0][2] or arr[1][1] < arr[1][0] + arr[1][2] or arr[2][2] < arr[2][1] + arr[2][0]:
        raise ValueError('Try matching the coefficients condition for guass-seidel')
        exit()

    for i in range(80):

        if i == 0:
            temp.append((arr[0][3] - arr[0][1] * y - arr[0][2] * z) / arr[0][0])

            x = temp[0]

            temp.append((arr[1][3] - arr[1][0] * x - arr[1][2] * z) / arr[1][1])

            y = temp[1]

            temp.append((arr[2][3] - arr[2][0] * x - arr[2][1] * y) / arr[2][2])

            z = temp[2]

        else:
            temp[0] = (arr[0][3] - arr[0][1] * y - arr[0][2] * z) / arr[0][0]

            x = temp[0]

            temp[1] = (arr[1][3] - arr[1][0] * x - arr[1][2] * z) / arr[1][1]

            y = temp[1]

            temp[2] = (arr[2][3] - arr[2][0] * x - arr[2][1] * y) / arr[2][2]

            z = temp[2]

    print(f'(x,y,z)=[{temp[0]},{temp[1]},{temp[2]}]')

    exit()

if choice_input == 4:

    # jacobi method for 2 variables

    print('Enter a coefficients of the system:-')

    arr = [eval(input()) for iterator in range(6)]

    x = y = 0

    if arr[0] < arr[1] or arr[3] > arr[4]:
        raise ValueError('Try matching the coefficients condition for jacobi')

    for i in range(100):
        m = (arr[2] - arr[1] * y) / arr[0]
        n = (arr[5] - arr[3] * x) / arr[4]

        y = n
        x = m

    print(f"(x,y)= {m}, {n}")

    exit()
