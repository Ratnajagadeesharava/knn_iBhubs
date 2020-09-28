def l_norm_distance(vector1, vector2, n):
    d = 0
    l = len(vector1)
    for i in range(l):
        d = d + abs(vector1[i] - vector2[i]) ** n
    d = d ** (1 / n)
    return d


def find_k_nearest_neighbours(train_x, value_to_be_predicted, k, n):
    l = len(train_x)
    # print(l)
    distances = []
    for i in range(l):
        d = l_norm_distance(train_x[i], value_to_be_predicted, n)
        distances.append([i, d])
    distances.sort(key = lambda x: (x[1], x[0]))
    # print( distances)
    k_neighbours = distances[:k]
    # print("sorted")
    # print(k_neighbours)
    return k_neighbours


def classify_test_sample(train_x, train_y, test_sample, k, n):
    # print(len(train_y))
    k_neighbours = find_k_nearest_neighbours(train_x, test_sample, k, n)

    predicted_y = []
    for i in range(k):
        predicted_y.append(train_y[k_neighbours[i][0]])
    counter = 0
    # if(k=binadicted_y)
    predicted_value = predicted_y[0]
    for i in predicted_y:
        curr_frequency = predicted_y.count(i)

        if curr_frequency > counter:
            counter = curr_frequency
            predicted_value = i

    return predicted_value


def classify_test_set(train_x, train_y, test_x, k, n):
    l = len(test_x)
    predicted_y = []
    # print(k)
    for i in range(l):
        predicted_y.append(classify_test_sample(train_x, train_y, test_x[i], k, n))
    # print(predicted_y)
    return predicted_y


def accuracy(predicted_y, actual_y):
    l = len(predicted_y)
    correct_predicted = 0
    for i in range(l):
        if predicted_y[i] == actual_y[i]:
            correct_predicted += 1


    accuracy_of_k = correct_predicted / l
    return accuracy_of_k


def predict_k_value(train_x, train_y, split_ratio, n):
    print(len(train_x))
    length_test_set =int(split_ratio * len(train_x))
    test_x = train_x[:length_test_set]
    actual_y = train_y[:length_test_set]
    train_x = train_x[length_test_set:]
    train_y = train_y[length_test_set:]
    l = len(train_x)
    accuracy_with_k = []
    for k in range(1, l):
        predicted_y = classify_test_set(train_x, train_y, test_x, k, n)
        # print(k)

        # print(actual_y)
        accuracy_predicted_y = accuracy(predicted_y, actual_y)
        # print(accuracy_predicted_y)
        accuracy_with_k.append([k, accuracy_predicted_y])
    accuracy_with_k.sort(key=lambda x: (x[1], x[0]),reverse=True)
    print(accuracy_with_k)
    return accuracy_with_k[0][0]
