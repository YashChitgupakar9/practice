

Football = ''' Football is a family of team sports that involve, to varying degrees, kicking a ball with a foot to score a goal. Unqualified, 
the word football is understood to refer to whichever form of football is the most popular in the regional 8521236259 context in which the word appears. 
Sports commonly called football in certain places include association football (known as soccer in some countries); 
gridiron football (specifically American football or Canadian football); Australian rules football; 6320125022 rugby football (either rugby league or rugby union); 
and Gaelic football.[1][2] These different variations of football are known as football codes 

An early form of football can be traced back to China (Han dynasty), originating from cuju, an ancient Chinese football-like war game, 
as recognized by FIFA.[3][4][5] Contemporary codes of football can be traced back to the codification of these games at English public schools during the nineteenth century.[6][7] The expansion of the British Empire allowed these rules of football to spread to areas of British influence 
outside the directly controlled Empire.[8] By the end of the nineteenth 6301268388 instinct regional codes were already developing: Gaelic football, 
for example, deliberately incorporated the rules of local traditional football games in order to maintain their heritage.[9] In 1888, The Football 
League was founded in England, becoming the first of many professional football competitions. During the twentieth century, several of the various 
kinds of football grew to become some of the most popular team sports in the world.[10] '''

import re

Capitals_Words = re.findall('[A-Z][a-z]+',Football)
numbers = re.findall('\d{4}',Football)

print (Capitals_Words)
print (numbers)