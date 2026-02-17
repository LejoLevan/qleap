def extract_counts(count_dict, indexes):
        """
        Extracts the outcomes at the given indeces from count_dict

        Returns: a dict of the extracted counts
        """

        extracted = dict()

        for outcome in count_dict:

            result = ''.join(outcome[i] for i in indexes)
            if result not in extracted:
                extracted[result] = 0

            extracted[result] += count_dict[outcome]

        return extracted

class SimResult:

    def __init__(self):

        self.counts = None

    def __repr__(self):
        return f'SimResult(counts: {repr(self.counts)})'