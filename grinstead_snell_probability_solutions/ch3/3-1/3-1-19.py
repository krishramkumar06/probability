import math
list = [10, 31, 100, 365]
for i in range(len(list)):
    n = list[i]
    d = 1
    for d in range(1,n):
        # print("d: ", d)
        ratio = 1 - (math.perm(n,d))/(n**d)
        # print("ratio: ", ratio)
        if ratio > 1/2:
            break
    print("for n = ", n, "the real d is ", d, )
    estimate = math.sqrt(2 * math.log(2) * n)
    print("The estimate yields ", estimate, " and the variance is ", abs(estimate - d))

# for n =  10 the real d is  5
# The estimate yields  3.723297411059034  and the variance is  1.276702588940966
# for n =  31 the real d is  7
# The estimate yields  6.555541563800554  and the variance is  0.44445843619944636
# for n =  100 the real d is  13
# The estimate yields  11.774100225154747  and the variance is  1.225899774845253
# for n =  365 the real d is  23
# The estimate yields  22.49438689559598  and the variance is  0.50561310440402