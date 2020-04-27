class Solution(object):
    def numUniqueEmails(self, emails):
        ret = []
        for i in range(len(emails)):
            front, rear = emails[i].split('@')
            front = front.replace('.', '')
            front = front.split('+', 1)[0]
            ret.append(front + '@' + rear)
        return len(set(ret))


if __name__ == "__main__":
    emails=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    print(Solution().numUniqueEmails(emails))













