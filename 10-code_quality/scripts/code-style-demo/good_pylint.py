def find_reconciled(transactions, receipts):
    """
    :param transactions: a list of transactions objects
    :param receipts: a dictionary of unique transaction id to receipt objects
    :return: a list of transactions that have an associated receipt
    """
    result = []
    for transaction in transactions:
        if transaction.id in receipts:
            result.append(transaction)
    return result
