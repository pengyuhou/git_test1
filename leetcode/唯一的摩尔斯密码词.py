class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        s = 'abcdefghijklmnopqrstuvwxyz'
        mers = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.",
                "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        a = {}
        for i, j in zip(list(s), mers):
            a[i] = j
        ret = []
        for word in words:
            c = ''
            for w in word:
                c += a[w]
            ret.append(c)
        return len(set(ret))


if __name__ == '__main__':
    words = ["gin", "zen", "gig", "msg"]










