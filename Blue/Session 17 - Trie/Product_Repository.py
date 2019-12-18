class Node:
    def __init__(self):
        self.child = dict()
        self.word_count = 0


def add_word(root, s):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            tmp.child[ch] = Node()

        tmp = tmp.child[ch]
    tmp.word_count += 1


def find_word(root, s):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            return []
        tmp = tmp.child[ch]
    return tmp


def extract_words(found_node):
    result = []

    if found_node.child:
        if found_node.word_count > 0:
            result.append('')
            if len(result) >= 3:
                return result

        current_keys = sorted(list(found_node.child.keys()))
        for k in current_keys:
            for s in extract_words(found_node.child[k]):
                result.append(k + s)
                if len(result) >= 3:
                    return result
    else:
        result.append('')
    return result


def threeProductSuggestions(numProducts, repository, customerQuery):
    # WRITE YOUR CODE HERE
    root = Node()
    for i in range(numProducts):
        add_word(root, repository[i])

    results = []
    for i in range(2, len(customerQuery) + 1):
        current_query = customerQuery[:i]
        found_node = find_word(root, current_query)
        if not found_node:
            break

        result = extract_words(found_node)
        for k in range(len(result)):
            result[k] = current_query + result[k]

        results.append(result)

    return results


# numProducts = 5
# repository = ['mobile', 'mouse', 'moneypot', 'monitor', 'mouspad']
# customerQuery = 'mouse'


numProducts = 5
repository = ['code', 'codePhone', 'coddle', 'coddles', 'codes']
customerQuery = 'coddle'


print(threeProductSuggestions(numProducts, repository, customerQuery))
