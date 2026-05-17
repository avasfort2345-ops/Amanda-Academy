# Michi Studio - version de un solo archivo organizada
# Generado desde la version modular conservadora.
# Mantiene el comportamiento de la app en un solo .py.

import json; import os; import base64; import sys; import shutil; import random; import math; import hashlib; import secrets; import subprocess; import webbrowser; from urllib.parse import quote_plus; import tkinter as tk; from tkinter import ttk, messagebox, filedialog, colorchooser, simpledialog; from datetime import datetime, date, timedelta; from functools import lru_cache; APP_NAME = 'Michi Studio'; APP_FONTS = ['Segoe UI', 'Times New Roman', 'Comic Sans MS', 'Verdana', 'Trebuchet MS', 'Calibri', 'Georgia']; FONT_FAMILY = 'Segoe UI'; FONT_TITLE = (FONT_FAMILY, 20, 'bold'); FONT_SUBTITLE = (FONT_FAMILY, 12); FONT_BODY = (FONT_FAMILY, 10); FONT_BODY_BOLD = (FONT_FAMILY, 10, 'bold'); FONT_CARD_TITLE = (FONT_FAMILY, 12, 'bold'); FONT_BUTTON = (FONT_FAMILY, 10, 'bold'); DATA_FILE = 'michi_studio_data.json'

# Asset embebido para que la app siga siendo de un solo archivo.
# Asset embebido en formato compacto para que la app siga siendo de un solo archivo.
_MICHI_IMAGE_DATA_B85 = 'iBL{Q4GJ0x0000DNk~Le0002o0002o2m$~A0F*db)&Kwj2x&t@P)S2WAW(8|W@&6?004NLV_;xB!2kp-1`G_jc_l?b?oJ93kx>fl4;UDM5DXHNiwhWV1E8vJ*C1*y>*7&|3vi~S7AFJg4?wI^1hgDzqzI5Lk`7^OfY?b8whf3~UQ$p3WCwuQMIk}XKz0g{t&xtzPC{ZQ7Zici_W;>8xjCiD2zN8^q~?VN18EK*mSHGn2x4$&a02-sq9lJ21B1m^1_tH{2(hG@3=G>_85ksPA;eS`Ffj19FfeR8j}SwINkL*!B3Ot8h?&yT7#Kb+XJFusWMB}!z`(#24GRbyZc_le&7C112-6vI7*c^Eo(y>m$qafxmJx#igCT<%0H)SIKSylfPyhh297#k$RCt`+{de4CM|CESKj&24dpo>&X5Ps;Nu!)l00{&F5xlGo7_f~4HrU2-vDesMuft;FyiRKtoG{7cAc6!42_!%P31w*{P1fZ2=C`}=y;bLY|ESyjcE9gCqY2HL-|whD`pny*Zr!SLPo4N2$_^jIITI0lTFa+uMhSot0Fc6yMtxO|A}9j@7+^pFJ<Wju5)y`z_vyq0$;=N)Ap}lhTdjB^Q(WTAC$9jhc$ZB~T7i<bt|5S}R&BZD6|848^A1udRNUmWx|{$Z5WoUYN|8<a2J~!3oplK)tM!_VPmuRY#rlM+Q&Nh1dPT#|oINo~Ha)G4jGKcKRLOg`rM^MXS#H7Xt8`@)4K()yA_CDluEfkG=6Ro(iMw+b#Z@{+2NB`iS*AJoJnwdAd777i>U@t4HD_?H<Li8Pp&(G}BIi!s*-mOv$Gc&V=iiGnC1%4+?PJYcOwVa&+vYy|7F1PKx-fkL5fQhI-5OL?n{znVtEdtJe{@`05sn->_osLMX%eZbs+{BCE$W(#!Q9CzthLtKb00h0v#NG(9x+oCMT%~$NR!>$S<tYtHagdlfgnYwV36ip1Og>V(k)r3%_FPhO$8A}QH*mwyTf<{nk{Bj<0R(pomX8uzN08I#wZkpssRGL_uk1l3U(@<a}z~z`=SRnb<UB3&-v_NV~sVl&OTA`-b3}QwaF$a6Gc%pGtHnB5S(+}QV)oT*w{Ey%uF_jNb!Cisd46{iYSRYB`yKvo&Ui)zKMvLbLX9^5(x>QqyRul5Q1{k!~q~@vb#zuEFfh8<=(do6$YuoizkIS2Pq&>QT5`T_j5!5L>v=X6_9z=wbQ+dNS0^C0HlBfN$I_Gi6^0|N}8#c_9L7~n~#>rxt=FVXylp9JVu3bAQEInclfefk`h6CEdFfH&01@tE*#(C8nd)J1&Aq15~Xw2TL~hf&{-!b8%~m>Id~Th5}>(gaT0gy_$CU>q3G0$i8xN;p!{^@DzpC9;`lb_K6s!mFlA8qY-E|aB_o9(1g}B&?!sEI;V6zen2*S-6nk(ES0Ew+MNt&lXqGHgk+!`&7rrNAj^nsvo&*W1^2xmyXGW?Nl!VUP&>$nb#QIUxsbs5yAYRT{!<nIOI#b$D2PLS2tqD(3H!c8`jze0Y%m#+eNFg`{dGBYvV~inc`7O`Ezy}Br?>m_V%xsM5(pCaQ3iZxwCw~x;F{Ue;D-pc+Ez6;J6J)IImJ)(4G9?omYuhJA022TOwHpd&yR}5d+S&RS5rgU6mP3QSL5QMgmf_0GM2z5xI|ostPytL7waHupl)B-j2}A&?GEp4IXgfO!N#894UlCbrm}l)n7fo+;ktvCYxoLO@RUYbHP7o&PWXiKyAXQ-|W^S{-72d=7bG!$oFgXHuZXS_yPDR0_L}xv7G?_5y2{hwsCRGvdLV%$ge#+wM0YRFQl88h^<{ScNN2E%`6uet)^Yt#LaN%xH*O=0K?{e3nG6lU`y5W2V0CLW$N^A3oNP%;=C^>ATh|3-6ELo{uW}D<^N5Olgoz6m4b>4MLi~%5^xJuiYs_I>LTtXmnF7MQHNL8Kd&MF1!7E=<Mv5EG{Y2e9jOgDHvXN4=Y8*Yw5zW^XId*2jY3Fx30ex9j{m#%1g2+nyTFEUr?c1NuT5bmNg>_vsy(6vi+E6fOKxvIMCISJ!ai0RB1H#*m~C{ATj6`dWU>mn(-b%vgdh`RKYo{~<H<IpX>?2;3)jkM*bRIoA3B-*Zxoy{W^{3SXkP)0;Hj?Zx=f+Sa(C!2u{8*5bOdl=4y2o$``ijZ8Rtl`qIQLJ5(WYUx|oy)C6WUXz#xpN6PHXYI(Ls)CO#*$qOGg@nnvB6InPD53-%uLkM>%(`?a-xM@*+E3a=bXh8CQHnAmi1laA9Q1hREa2wV`{SksR#?&Zf$1J1L8QIQAnEcHtv?=NfF2KT#rG!0ebG#JxgAc3DoAmBBDIc(=<ExBQe}>N0tqWq_Re%PR!@N9t1G+teJY}vn-|AZ=V&Zg1AG#C{(ppuXRP~*5V9BFpjnD0})B<^)BgE^G~(WXy_dAdDhgm)U`azeC`OuZI7vTDP52V&bdaT(f+0u%Rta`*99rh^DIl}&2{R62p|&GM!l{b+@dISk}f18hTn@wSfyDuesQI42(x;<uHR?1wVQs**3!0C#9A9plkSW^hhvB+E|t2aVz-Cy0~urDnb`N)Q&Vx7Jq{6-%Vpv&%s(h0JXhHuFmqBaog^3XjA`CM;y6U`|MSC)t=u10<tVODWIc%|7BCf70||oX`D}&_X-472*2GEN;u=;IwgSUL=lF7F5zQL5<1-=vQ4~edY@Jn`9$^k;9%phJ?IciQDwRs@$4E=Mcg^dh03nGJD1_iSIOrkJ!i;M!=9v(+rFV&vmP#dJZdwis3VC^ksB7ZW&ROcypYrUS9Tdyb@n)F(nXH4J<ljIDedtNQeR^Y_<VQplqAjy05XxOn=Q^ia$(ANFTb^{!=UiNMJ`vE(i_ANI7hUJ)#*`gThUz?t7iXpF&3fQwVz?n4iOxp4&+<dfH!D@0{k8Dj*5h_MSLyiWJXiR>Q5QWjrzV}R3aG1vMzCSgTcNu%DJ$sMW@2uiTG#+D-U9O;m!}@KmBJXlEFwk7HSoC>pD9$lCu8Q8>9jb&SS#Y0iHN-S%<R2{gIQ;;rOZT_eFBMys4#QW%N5*PCvhNi>$=)HBMa$BMF#lXoAu(OZX{A^^O%xi0yCSc3h%s0;w}UlsK`a?xG<6TzKdLGn<q*$TH4&J@V;utKMGF4jQnbanAEF=$^k0M#fX`inIP@Sv%vvQ&8?l4!=ke!69K9cTzYWc6QELPdJ2Vt0yj}mX=YZPn5>PVy5pIrhlYlZjUHF;hlYkG#>ZE!S{IcPF)EoiLP`pTsEGJk@`jl>%uNLfB1>pG(zWw)A<`ehq0X_f#O>aG4PjD6>%j`QN2NGXYs7oQ#)tIHrbSfTrb<%|23un0v*5&TX-9!0op&=|2zNnb3_}Go0|l+5^>`6AAG@~24^Fp^+XPUg#<k^NXh^4;SvqRn^2|oI=G#W?0TpUvHrtq(WM=Pu6h}nNY!ndjOzcIhH6U`%8)HDkM5^k&6A=~h-j$M)LJbj|mn;<#Vh%xMAsF&LWnv><MMOl5H7Xi12Ap?L#N`Aa74ag}Tx0QKBWsMUHyYmgI7yNuA@wfL!f&m$D#X@Uh08MM9Oq(^7?!>B5byGQ-|j<qeeD~!f9A78y**RYQ$!TUah_#Mm##ej+RJZx(+{m!yCIvFi1J)ADAYNZ=foi9Pyl2o(#(nXdG1stiem+gG0r(rVPkA$nT@LEX^PZ^jTG-SGTv|$$I6^G8f*+lk(b=5x5NM|GZRDQv4<ZSUa?|m!GeQFjx1iXgpE;%VWVF2MuUiKY{Q0$_i2_{!%-Z&+<EUK8;KV-#)}ve!e^|;qyqJhS-~u-tYlOGU!)6B(6vB>P!=c3B2xG_2*fJlNg>{g7aK*)6l8&lS~fXBNsOurDKS9IOkM#naqA&*X{stwDFKnoauA4^iP*4;LX?>EJR>4&jmvUH5lN=Wt&gL5vZ&5Ts@9tTL?k541;@QK6BpV~Yl7x^-m26fB2i^)II^KEr)4g*u0^dwhl*!5tVys&i<6=_h=`eep1C}m@eO%^DM}I#1t|%HV60)K#~=LO=RWe0XP?;art%6$5jnQrDWwX>tS)Eap8iFz{h2p!dclQDhK2?Q2Am3<h;za-`UA6xL$z9=Erf%aL?!%L#7mg-JmYpR1CbP;qezotQc-n|iARndA3b(_dTinwcYfo$_ujW)aKX^Rq38DPefeu%x$(U7F1_~JB#KMrq>-i~Vj~mo*SU~{rA#a$ATSy65`vf^v(&P2S)QjU0ZJ0iF#_UJ3C4Qw!m-m5Qc+|@G)N49jNy>t>6~Lgyb#ce-!PFAZ>-7F6y9-I47LJ9NutCmo(&g8rwX47pf-v;G{pVG-Wg+6MVx15=RFY_LtcE#3qiH5Pt1tjwiCLQ{uFp6xL*Ox$ocj&7f_N8rUbmIF~&renyT15#)e`>xjQKpN`k25E}t1di9sfcnz_UvCUNqGPkicQANYu*zE|9u-qNyaY15*GJxmSIv5Dzv=Ozud9y)#^V^11c*>u(AfA|-FMv1MbspgK`=EB5@iP5Y)Y`cRQl}%@6*)i$%D3cJBDK<8nuD|ae-}~tO4^15#;mm37;y7Xv2l0mM>dBfl>()i3<ek6su9fT8rg;WP+W|eJ&{1pQo7*I$6tq<50hKmCMI6P1nG?26nNoxYx^)*}Pl%vulypWzE0jD1@;rqK7s?h1$eM_aAxO}s6(Eoi20_rFzqN5lyJJ&|c?HIs+WJKMV$y8m_oSq=t>77^ES5}_nWHE=brH>M7Z1()YvyC;z4NZkq9+AKQN&DvNh;;?$3O7l5B|gZ`b;#OM4J~>FJHcBfrW97l{^vHD9Cs|lDTj0-@9#Mx-QlkKJW62fA-gYdD-ffd6u=?dQ2SInZlac*7d1o-tj3}lV$1m?)mPwZ@c}Wd+s-o1*Oumo@&WTxnh?lrA8w^Hl2>v^W#(X5vMun>I*i#>wo>>(pAgSJk_SQPtv)P)Zs1&|MDWv<+J=AQ519ge$D>j%$W;7S%N2z<}vC?1-Z)z5~{ICp)kf+!$v#(=ceh-P;NfeO;I-U6f_Uxj%!Rk{dn{Hg|GEAshwX4Fp4zKRRyhQMPZDIOymizqR-aN&piEYo2h_O$L6-DXFBJ6Ta~R4h$s$B!yFrP%ZEPo$^ZD6PEK4g*ni{d#RIYBJY#`SF(`==K>$N=hW9ma->!q(#wW%j?&;~j@#dS}@bf=uBMUEKorrmsN4;I9^Ygi(m6TPDji#q+|N4L4f5+#)&?B;>Qo3kx;L_#GdLy#Pl`^Yd$z+IgijGXw9y~Vw`0=qiuw>2B-}qm@w|?^`pXERkyQectc-D>p8XjFHqPB=a6h)nxC7nO)lp4x{CMVErmV}DtJ_oeLlmJ;a)<nM3i5yr_n<q@Wd}+UnxhEw}Z+)zDB~RB2*e>%4uwoi6^YE;Nl|uq!qR7T_%8F_2jEv24O0{o+IPaZrt)6Ewpu{H1-0<$!Pk#EA_kLV7U(<s(UwGc2&wQKMZeJ~h0R-g5+G($k9+~>q;X`$2ypxM=y6!iA?_H6xPP`{Db8O<a$#e)9>V(v4VLqX0u6dTSjh}sX+n@cxd&YO}TUkvmU%KGD1${%T+)O_OI-YGdH0tq{?Z>xI)uy$^y*<D9Tfh0Tn{LYUOn8p0o@X)PeeQftAkvwd*C>j*6Jt~;G|Thm<uo9+7;7S9XC0oi54|?|qD|jY5ti$K4gs?gD=~^!*uO$_H=m%HKRaI3{_@;52?Z-OM5YQSO4}=3PK(#9VT+lBkI-?6VpUpGR{}^tk&T~x;L(r0_urk#)>h0bSFh>SQx`D^2qet8^eWx3c;Q<&Z(bS0T7K$|?|%6spQ@*+v&>47rx4F<y*lr@V_6h!UxO;tQamy?^)G+_zL6b!*7hZ@*tqnCONNHMVFzjEYPZi)0q<o9^5#veU$cJEaAavD`|?LWF<qN-5o@z@W1hWeN-PqvkP(`dHx-mo%=yXOq0l;W+uU-kPleEONH&dP0uizCtzT*JY8zHVWm0%GIiqbeJEz1#Bt#zMm7Ky8Ji~MIA5dWk!xPk!T2{+q$&m^m6hhl9%sI6cLlhNcBv7X!L_+L|9N+*U@=6}$L7qrRg;WRv6{uHug{SZlE3+~SNQj9|JEs}2l2PU;iXXl2!IHzON_6A;73(WWl+V~hbBRLcAq58V8BMQ=_08vRS~pOUm_Gh*AO7@*Kc1MF0s;pW^9&OXw_Ge5!$UoTVoQn5Ngb&)*Ia=}?FZiXFFWsj;JV)aAKP;NdF9A7CLHJf<Vq4NNL<DfmoKcoeBJ7DMEjrK@h|UvA15)#k!NyHPY^?%;YhuKX9$z$;4FxvBw;cwDIN@70T4wdj@1}P<cU17XZ9dY5{hCq#uKYCWFr$NHc4PCtQ8_pP(x}Nk)b3KL(FWL*)XvoVq(iSvZWG55sc*|rYPb#;>d>bf14y^t#4kJY!sEsrj)3)u#pf8gJR=J1LIkV3=tb<@4byIHyscv5<K+*p-Oz=stmT6a}EL#@!ls%Nl7C@IzCBGy*dR7pEHpyB{q&h6ut}~GDe&a*1Y!)21$}YRaC|KLLVnm5feqkl%}cozLb>MJE-?wM8sMfv(1T0eLc@Swf)}j+)M0Vyl{APPn>0StEWP1Ab2JAWB_IL1fI5yA&qWcxqNinuHz_u<<qw;ShVQ%KmO*aM!i(28e_z}JkJFZ#}O24SiCrK0Rn`XMa0KOa<8JS<isVV>YZQs+Sk8$%eBJ`UbA*>S?U52wn`2isrVhFgp4hTv3a(oFFCq$_^v&Nzw!B7`<E<!>wo*DJj*zD!A<ME_ufZQ6dZP{%CN>5*Qm31P>=`!HU_FDiQ}Fg09MsG7rr0--^@(GU8O?duq23T&|1Vh^|_6r;D-|?ljY)T4DwvqClYk}N<~1bMcOMtNj+sb2vM9Ek>DC54t_r}#1JJSmt|zYhA4N$qzcLo?qg;UR1_yqA!#$Knw~>+y8G2P#wM()LJC(NVB%7#uh$crp^ZW{rWwgSlNDSzp@M#m!pqYdpNP`&amw>>aRRZxCkzw6>t}yu_oEM8zNqhq*RJVB!!ePVS^8I}@g!0lzc4B++=#ptji|D9a{89t&rPOO?jQQa-+Sj3FTE~KdX!0nKSe!}7C9l*I^$*{VC<EcLzwExM;`yZpa1o0ZSqGque!LeoO>r^7%<{>jwU_Blz<XNo<Uw&$JKmk*ZyrIS>9jz+fRLP`TBK~we-0e1Ets<B39HVCz0o^V)Za)+}oqGa-dq-A#?N`ZF3zFgaT4+@YOP0BlDAWQz+13n<T1MO;T>hS}1hJ8J5waB!pUAQ22z1NY$e)^^M6`B^D(mRxot_m(Kj#00zpcO(hTvPyi#4;%*7VhK!1eN@0U36+?lgO@~x1UVu?8v@!`fZ_V+E48T#80K{yX$_&TWJoV6{&pr9f@=|i+niX-R0%lJ-=X`9}lZ3dXWh>Y-B5z2olkB|S(i=B!7_c-pHTCy@{Flde?xln%F`O7vifyH2%86PQ%M@GBP$m<{6dAVGM3F6*>Y7iw6xM$BgCC2>#$T~=)%gQ`>T?1cRZ^9p!=Ho*U{%lF6GW-sxSQ55?<3B}r#|?9-e;sp6r8nFVF82wW36dbq!fxE)X(I-H(%j-YB>$tUcs;2R70sy;M71_1;*O;{5Mi1s5l4WX61Yl>Tm6=f&<SWOdE_sxumAXXWDtJYlUN?A|gD?vDJl~@Gwj>EZO#C3qhvqpZmzitjpF94=sx0D9>5YbQ+({b&c~EB<0;JhrjXM;o7+S%zu3TjYA9e?b}~1SH@3_Y=83U-g5cLC!Q3MO1XUe*l`=#B}<o%oES-xIF6#hMGK#J_>ruhuH3NUv2WgU&2azKOZ($SDrCX4pOe!e&asf~#znoOCq|yS|KY>W?On8HrSpyyX0|C)H~|Y-m2NEiTq4k1aGS1^?N&Zj6H9ZJ158B(rW>q3C$pJjv;Ud>&piBCnPlT&Z{l-^fVgR9oXxH{Mn<)(mn@7L{@$a<zy7sb@BQ|->to|F8SgUhasZY%Vk6#p!vcLW#9&2@+M3m}aHRCyQ(IS;<15#!j9ksLam0+X*-HhN)L*@N$<DEf1II?c{E5%J{eS*;?nURg?h4n+N%Hg0VV7sAzai~K(ULYqZTb4$;ic|L%A#(ggL72Xx!f4jg$H*|g^4iT`ng;DbiF5vhAb;GVbj#H&VF@BsggCWUpc(6r+ojR{VLM~3w!!YNuH$(`+Hct0riwBlI7k|>he6#lOz_eBMrZO{MhQg1%svPb7My@7#v!WB%IcBCOyq8;W?BW5_OA=S=&E!^vJP0zx<U~zwymW)~(E(3yU&a3KVGG?NJ{<)#bS@o!t~V{p!$=y3sxsf$}Uf&XYL}SL$g{cbJlha_5@qiD<@F2};JqXI*sBI)<4@ym;qKOAIh&_1eB?_9aX=u3f&Y9DB){j|AatJ4I;W16TEp^9Cv#2R1XoD20Hywqk3dR4%asnzXK&leuo$Kum@eS1ej>yi%4bXf_zs8O}(EV(%^*h;~iH`wowO<o~|!zyI~0L{fyIJD+tD5$}Av>meklwX$8$Tx8DrzUF!1{cFCVATV>cI1*h1O*JMgMJrW?pa>Z>U6`sCtl4_QTKmWY-`lx;=TND%Zm5^N13LHOY^iBf62w`_+2<meliW$}#fum5;#Hl96LC88f0aD(9xfA~nLH=&P!tb!1T)TvxX6{3)r<O;RFkT)-?{USCm(*;Mix+=EfD89zQX}?Zpia9Rw4n$m|3f<P-6|xQ5(*hx>e1n91;XOskuhy%9SCv!<ZRIk70i1@vZfIy4Ph!oOG#!%k1l(;na1`Ke{mmC}6~IT-aannV*_Iv~v#(>%6>9E$J}p?HS+QIT0a>B0_ssOmIy#&&F<0H}^6aeH}rUZnTB~X4arJxOh3S?~st&ym(=i;b+J6|Nn~!?9vSb)dl6KtmZ49_|&nZhuC(Arq+QP3U=F%>F_*jH|oB%i8|c=77^JfY9%+GJ9Q0pjhO>HbH_?`scJnW<i&B!L?NEB|GB+SKlWsj*rnAnha8UYix1>KfpjL{pcQf;R_P^KG0<0Hvv2#ZiSaR>w_03bttI9;-E_LNI;|s1XT2?5EFJ426rdH604m+GGi2V<w=)^E_4IqdsfT*6B21tE=%>bxo>&r@<&{L#Da|QdQUkRF$1}iBU8WG&ZM{zM>6w&TD?#85duLThO~^#?6h$J}EgLQycu$Xg=ethO-gYjm6$9`B-<}(z=LW?_?RDQpvA61M5l}ecyF*>mDVq_e&Ud9d4Z8q@fNY4WXKA);`*usZyxLQa40Ki!CK#S5bu3CMBy#cuh#xdE3hQXBw>r9bXv(zvVn|hcBP<=LAkDt~iO*%z*}T=pDjhf<L1cChh`*?G?u?MA_r8mYbk`(hs0*9zX;p2NRh$bICEqFpFvt@3_w-uH*Ho$~WMoIcgjJoo(TMA0t#l?A{a}+o$NEYe-uVj~fB6?`No=H}P$4G2Y@k{unjW7R9~+xxSq4^-PUz&KlB8>4nE9&viM;n+Lu~FEz!jh>BH9*&2LL8wW4bcg=HrMcithc+J&!&7$Y5V-)4-srBh1RjMlMK~t=#h8-&wi-hK7*+{^Buplf0LB#j>8uFD-38KVCTO)wO@hB6)3EoF5z<=o_pkIzA0mFVczR8-xOz*%>NlM?_Sh<95m!<}P}Ky5*-t$a-y0`T;`I01d4X&Xr6sAwf(ucKn3od5^I@k!{vhb>ycsfF-YbW$%lxU-<GHrxV-FLiuh`&^DS$*E7e95-gM7f3$JvL=;!OwX+ltRaw4ZVG>7&4<35tdk=8bDJetXVitHL5do$v-r^>Uhl{npX|3%dNJiImN@LV=Gn2gOU1R2Eox3!PgJ$DPotoM*qBSC`WWZ+P#0eI+tXvYKEJbqr%v6e0*&L9GLkFYu6gjp3IiwI)<xosOK0H@NEeiuvqepMM^~fD}`oqV|od%SOTURL$^^~*G^pU$CR8uq^1VGB6sDP~zDpHt*;Gq<tYv&7#pVnk&HjV){#>{F^LfvYg-K6fpODl+2)uRb9N<fxni7y2hj&mWRP(06u`Otv__uq4GIf~aW8Y)R{goF)X&~}zphz@`0HeR+k-L|dl)iV1o;Hq|wjFKlP!3Y^Oo*?WMFv6@RHc@)p9SuQ0qZY^Qj$a}2S>_s3Hs<Gc?e@6?&5rXE6H!M|s`oz2avLRG@t@D;Z6biuG>zjjx)CTr7eP~fo;x>ZjfzatZe*{CG|~n!jf{*QIdHHX#e+!{6}6<Z*Fr3K<ix%|f4|;wFGt*nez4AOBP6U!YLrs8bw|c?;*}wuIrd!AtVA`Vj-+FQgs3NqR`yp7vJ?9b?%%VQXHblb?BleNc4kWe&5(CjGQ!d{4NwTp%eKb+fjhqEdq9ZLr8YWY6;#!*IdbH%&vI4-BoP5AX<I!L0C-T0Xko)gK2`SJLr&}#5tL$46-+GZANZL!j;~ziz((OoJxR`-b0o7Q9-yGa>*~S&GRv_&`yRUgK^sTyic2dKru|akv#xp1=VR@;S&QdFo!Q89UY+G{v#9Nx^UOz^`6KNEqAm633|>UcLZswKddpP>#{`R_z6?<9+&oscp3_L`5m;aXzK9ASdWK5v_k%nsE3u%V+I!s#*8J3uEqdvV(_v#toe>rjJIhM5v<@q*;@1xJ4aFrR$R}$66dDRUgA)X3CRc|0481vsPTygyZLe8WB&BQn7crCLFgu&}q~pvTxc&7!OgZN@|3LFO_?za5dY$<)&VngD1=c1eN_~3oH@_vBA1d2{IFaBtFKRhDW~L+rNt^*#q1KaUbqp)i9Us*>kg&3nCw7Dd=U-5VO{zUgBm|>m1xn(KDCsOsn3YoN`V1CTdmQ;}YDxhm;yDZ#Di%V?vZ#8I;KrO&C;j~J6P=QYOu?5;ej@-Z0@denh0c5F<^(!++{($%w!m&3_u09&ZQq>#&X}1E3sh$(51bZXQ1jFgKv=D{yS6?1&D*}#YwX&=L3`SIyOMekQjVDN$l)}=Exxa$q@jkI)lEM8?2?yUeRS6|R@KZCE$#dv!gDUUch2JIiDLn6Oqk>(d!Rtb7C8Oso$1mvT|%>M$<rSv6dSh4Hq%!N5ao7IP%2WCf~2EXe6wkNwOWi3pll5X5I~|<T81%}nWeqzt{AY8o<(YjhQnuOUNdNgsssu(XCMqO9A3J3+4$}~iz_j!oNkyxG1*%ly5!Qy9lLSjKuOMM#l9~@fM<#gP2BguuH5;1AL$1>R-scB^C+p3kceg(sm3;96uG`i1#X=&MqRNm0WgY~thIXD_uMXtsD(||0--g=&zYgM1zur$0FT>vX$~A%JAzsPfY$sbtZSqMNYS0iG>b68&jdt7tg39NxOIYe9)S4Vd6y(5Knnmx5zQSD`2b?ThS{+9L<U|$#FQzVCrUu>91)Tv(U4{Dr3v>1FJhR<7~jamxwxDlj>MSM`P@qqnVyJo`aGHW>LnMg{rz8`di3dCfAk(xZ^-v0L*sNQAVzpX%vw5hbm9xQ_d=af#}xUwC(;as+>Tgu$-rP`s<CJ5v-worMwXlq6IlWfMNyij-m5|bb|#cW!VU(UU#Mz`z!XiHsDpKyII$|K-ut5IdBM|aqsSRXTimh*%NCey2JFcTR6~BJH04)I-3{ONB22{4kWd!Jv2J>*2#<y`@zCB{B?Oe%7yv55#*l`3YjOcyjZ_s`mW2#l?_Hi{R2)qJ;Jwf5H7|~hC4tOf_%`)qRU(AGFU>5y)&rxSjbZlQL6G{KBWo0Q-G2L_eb240R{E_4d@H)hN=8g0@&qwLj;TGl%CS@idp$=qydW=^Q0wf+LmmOfQ~{8q0OF=fO-LyX3r(!b1ZATE;>LM}ih)M}#1ep6xrt8US$((>Qf5`pt+X`utVUHp5nx#b@EmH<6@ZXY%89%YCXviUMwmiDy|NO9E9H`jcRaoAp}X(C^15r&dZw1yG8xX()a6+S?x=WGm0T1^N<Po?kU!8WXDB5lRdwRL7iMB(h=_?@?m})+z_|?vnKi~a#{}mxD$3mvKwGl<v{e@ha075I0a+tepj0ZUNS0+FA|?|$yQ$_`ZVYEx&dk=Zb1o$C5WyNW&*dWZ!=w33FaTHlsou4!pE@ipF9fJ~cuzBjad?8jfDs{eAT~`-?0EJS0phG_2emo9ni(D-sEBW5L{y)eB*<W2PbG@g)n<}^38@u=0IES#Zaaix%SZ2fV9`rnf-Ivno#i*RJ_gjYI#z`+GJpss;z&S_NCdg_Y^<;unVha`uEdR6V?l4V6q|gyK2$E3*+2s-Bm`bS9ySWM?-{LtO>vtXj%mS6X#oobMphyy#~w<^MA;C7Tj&g=tc*yUco`gAw08AsmuCd8xszN|Xg&j3qb<28d7jBMHKky4)iiTcEzT0B0uWJgI)`utpqUSs4(pP-T-wmNTKvFJfb%pBKMZdYkWEjuz6Pfb@M&5cm0>>O^SqEQOawjsh)%edlWQey=$dUmYQb8aGbz-mUUJ3dw|?|9M@CLeE$thOW`Z3`0+MQuhM}Ah`wo8q5qd@@w!P<XZEWMT(Oy_ZO{0fIguIf#*o<u*$#ciXj!idCxGc@`TAH!3V(f|OS_ZF7;-wsy45_5GrG0$^NlDaKpyv+{FOH)sal%%Ky~!Os5s?RQIz<~ndG~<Ssy%kod85xhJ5bA5y=MeGU{<Y`k_b|po;-f+_~7DURUcG&=sX3rttjI>mzrTv6g7(4@#*ZZ0n8-Q5m!`IHmn7X8PTjhjqN{g{)}di$*rN##W3T%#l<1D$J#Dva74sJ$B!R(E>Ftk$XeCBbziJxotaP%G7NR>+j9*CToNrGKPG_K4hNP3xk-r`WL0fW(a!POQwR2+0Pn3e8qQmR4+w3@Bjn|BoOuV8O1WHXkOMRt7@5pyVv>oB`bS3g^v1To91X@;-aoLqT3uqS_&g;wqL`h}G@DpK0%v?pbGcx{1;6zhPyO3R(y!hblLrwA69DnO<?=vJdFS}V(_6Q0zWBmcGULf&(BAt1gng=OpO!B}XIV37ZoP;%hH+MLqgg-c7E`MCe%{o{t~4G5AR-YP-^eJJYJU>5g`a^|Q^CaGKy=+jwMU;G+J7{UeS4Lyl5r$t94WCxN-Y!(FcEA#;c5Hvsb`Oj)oiqXYP^=`siM@=yYbRZJqxPUzP>B2yEe_8P0WgQD{B)I+n#u0$Ky}rQ}rx!<w|wr$ce_pG%HU|O^r9Q6PX}Ot!i@Q@WR-v=`CNhWMFk~$vA}<hgO07eCr4Z6X0WyhAF$gzE!Vy>9cozTN(|(vXT-QuuLqTnfe9>+DDpou(s1Fa?57f`=@B%78K3yreDk@+fk;epeFJG6-q_ZYtxkOEi0w@8#G--Ew@k5`WXO$nXN$q2Y(7j+KhLpZB1v{p*eKl)|~_lT8hNCP_hVUi0irWg&Th9=l6Z|LzDmh5k|S=5+tNxA5n0{lMo3D5S8{d8jl?q**7+Iw3bddMHESox%8DUy8e|f9~vCG;+m^CAu<f+@O*joZ0*YP*6-N8v)Y^VFjTR8cqI#gIIA~&Ege5PlGW1VCnnN*cEGs<$H$)@o7&Ldv$9&<ys&4$iuzR401=dps!)4tlL7@OK{EF2o^;>dT7BAiRaht~ds28}^3H+SQ{HG8P_wB?QLGT4%e3jgQ&r1si9|GXuxo;2%@~*MyU{{0>r7+lQ23!>K%juKvH)akhhv)p3TX3J+EI!xEh7nFkVm1;7EIaU9uFm2tw)bq|EG`vU*NN~@g)^qUx=f~XIVS078Jw`<_`Q)Dxv@_ymk<IZ9RN5u-U;;rA)zpp-i4IF*X6lP=7Bo%|sAXz2W{Xn}rgM%8rvnVo-YmED1r38WmEg8fPL;(bgj)cOTj}GU*yjez0==Yi@qgO)p)te0cHNmDPoV;=E*;ilCYP9kw&e-J;>e*WYy0x4-(8#IlMiLI)l;<tQ%4y$kzEvAmwvCTe5H#>Pj+Cyq@#a%}v;(c|mJ%QvoCwYoeIt0T!g`;?4n3#*XADCGuXH5xs!_k$m&@#(>OMiFu*R#*jy#JSA*$lAVvfm|fy1%_;1HVScVeqL2oWpYHY6tMMx(4GeX8N*(iP|F$wi2)$qcW8&fd|?I{&No$54Mu~t5m_7JMgey&d>DSt%&L+%(`uOl_`Is9A@V`1Y2$e-g*Cz|Le{VewQvv>fW&(nMF70_*4U61B_b}*p`t2YBu)|qn1hSRDI{n<h3;$^Cg5L6@H8>87ax39UPK9TRMMsb%1vLEK-m~$Oq!-nHAxa<&ESF|QK_d5P*1!0XH}1V^KLgjaq#PR3;;%Q-&Wwl0Y;I%0x{xoXTJLE_CrZ@_(aV~wCIw}H~#ReuDtQubz3&DweXsY&ueuO%-iT&0Wo;tD_-{0<ByCSI2ak*d~l)AoHP$zo+@0e^z|(nl-%!nW_NwG(HI@yJ>gDl-MzF_zI^49O#@NcWky0dmbRYRaF}|QK5>n^?}<Q>(FSYFU{r;%CW@lGUVrN8r?0vBWo!&o*qF!~pJr*jMj|Srs>T=sqH>u_C1&!@JLedzs=+L=Q3QtbPQ(+lHI@O=qLr3&PDG-(fDt4n&N5$5El3CfN}ND(PnF`xt9TJ(ObB_9P@1MtEtSe1KKFTG31bWy4)tsXoMo9Iwl>PMJa|m4tyZEaD%^w2%1tvnNW|t59sv0Yxvd%}aghR~U}j=g26<I&coDK7RdQ<MDC+A`CMZSWu?yx^6U)I%01pfrLlF}ILVKk`LoFwX^FE3qRzER0*@BjA=aPij-Sfba`|s-|j#vQ)MD3E&s74NXlpJyP?&C)vsb$$@&OOx^y!I9E_=Df<Uo<E#(=0>ogeatE2H>W4H+wi_jY6SG65sTiSAY5gA0!{vA5<Jl1&Kl-UWE;<zGyvXe0=NPkt4^)T<v%|z3<r_FIuzwszrl?KF@U~$R?y<u(BsuLYXPES|gCMX?l8#2N57p|KNhCx7RlsL4pFxB9s~;vdn1uYvNML+eiUUY=~CO+?0X{)*5R1>%w(H9gB_Q;+k4aFR})ygAaJo9G)lV#WI78Y4!~wz%VC~0Z3E{97jz9rZ`){2Baw2D2T}@iiioS)|8Xrmud>?f<LIa2h9~gsE5<$=cGc$P;uys7ZooCOonn&Cbbc3(bt!u5S6BzuI-sGl1{>5-s)tG0w}$yGgxK?vOG_-jF~5=r=1SA13`q&L{+H5X2b>^4efFxqFR#Va86&{wQI-7R3nNvUVX{0zx!Q_FI*W@oY$rct%XRMYJbzw-Dav6K1Qf2#Gik`g)7&s+xztPIEq@@FAD;uj*uySp~}eB>VivFE^;fgvGJWx?wlO0-?j7TiIIsL)-PUU4S5OLosxP|BkW)^hE+9Q!DJKy5z>}pQ&kmI?e9}2heCxnpxk*;7;pfU4r;o~9oaargLcA=gJ4kjptWg0%zEZqe+yBF<;<`Kpaid4^sj6iSI|7ci3oErL)*A6<kKiZ4n8cJRpcH0msHy?JTr{WEJ?dk3xIv@#RaR@6cG9F>VuJ3_*RvhElHXl47BW|`DP3Tk!n#_U9UAJC#H-VCL_#{j-M$Yum}vT#0udes1>ObiXJ{beaF7Tdwp77y5LuT_cyM6^-FpNsy=V1cdc}+BGBGk?pf6O4u}LwY+nD9KlSBLeQNvTkCn)@RQYCTU0OG%%7CgmH54!GJ^w|Q@85NB-!r=(8=W3`_RwoKFJEqAIOo|hgv9`Abw)~XVULjYAqS6CmA#6=v15me09`<427K;JA<kKvArU7Mq1B^lwnL;{r=4@t9b{C*xwia?z|7)Z9tkx?S;rtP*W}#n$6|5jT%~I<U~x|72BYWk*`AFzAt<s*DPFy1rMh&<;6UPMhp*e7T~!KEJGG)#V5H}}N2Wh<aL*pi&wt_7fBlJnzxho+ob;6QJfoAtk3TPo$iU#>%U*f2DV0*ME$9K7^}M!j0)VO)5#v{GTzTFV7x-$tcdGvBM|V9rp88S(B9@tS&*C)cyhjC8#TrwNBNc)3G~;!frzjhRe}g+0>1;{iayL6Fr)rqznCoXxU1LgPEoOyof)>&Z<d&ehI`0l0+|L}ah~*SeW?C?ZD&UgRcPFO5z2}%~nBgrO{>OX&V(pgo4QYgKmvpwEfq|UMm#$d(x}SK<(DG%j*)HgL)8Yh@qp@Jc(ArBjNq=RpN$%Qr_**-6*NUbwC#8^XMWmM0LK#|0N+D6G0NkcvrgjhkBEBoN5CDv68rQAyiF_fC&Y9@}bhAe1B<1e&f`FYlsj5O?O{`=NpBTxDrfVmekHU&VsZlCFI?=d&-~JJUHRo^q&3FIyz|w&<ud#|zHSOTtXF;SOIF$>pyy|st`AId#sh-Ywq)ebp>Wfw`I`4`tCh>>U?4e`RM_j8W@f4(_YKeNv2`ir4yRXO)PynIFL+8(l(6wCv=1LhNEmDDgz$9f5;PXbY@+>bb#d(gSGovI<)^0jaJ!jxnXS@051F`~R?NcYlZ+~XbvB~<9OV<Cv7ykK@7hd7AI;omM;le36`*cVNN|fj6lI6?Z{MNTt2l~@Imv)m8I=3r8t5;R7S?^GF_42{o$SB$Sw(prB6LJVbZ=u;gEgm9a_=v&YmqSWrGnh<;D={oW^ZG<Cck_q8&-{)<=bE-Rl!?9b-sRnj^mGj&BhT}BG1fw;UYpUPS)Jrg{|erFa(VyoU})zQ0d(@B6VK$0Ig;n!+<Roi^Qx=2y#057b#QPX&2s~5v}k*vMM3&mQnNxp2?~|-F1_rhf9aPmxavw<NgVkiuP4-m%)%5PQ7EZ_l80Y@!N&8hxzG&8+sEs-Z9Ceq5vvM`XJyP%h=R{dL6nqAmd&nbx7Vj@%tc>k@4a)b$gF7oR7IJnWn7;lWm(qFk^l%y%BCIr{M@KZIwjHU2PlkQB;t4B0b(Ko?b)+ORoR%?s70NWsEoM!XLjy6T$iDZOaJuW|Ne^WuTAr;OFGZ|l;-)uC5wOTXW#nTAA56Mw2|eiM9o%zCnE(i*1qM7R&3dvRVsU@8~bygM@h+PB;J`0r6~9&h2x1-b{!e58{Tm7mZ(yaX1gdNGG;ay1`$P3gf3CY`R%v`)yP`ruGKzu@A$Ts<}AK60f5f^3dUF)MZJA}AR3>Z%yn)~{tOw#xT8JO5|t~z{)g`xTCym0IjGI2^L-$KI`Pi?4HsPax}W^X>tFc_jpNKK5%Ve6*$N@g7Yy}9Ni?0yS03NCtDcgLjm*i7C_H79DN-li(3VRsV#6vDz{Cvmyv&h1*CjC)@KI-L6>eVN%h^)*3?1hRjeF+ZB64`{JP_<V@0@t=A#o|zIk2GZl(X43*~l~6c=7s+Uvjn2zzQp1{eE#I0HbOY5HQ=TuD$LRulujBeEknETeGH?<@qU}Oj1&K6Z?%@)^H^{oW>6vIyPx7!II1}P#DUrTC!A%V7zR9`q`FW6hvNR)`ADACf;}J_;&O4y%Z6Zt}SiXTtd#vOtoZdbmnt`fTxykRY?_2(bH2ghL4|^n678R{BE<M)Dwj!V0$zD-hrcPb<2%cXv`#`0qy)(X*MS%pxK+YnKE)l%RE!As+#9nBhRk7{<@$3m0$d!AA94%70ViV?nRnj#2Htj0*>Jc8T`Pig^M;X%SvYFiQ3-ry0<jbwl)~I43MyTQ80r^vqnl#f+z_HqT;21ObyN3pele#BAW4Ip92wc?`AEFLQQ1J+8?yz8#YQn9Ez7)sK~|`Gb<1I3<nO@h$@(^TDyMzI#@Ds*~UqG;V>&gMjELK+eZ(MjHPn^6&Jnf=YP)U4sb0Fo6DM^{aUM#xoFsTHgheaiUeiRSm4s!mXd2;cH<l0`ZJp@yl`OgVjD&3op@=PJ_HcND6w+p{jv?qhL`uH%3BW~ORZ@&8w{`D`DM~tE)$JhO?1f>R|H8AtSvUiL{`z}Kqpd5+%27w5SL1AR#doQZzIE|JH`XLn0aoDF~-2nB#bEvqpvGOM8=wd{{ARQQkSPP8@GrQtP0{WFMCJEGRW1hcxh6t=2`939%+V>Knb29C{SPsFakP<<37}z3D8Kh!6i$6>>WSvy?^Y!`|tneUBo;(Hs<OLOKgdWi@Y;cAvKGK7aZSzbWhzMPq7llx3ww@{O4h8Tr!b$X<lzMLd6>?LRMuQ#d+pHt?<9n{Mk-tL#nXW`p&dh0@!dDK~uX~4lygx6#DoXoe%Nl%m)wKHc^|-#i!miyi;pCm@<fc=KW*Sql(gC?|D~Us@^pP^+_f{$Oti8L&m$jl*I6w``ph|{GAO6sWT9w$R^|oBDR!}_)Bhh(Ir>EK)oM5e*DQt9)0G?tyAOUX=6In4O(lxG5xETCp(@yIy!l9qP}{d?Av@+MT<X<M#iV=X_{1f)@<D5eMoEqk*FvY&DKFgQ7CUEvTR%@C!H<Lff6E8h4*5qJ31@6$dsxgz6jj5P9_m?&e_<W<7`73Tb8D))~@Lv8q5wI$O2P#5-GrZWO{nk$?8=r*I&FvyeEb5$-zk!)+Bqk?Y`@lTem&Ab=it#m)~&BbuYhB`J7ysVbTeB+XGMB@!4CC?>jKOcEz=?e%WQ$UFi+T>e7`fm#toX{mrkKoR~Oq^jK|r`pDrUYuB%<^z;r64FBzk-+JWs`)ba6cI~quQ6>_y6H|3j6_E1+GR=%$G1f><Q5+f2_{8M1J9kyf<wll9eSMoRz0^B*(%GKwO@%vaYe}j~M0u7`A~bKqiZiEfwZVf+bBIv0@*z-Lf<P<Cah7o%?|qhMl{l$ZdyaxKM_ghl(p3lwAu(_@Z+1@9#OO<3|C+cONuC+Z)*(6&LTt3-$(_IRQ@=2M;Amv*<04=E*ynG4^N;+(AH7SHR<-HOjRyTqp-RHaCk-nR#ZmmdFW>zqzxumwx^9@AxUYTUb8mXbTi^VvZ};lR3q+zgUbtv@c=6&Qw?-AjwW-E|!$+0v(?<_qy<klV&2%%su_X{7aiy$6)!yD}xy05e5xggd1AF$4A3a*1n0nxw-+JbuM|bVqWs@k)vV|Mhz4wzJ>nT@)hve+-WTG@pJG7x--K(eyp*z9MZZ`}KRm%wf)F_T@6wP7EGv>&`1FB$xi6Rd(kwSV|i}WxBNC=i>s+OOqH;7POFi_wsobsY%%+?1Vo<4ANAgP3^ALsR3x83<;zxE6L%ZIeny;4BsDr|tAIC-cuz`Q+j?*lSXuU5-KT9&vm)wt`{uf5?H-by7Zk~dTZzTLq`L{Z6Jd((}dd*&l!Sz|KSC^1s(w_1@{#2KAT$5Tl+Ubtz=+LgPvJ-hXLkKA+nH_*toJ+-wyH7R*6B7;kYuYLKALyH%c%4OTvE3P9C@+>J7jx_-`n(t{TDX}r#YOvKErc^~KDP_6WJVTo<Mnuef?oL$^G0f$-Y(W=YdGYS8Pd{<s$d<viRVI>V98X!89n^~s4lTUms;i#YMM^~K{kDf6FR5XHHxL3b6xwJs2IlM_OX15AGRkxcEO#PujmEa8o{nwA0x(!%*ogC4nw68%Nwo<Dm!pfWz2Y<P{fJQH*hG>G2rwYyBYVO-XW~XwF;V%@BU|6~!#{EO(Bb;nMA=5sP~YI-;0tef;qa2h!z-3;x#E&V!^30^F~z-oc_!!HYm0~~l}egV7FHFC<2z6@MfhB)YbCa`@!wm9jtJ%izMhwiF<yL|TZ4$mfIZ{|*I#|xr@wSKbI0oSO0~=o6nG{iAT^eZ&C<MHtA*U_Q}d<E@;!U@v^O_Uz&q!>FOU>E)L~^njcMc##+Ga(E}wUNBAT3>*njW<8Ajm%RS+`g{2aeQ2dTpQp(P7@DwX=g_~GgL@&%P#&2+94^=#|d=&q?L*T`z#5LLz}rpB|{`b*DSwr<T0H@$Sl`t?Z^4G#1*8Z{E7%!_lHJ3vX9OO>veIb5Ji%nYVb=Uk*`m(?&2b&DxOpea}sGc)tf<#}#7IfH=!Ywg(hcu!xiwGrCN$uqA`b=CSc3l=XP-Fsj%cTCLceQ>G3DAQEh@Loj3hZqI`w9D=eQozK~RoB1p<M%&etpS*UG|yM9UcYqNGVeWiW}@W=MC8Y7fBn1fo;Y&ig|EN)wLks_%onXu(dt0o#V@$>TOa>YPqi9utdVCIZ{FBD(C^iq>`@`WklpswQ!Y!H%&w_)%Ip4-@k7&%2`8CXYY>-{Y00Dh@^AmeAFWuoddae7wwwsmJ2i^h_&B9G0YMuH<q%nxl}eS<--VMBQI=-2vf~Jp<r#b5t;Q&}ZQ}rtQU{w-s~o!s4a{6p!sF765_p%X`1as3D_LXN#=_Qwlt0zZ`Va*uKv^_vHK5Q>{?iA(_=!)w>P@d-cfsbN1q0Qdp6RLSENvtvUa@>xfA7%hbt@0=*_j%|WC_k&7!~rl2Sp|HK#r?ql4{GVOaWUpxO!3ivkC9^WAFI6C`mr~&mWMnX>!gE_x#j5-=0(>=kr-%Nm9g7@~Kb$$Jamg`Cf_k9NhD=SHGe%&?_R`>G&eRuzANH{MO*mf?GfINou&9WN6*;xBTkcl%0w<8ba|QlH>^hvxyV1Illkc)^C5$gUQ5CoEUdCXGnTVc1eFZQg{B~Kw7EZ`Q)C#6~k9ve{F2b-aBb{C=386l!;NI(18M>V2C0c6@Im%&}IH0?JR_#=9|>|(-Sf$R)`gz3Mab47;D+ib~(+>+n8@~1;9;s<pQ>ap=cXzR?GW>3!84(B2_8mjiP1Q5LDTi3=mc3P*bc52C*Rn1vkf0sBiX&4@QxdqG}8P8MEuTJ^%hs|3oLIKJ&l-Z>laTMWrNZq^XKjdU{r_UR5nu5AJ!choeUhjJiDOEk%<jY745pJvJUlb#b}e8y`GmvNFe!O@fl>rAVtQHbm8EQE#Los762W&bM#5=91~-qZ6ZJ7hHP5s`EBvKA)S{z<}oYrPo~bvN!$kzHK|VTyt5eQVtt$v?F;!fmB>&c;M}S_}{O3$@R6#sj=GRmDgQ0ylQc(&H#?d6AU;u35=@f*pZRjKKma-mA>0P@!6e^KT(Ybjk-a&h0BulLkrgT^bM)9GDXSfwrxvA`xY){w%)szAJzlLG7O9N+}z6Wup7%L&~Z=Yv~BM1EY6w{A`C>vDzX-D1nx1!jG{JdhWBPWTILm^O_^ATI0Znpo!d|p+ZtmcG!yR#@ZwEmNg*nRO)CS-Ij5@dPQ8zl1W+ax=jszv<V6V%LaLSwtS$BR60?dAF?(Z85djX#>Z(a8A;5bH)$h*xhwr}k@q52}|NZwb8eU`-V`F1O3l<zYbSQ76$B!SkkyS4hn;1mm9gwMdYmx|2FUx|#-u)9($6WTJ*T4D|KmLZH1w)7T?O%W1rbWw_LRBD61d>t9R{#<yh-@4c&0jN@iwHDe1a#Wh3c#93l^SW5B-X1B_P7!FIU!pi7EodnVgjklGZhaN0#Oo?js0Zf;k)jeo}T*V*X}s{%&z@UZ0FR`V0q={b%%Eyj(qwP8`fOdmxzkf9FRoJbE$sp+3mYidDAcc!rOoQzh(95P{2gYYS;kT<fPP767Nx9LqfIG*GEZ7rRW@5)B+RP&<{?v(2<DH!ZHQKdl4~)TQ$(6s(GGHP6uEQ1fi=ir6j6WJcyWE=9F^|K-9zyz)XataHmkfC<UxB;(g#lC}{HOC(!gx14SlwQ^><m6A6U5=wD3mUZ7xj08AXtU{UYWoC2^X0{9{;$V5@AdAx`)Gy7ImBq>2y(SmIOSwR%Vp7i*{c(q)%pn96daa60-rbfs2?A%?hlt+)B_{>K?KDO_~P&HasG8Jp~O;6SxGMDAzfjH7=I;+<s^p>l6t-fUA+KX<uW^mEMEtg%qX!+8?g#$@BvZa!$c<<Q@G@whiS6a^NZ*R$a0vRT4D@EuaQm{6Ux7J%))Ra-2+;{i4cRl{h_`&11eC(6SL|usbS1wy}-iD1^&Oh(+3rX~EfBAp*#_nyK)-5R!yat$YW6ho86SqBkpm)jeZ~yt9Z90E*!==m=YM5Zy8qR8U$ufp|Nb?NTI4(y?#XILk(5zKeMI6U~hR%w?RT9YMd5{`f;N=2<F)U7)$fc>OFvJrKh+&kCDJ9;E3HENmy*Yq5iB&YD9;0Z%ZB;ePb7M@N=S*anT{CfARc%q_Oa<VIwz)Z2!2wf)2nBWzDKu(+8O3QF4)&s^SX*vEQdNcbTvV*9AyV<uDvv5gRD?1w0*MN^;W7diR(gU%wo)nq=<DsRmdZ<3EQ6vNCu7G?{Kx<Or+yyzp|$Ilh#YZ^Mx<y+ruMr>k3Dp3WZ~M?!<*I|KX7n*baM3Yv0MM?!wr|4Qe5rt8ya4;e)GmFUUc2?ilxg|t?XYgK$fE<1}V#o2^q>II|`%$B>^Zh)~9(RO-nshuRdrarp@0X3=axGTCL-+C}(3cIWqFT_x$y~2cC>z2A3~B|1~#W_tF<%cI`Doix-<XL6rRaU;S^I&KC5P7sdvfDiaBmDMvgp<ztO4VZqV`;++*GfkH`CbLUkh&p_Hj@Cvfe<vB}AR2a5Rrc`O902su8s7KKPCMY&)nV{OTCDegHd2k?v4+_t@3ORuqGNP^pN^YS<B=t0a85LJ{;<8);15)QhwW0bf0*c5kVFt7y{J&iR)&c=+#`oP+BZ{5?9Wq4n&?-L22LT~;2Pqy_p4r&;3jk;;oK3y5_#|&(&KBdV^A27COp3em#n;{bg)i+rH1hDlgD+b)FvRR2S~g|Xe0bogk+BnF<G=YUZ(DuQhN;Qg__5Kc(a~K`KePRbt-GIowsvCjTc5w}8=v|@sa&e|^z;l3uDp2jAO7QCstKOFW&%u;mxKsH25gMYjl%GuJqJGY*YC};{CEHUFKjho(L77rwMtU7THv&sKp~-tiON0ID{p+^s!bctzxIloe)NZ+D$c3PCHK=~Bah#8ui9iuPk(H@_XcXLrryN&9v**e|FH(^jW2s?Z%?17M}g%OHbt~mdeK%oTpUU~C)PXT1)DJyW|o{=8%=HdrmD><;wF4mGyO_H+?r2w9|Mp^n@^_mqRsDcy9f1oTteOPJDn|^?CRe8RjXJ1^soKuU;V+KJahcS<trETsS8F{E^er&Je(xYOiVrYz{BTXb6L5ZEF2zEV=jBiwc=cTx>lR2fA`z>j_yC~YuV1Hwm!M@*&li7izqg7a%Vdmo*bKe^5G{|tXw@cI`-$k`Fo?!?lDR7`(wXy-79aZO;5h?6)#@CZu#kSFcy(&U(X-^^WR5NG%z$I-siPO2>mG`O6((Fy?^`tj}FA~`K2lgJO~6KJI(R-69>nE73Xh!%g_C^Wf6ZeXV?F4Q}=o^&T#<*>Q?56cKT+W^Q+dbDOHlO@u|a;GE_BQ90>`b1i!-a0hN#a^9Qeb*$wM1SmpB+-g-a?rWy}cOF#7H9}e4@H5!e{slLI1+~+uXIFi|njgSBNfB(I5L({yGH>PiT#fwJ|A9?EA-+uItZ%;|ik$vOlpA=s^oqHkGp@oAvX+5t;0@HNv20*>ThYpMPy=AvzAoj=sK#|AMGb59Gr)xfmUU<`uakVUYI=7R=$yQrirp!6hNiNY%@zuqKq4VE%x5_SOkr%&Y`S8nL{^GBH>MIZKJhJw}B_#j~XEc)Rh7IeFKE3PFBO^~d_}Kc3HzLohNH}%iLE<IPJ;M=Ts5;o=d`1Nj&HS?!?^mx~d;JTq|JG-3x%uWB)^A#|<+9B&`5jyLe))6XdSds!#Y>i)Ne5{)LCvy8y$3Thi+6_2u>%Lcb=w^Y#hZJQB+jXs<=s%)J~}z6dcg&oU-zaT&7EW6lert)DOk)z)RhjIr?}3UeLcWxorKzZ!Ufw0Xxc4BK1?x4NXZT*%SAumrg;NZ_-0S#_TdObY>Kb7$vU06MEfAE<ZqpMv+3(nK#7FfzvJKVQ$IGean<(8@of{CL<Ue5BjBp#^$P}joIZHRxAV!mAroq`Ih5%zDYH>Z93>9wd`pj-H^G7cs1W1om%q3k$%U7lcg+hgj;JnF+j8aR<tvA+%D~XT=`*D#I(F#T*83iP?B0hC96Y-7*<BBO?e3{#<3|o2{^$So7d!5Gc(Av+W$lIrPy>lgki>gO$95hcRTEijY!t;wDT+(R+9-<H7-bS7wFZ%eF&ZFVRjHXMLxy3PtW~CPVhB)pr>uc7LKOZCUt?>9piJRw$^lG-V2y^_a$+i8M1YMVo0MRTFoglh8Zt%zA#h}2IE=4EFl>^TtPvs@_5mp>d;yS9Nf)3ty?7hNY;0%=5SmAb7dD0nBEpdkkcO&oc@FPYM8qehlB!y&WK+|~omWT93JplEY^-g1A`5@LwZ56T>YZ00N#elw-uc!eEg~ki#N_L#c%PK2QJ&>#-FqQ`iDKAf+0wWD<}d!`Z~WfvJNDE1;fn?bOL<LHKvSC+RUSVQJ@U=F{_mgv-7mlUT_~AW&_zVEMk6wjuzG;Soia1KnW3b9`MR~%COdcTJpZEAs>TYZxw2)=(kCB%;*uM#JROcCBIEfle*4{zef`@No0R+e8k)P2@s$^B8mUd>`%d(gDic2a%+{T;&mzW(-u|deyHAYP$yEA#*IjhscOQC)BI|06#fuj^NSq|g*Q{nH6)ne!5y@%|g1W5XMIvjwcpI1EYBd0vIOmv60od29zV+fmg0L|r0Bsr(0y*cr_$Z2kRAwfV#D2QLO|vev4Nw!s)m|Y{5oT5>5krt>DS_f75tZP!G{!J78x|1}C8jLPEE{7?@L4L<#=X798bBirvEOD4AixqANWE%;AVdKK8%H*r*FbS(`!pkF8%HMO$BHl!8Jm>LNTL?Pk}3$q!6qj%BEk0_?$4lwKnsM9K!iAo)C)07nkE#fRUeFc;xu<Jc<~Ky`t@J@x4-(kZ#_4%xNm4l%&H(qLvgfj$-)!+NACFG7Z&#~9$2yP#L=Vmi78i4vs!)6u3eQ%rQzL{D=zt&-}rg|e0>E0i1&+^ELpU8*^Z}o%PYl@D7!qZKf7&PJkYoH{EesC08Ldjrq{jgClYIp?bv5PX<AQvdq<Cq>gcq!k<oNmO5>7_D|(%M=-7$W#A4!Hrp@Sy&;IL&vVZ*`5k-P>r6SOBwX$f*l2WytdB1Sc!i^g?mMaxiS-gDls<mqsh~lX3Czfqk4=Ah&rF<<#)+-ofLfKac1Q*EQR#c5m4239I@RrSig+XxTsi+b&*#aU?0W};~$^bbLV$*_-5vZsV5nEQ(q*MxUy4Dss5*AUYcc-Q?&rL4?THeIABfg1t*NiZs39Ke6XbY4ZV;H2&99!4kAb93<C!lx?I*z?|Rf9kTM?}OB@l0xsF(x(!fKgcJvBSrftzNVGf-TQ&-G1Ay-2;`lk(<1s6RtL@UKkPbkN@v~K<;ajJC#aY5*1^3aKX@t@v;7DPs^|N{FJcmDL?z{_Gg~nebL1$JejcrQ^!Z9N{bh7x$HtY{k(4HuD#*fYp=g<dTLs{XzrDw5B&Mxf9sRC^pM=VZq??Vo++73v%I%DaQFU0PaK|@f_>#1-bh9`iADVM)U>NNq?SJY)YfvP>_v_rK6>Kl(Wh(myZu)~7bc2rZ(pwxMb?&=F8YU$eW;WqZ78HoM-QoL3oMK}wxfAS0BCN#1e?E|6w1tojf1vVkx0u$JG*UTyYq=un{brPFWFg%1bpTwWa0ObjT|+aklF=ss8>zBGaPpg+wS)|>7YbxBMVYx^4=Sd)J;rHOiYZ8Z+~Lzq5b<Sy*<YcA9?E0$M^4fu3D+6`t73)H<lWevI-LFw`NHa9r5|Ng{f5D`YS)T;{1(63l}u<MiNKMmM)u^7_apAdXm#Ad=QaxU-FiB{M_IC>hFH@?(c57bX}Uuec!rga>~E#jn|iYVm)o0(u%@oVz}B{As{#A-~Z$vzJALWdyrl`xcJJ!UXt2EV)XPsHI+VhY^v_ko8I^%zxv02;3I9pUV8DG`;p@(%B50LD%WeZ6Nio*-n-w|8VT{%C!UHUJ2^FV_{b4~zTn0eCpIBznLDT2f>ShyBvKniStFnIbMKw=9+um^*Qd`*v#x08^m9E6+nxZ;U0(cFgI^6$QWckHHi|n3J?SM1v~vQ38k1B1@_*htyl6qsVE>M1woM)%Iq}@SsgaS1vGMxkw0iFdFl?h}!SHaUx4L}IWsf}ggqxULzo7S;RZEvL^?7ehyxaM&J+))sRJ!At?Ki*a^$S+50UDtIYXO#IjRqtSx<u%jt<WawIJC3htwOH9`6XYz>XL`Q_t57){57WJwy%D(x@^f$|I*Jzk#QjnqR2&JQloIrs3BuOYMG4%pepLs!#gO1%W?J5+rROJfBxu@ql<=yu3xn{%2Q`Fk19Ls=GN`|j)>8PLqGHrZ*a!@x(m&Cz%YP-7cX2K5*6aUf&QTd8@8O6O-!)U7rf+pZt^Zb0hVee1TrUt+WPxstlE-od6u_{HA0c+MJgKFc(#52RJ_#w*{qAsbqSq~!-<NUFH$|iC=^hylhS;it&_OZsK|j}YxnHg{e=&GG^uC8s*0FQ(qHXeIJ9iT+U3ia4Gaw}U$KHCWBYn9zWVA)e@|b3&tu<x>|g%kZ+1TPy*RI5w`S>Je>F-Q8>0y4t@-lKJ@?%5rG4AB-~8quUVq{FS?cOj6Sf?`=;bfTyc#y}qTYu&oXjPyf~2?n_TT;W_x$R+zW9}I0bE)%_=b1<^w9DJ&N-tqE+r*p@~|X^rY9S2Jl*=pV=l|b$H$KxJZutv&FlV4|4_e@z4M!2|L1rAO{tM>>hHOE<C;o7=_pE(JacT~JNu3uOw-cB{{Qi}f4OecX5VlIq-`f10pTnygn_Eh8m?Aj7;PpJ2bWM}E3L@#yj$@69-Z)WQSnlk1jRa$DvY(pMlu@+@l?EYiYrof_~7%-=lNz!fWl|#_+*F{h2R7!lqu=0z{YyolAIKtK}4>W{_P*XCnDN($wkxCQ_GevUAA=b;DVu2sgxuMGqb|0nrd0%*sCX%B(Cn=x$j^8`fnb(<Le8>U9@8H+P=#2a__kF-#K)2`;l5Ml+qN+B{anNytHWWE${r5r=EH06|a8vhVwV~FB_`+dJ|5gl`}FkH&04LG3@aJNACFYS4WPIyy{0@yZZcfjy#~&lK`F(;J#|(6Nh*1W0QR7AOB^~!_U-4ry8|McxPZ8>%fx1fuVly{OFO9##Cd=VD;4-S1i^v5`R1@-Lw1f0|!S(Ne5Rh{^kGq+b_E5rYz43boi6+w1OhIY--YF9-T~SOJ!53>M1>6r?JZ*h^yD#blp&ZuxA26J)$VC4$Q`wIa}%iQvx8UxHOxbHl0i<P*W*I<;v+ZC7RC{gDerOfn^ZE`)qVf(yZynEUZV3Y^kSL7>-GmBNGvukNwLBzWIq;CJyc|YhH<MUaw6lHIlL=iV|-U?y(VjIXW^il~W|n+S1xfFMZ>$z3uWBUs)=bz019LZiaSeCRT)%VNFCff&$`F$wQQ1!H!_!$O^`ej{M^v|NXsR{A$S<nx2NJl%jH(jA0d4$J4bMv9dE(EMmX7WY(3Vi<U1nMBm!^+%r?@NU3u3kN(I{y!9<hSFOmhT$Sd|XU@8jl{}rE)LdGUviQi@q_4m2Moxb>3M!aV#no%B-Y{rmN_bBkR|hz@U8x=G5>pb==?QIQwwbThVoD^o)YErHOc_WBtRWl$0yNFDsmUg^ez+<G5T;U3FIy|kMBAtoqg49N7ryv+zxn%I&l^Tj@+;0?xaP9u%a``Ep>ki9V`4Sm`^FO^&rQ{)vZ>?g#PL)k-gx=>uYA*wTzcKr%hs&Sv$V5=CW@BJATX;I84jL75)$}~GC%v|)^B{~i}&4nXYJrvL=rEF7p&=BwRYK*t8Knu6)ZeOlw;p>&n;Q9tUi`+e{ARB?T02uoYiD7iels^GEK|oZNK+h|K-hZa-oGfC;)lj)PS1A$Q$Y8I4jR$N?{ZC^cqtnE}x5}tc{NwC#)i*0Fx4tcVsxJ#+A~4I#U*{IRHQ<pO}E}ST9xxRG8x4UW$^lfM-ys5((G>ZhF$EjdnAw;CqEFm*YxVl`^X)Hs8ACwukP%XX~SnoOtd)&!D;BhVxckvUK6fUWyfx2cLkFDk##}i1oSgllhKEcR%&roriagNzJag_TvBX5ARvIX_d?CDoR@D^1*#kxX%K76j6v(F|#R^9{kGPfBH+m?Z+C%U|?y|J6w9n>#yrwX~n82i{{~uNXZxy0mG1TeI$M4-dzve{!BDwE3lbn8?LzM-5>oYjS^eeR<haiLe3H>uT4p##>z@X-}S<F1Z+}DDixRz6*EetUPzQwz2U&9&kwTW@@#S<ps=#Sb5UvHiNx4)e{Zv<F+>W_vUsu^OiA!r>L;hEGoV=%xL6bS_6nVyx}g9G*gzZOqvYK@0bJs!w?`w(#@aak_HAGL^WXYCKQ_tiHea{y`qy8XELNdh-Tb?$q@H0(6H2s}Y<q0~17G^y*mD!Zt2X@1dw%<hmtR*V_AY?mQG35S0HKP~6LC_So~nKM-#-4?_kTDY8MS49(e>-Edd-%&8atMpJfP;J8>BFZr8KdxzVp%j4}I$ijK!Y#M}Om&-|)7dW;f$lEYht{!8oFg$#LUzYGcac6T_9Efvnyb9U1MZRP)?>)uG`<6d7gGG}jO(E4&{k5u`+JddfHI!Id4D5>OTvB2$i|YNhG&{7+{}C_&u#lsMncGevDtWRu=rJxlC_f+;P**QQ*(-Z6D8a%q#k-l$v}Ju&vso%ek3ul{Cg{P?0(1DCvP!^+E-aGw+BjhqS)%oBq=;EAj?aXy(p{k2^We0A$&s&D$`x4rQf-`YFW=Ow2Q`(UeDSil}RR1;fyZtJf1|Ha=u_LXlCVf6*eE`I5n^;a!!(6kDx8o-dwlg-#7AtGckv(=tsd+J|$@16DIX%2q<FTMSze(fCs@~RX7w@%5F1oHK1SDy}&GB~HB$TIPCy?*bv@44gFuN>I1yRTHu(#%26yX@jCuD`B#;ozoAFB)DvoMlCs;wk)#<nnZKBDhyNnG&4Dac}hphABx&B_Ep*-_dlJ6^<Z@Dfjf@EIWg=BxP}YcR2c0l}U{08Cvl4V^93q@BYujJNH=1k_GgZcm7Cu4YE9ir`RV7_>)5-kXq7^Qm#r0qm1gr-o~R}c<71mZtq>Y?!W!<?_c-I8$}!&J2E;JMG-T5=aRlsWTVMLBY*M>zxl*B?x`%|t6p~Lh1YM27gEDDNTQ(h66Dm_f<j#6NC?GTn%tXx@6M-o-n%>V_P_q(&;8tQyfc+dRIP%cr%>7m>}r#~KFtW&of_L{*Y+Ks{n#fC@7}j->$ACYp{b*)I`7jojpM|tf8pzX=uL0?>E)|dMwOBiiQ4;GwvSJQJe$Ro1SMe)*h(p?mVaQF5=zi)Yyxcn3>+F=v2wK(CzUQRWo^>c>+LOs2v8;hKk?X8fA=SUHnDHt@XCb?HVtgLX62F%y&z{@te`B)6k_D0NqQQ}{L}zoFe@odM^ThcRUW&2`(s~yJn!rM!@v8xo&`f&?|tCbk9{&O#m3s{>DootTy@P$Uh<u<-|>}?e{xZO^%ZZwe#M0Y4IUR4u_WMB0ferWE#-S&qMX#K8bi5K%5k|qQvSkUeW|`Tubbp&-u2Em{M=8~eQJcBk15GFYHoUp!D1+i<J&%a%ZLB*{k72vVj5gBeEyY}nZC*muY7r2sT|(BZ~J3UZvEaPN1ofCP1j8vUH{6L|K_`YKkBVEJxa|DXpK)qE^kauP$5v8l2X|#O8vbQ*`mDVKaVNfMj_<2Nmoy8h@dw;e3aOzry^jS1N2eo+(FJaCdMOZlidMkc>UAg`Gc(wK9tvM)g|$d{?ZTiuZvTysS8N~A+{s{PKx@|3gI^wKQNF&!8S3;(QTuj|L41Gt>5Q<YI3x<H?H(Yo~4n=<Y=RmS7M6to{3lf?DcD3uq^X+g_6!}NptX187Qr-CqN;diOA|`{=gTWe&X)kac|!rz5gG#Tyu$U2&)C1ROBm@W?4Qq8Cye@_`~n}*IPgG$=dkX(#`AM_$xnm!L?VcTC)nF?=gkdliKw3onOE6YajmHo(G<wJYReHMeq2--`Q~C1<v`zk%BWrR@*Zdd}DHgGBKe-un3k=R4#Klk#3=tcZDedCCS}%T{DN4$3d0jDDJCzP>@4sM}aA=!Zqr7qZXKw3`6N-|McNoKJp)k>gT^;-PNzSxVkKA@DwSt*i#t<vx!>#Sj>AS9Oo;hch~oheeH91uUxro*~SH{HZAHODtq#2hT}UY?)mcf(uu}3ue#!*mu+Zht$mc%%A6^}PQcBIne1fGr~mP52cA5!<%KW&%Mbp8BUQDhZo!bVMyWftWA~l6ef7&9`Q%tuyZJ3|_>s5&<k|~1O4bM%S7>($5u!NBYyQqped!~A`;SKs96JB1%l`b|-fzn#>j0h0l!83Vr)nf2IT8e@k}Z{@YT0)Q^}K5l9afi4Od&5KbqKLXXlbxd*`Dq34a_hl<@KpNtpj9;Ao`*A{p%M#`blfE)mJWl?b~m5b|TYE2`q;7wAyDBS=mrk3IB<xH8$WPF|m+W)mW=}DmF13i_?Zju28^~5a*NPQz{Q84Vv<q5Gc=cBFgjJ7{g4=97QqcG;&bd<|RbRS;FOg50BjbPv3E_{Num;b8q_fpKYXKbp}wR<2QhUGAkvAzyIw&`08gqU+Sy=m!JR1pMBS_8B0FP+Mm){%;T9$apmzl?)iha{i>g;zww>F{FYz+MVIER?3lQ{z?B4fo=#4&V1_9Lu(s6SCueYvr=o7*Q<8Y`-rHF+fyg;$;x1f8RV8<!m^wE0%U}G`7eD&Rz9D+a8(z5T@}&(kp_-FgmH-7Irvv96Dp!slJ(6cxz|vJ!B4e!$@L~fC20dv;bySd%r`)nyE>sapIi()rs!dU!oR}CrI$}7WEQb{7A}4OilBK0;^|Zm417v!npj>NfE?s=_E7m`B>-Nun;KQ4*y5yp(uhxA21UUtSv}B?$e&l0!f9>m~1^w^(hd+Da%`eS0N9IqBlTGUD`P4-(e!&$lz5d?M-uCFd-~I7-{Jb)$pC@C;``HacK}ByGGTmXPE_H`cb$Q;x18Tkr0N$O%LwF`c1QD;^vm&w4Q;$FK!S}x35?^@T=JRe??MrotutY3zXybL7XLrcNt~cslJsD0)Nm4GAdn#;<_#i_KhYpTV<E?=QX8}TiC{q}(){zsq#Fk5?a=BXV>FXUB99+C~$-vOSz~De{UtbhQXS4tcWxxota2*rZy!PVtTb4~79l7IkxADnUa|P6JZDiv1Pk+8vuf6njKXmQOU+l#}#2NTgYEM>_Ma9zfuX?%0cHgr*9(~}!korBVE32x8{P2!t1gVI4->q`2?#M7eeePP>z|!X9Hpa|tF?iZUO^ZRj<N_gv7ys%1_(V1_-Mg@~`Gp&&{j~8`VT1(aieH_c3ahHt+GQ(N0bph#Qi8Iw0|_HCUUPz2V@Z`&yh7DNqhJXUIl~ntubL(0p2f>5#VM@-P-(l$nOLC&7$Ip^DrP3uo`G`7M9)0&RDF6ZPAVsZnY7k^_+LJ->+z?~yZVy1{g3}fEb9H7Bx+zz<VK0CC(7OWEgOfI505-|_)8!C*yUGWnX|BVC?2XRekSjt)un}q44*OJ<H@L7eRQbU)H%~K+?~`BCN8qDjIBfoXa4+4*A6T#XPkN#PiGGY8v0r^6Ar+Rn3RkY&BQos?d0y-p(jTgb>+BhB1>_K*hO)<lqci6ChGfa)EF{k3Uxqq7M<aANWh-d8SjlRq4&_^6T7z^&X}*b@mgCg&8<c#e#YeL>67<A7)9nMfBhYm1$}4G>rDYdE`Hg@wdY-Zg%dwMKAyXLZu~5i8O*vVD&9Xua`2f^7bInvr?ob1q;u7I@4Y?e9xe(PYl=pgMC&$gxYyjVXUFa<>sw4u3?e0=*<I<+h6qF;g$JooDxq)t_x9cOk?*GC)W2$I)rE^zZdg$6k03O1=*aGe4(xmOuwk?El7%n-@vFE@a^~^<IV41xvS-)|mB)6~zVeapOdijpa`{Csx!zjiv-w#qijzA(^VuDbKiR)*;mQj(IG3Hlau5Q%EX8Ki<rjVHQ(qn%8%@)+RIapyUo#<tjkTJ~Y@t|yxP&a`b6te)fu?%*eJb$=Lgt!R5e8DpuYKtapZ(aUruR=j{MBbJebsp;_Bk~=9ld8sMcxC0g)6py_ajH|`p`pml-Bhxp4xk2_wEx<u#qTY0QE)!yD*6%yzAZr-x)|={HDvZJUjP0C8d}v`2>IGD^G5_Z%<<qF~{n%&wTL18!k96imG$f0U~PDYPWp&KjPT_{2#t+;p!!}p37;ss48*=6%bv&VPhP}S(>@rQH5sN14YGY=TaA?U9<3g&w(tU?Qoik8Lg<9MP2-_xMtz*Y1RG|l|rWZp+LF#t`gwVG)hWn%KUa@>{-Z}^H9?hAM)YCX(C>huUh%KpZW36{`1Gb{iR2a9Xs*LAG@9ha^#NG0OVPP#B^kwo_ej6(aK*SC{pW7w*1_~hranA4@4*QvL%Dpp1%Z*o{?I%`@~e{;9cIos5)3J^$!d@wRdD>e`E4ktS%;#!#jl$w(OOltz<I=iZ~Z}3J7l+VhU`O1U}#|0i4+Cp{I^N_weyY@7QAzSBFZGHRC5nzxUN|e)hso{KT*PqOUg)s@IERd?a!Fz&GyM^W@W)zvSAN{O~JNm)kRWLYrOxKtO%ErcU70XO4<O`><h3AXAh<7D{Oowul6hWoaC@I^hLAYRh$}whz!OPAI-aGrR!>$of2EHs1RvvLKe3<{8aPHb<d?F$0KTsQLC$97BYlKFw5oK7;!RFe?xlHVT0j80O3&Jv3Op3dB)_&~Z`=FeE5Mm5IojJkKR}r6|tREI{sy_?q``_=z`dxnRrx{=N4+ci+L!j@|mIx4*1sIL`7+l}Xv^+&+OP<x3@oaCoFVX=JsZ`wu)l_T>-Xt4HJoO9yXSzoMMh7+6%TZ0hR?Y9kRxl6!_5s%|@?2OisV>;FD_?N40Sx4Oi>4ws2xAoPzQQYH->D$S>r2^zdt9-<6lPEgU*?0W3LH$Qf-KWZWyYZV(V+XR(o9%<kNefRdeUiXtfUMiKudlDrI-N;Ct|I)`l?HbwYOV5LW%`{-`o+eY05}-mtkiLO|N>Uj)a(vH@-3ym4cFq}UdPWJ7JLH~-wM~2lj<HNFaI4~pP(iag7C>OFpptSEj5TDp6eS)SuqI&h$!R7MRnJUBU?xH+O7za#$O0tZ+sHyehE;<1M~dgGk*X>a<#`_9owV7{LPZoxOpU22@j<346Nl4B(G;_h4NNJm3SCtRU4o6toP$Va^8)G);-Rd>%#DdD1|pP?KQn#%`|i2)Rhw2^yjbGYIL|)vr>%CYvSUvWAvJ6#k7iHZwda{{@7GDXVA;TnS1;~ysla<;5{3A}93@HBM3QdmGcRAi{H`5`4n1D`;>g{vdegOi%S>fS)w7q-@ha4>D*^%qfwiz8lnKU=f@3O=?5*8@_xHvRP9NHS47s(XXwkaG!|RsBJtYI)aM9+c?tSXO(>wn5UBCZZfAQ|rWhN67*<5@Q$4@@^==S>`sw^6O#cO}adv~fw@RZDH$UO4h2W$1|z9kD64D{8<Ch{zcjU{FR*qFT02$g8fr2`1!m6%CXrt54BRGCOs8;z6*Nx2NsEK5NYIzQXUsHn>wGi6y$K$OIJnxV;f)~be4;Jp%brX>RykgQOWoOd%HgiPolIP<&^{ULj`2`AK20aVpz8He_OM36Qw7ZFG`FOa3$k6Q-Rd-2{9fgmm~fD#EzRF0FcfAQ82{oj9@oS0m@aqYzD#L?|1ZrkylD_?oh<*z!A2QqJRxYJdanNpBrvSq5~Be?T@-`Txqy4Tx_dhnX{3kRGtAu0gkc91QFuz^UFXBRH)8|)prb=#iZhbKP&zHjyoREIY#UUA-%N^dm0yeFxGE5=94P!{rDnIWPqmHLG2-+!E@+|k`T_HI3LeD8!oVxpcUYZvz|?H^b+n8P`EFRpJ<|FVtC4?ny2@$cNX?UBbfU39(|?;D;NhRr><-%&d;@}s}?E2}oG7nir%OP($>h8rTNYHec5d$(-)(j^NQO1*9r-ubpKsfhQXb;iu`9rjzetqElFSVcBD8IJ$p+w*{HqD6;c706siyJp+;bvNszo_Fr8tJ2J`05Efiu+8^Fn%T*Y&pWh@laPjcRt*@zh@<H4uif#lfA#lST0if~EyHV<xYQrqd0_9;J083J=^YPkzwpM57u>MX^pXTL<x>j{f`N&+luh7?2lhYlogL$QrdAnTyL!Q;3#z@&i4vGxfJ8z^M{`yYvMDTizdH7B-n{6peY#^juN`XaI<#}=eY?m~r9Y|kmHLPKdKQ)Ys+Iag?eP9%m1@N~mp5eM*yQN(2@(rOOqNUW@ao0=i--D`4tV1mE;ABb*gi+L`n;9(@rmOHj=%TM{_=PJ_>Y#ZUg>;rNT`EEJ(U|@`zjdLTp1*1;vA+{`z<d=4;-X`mFj(DjHpOEs7;{^7DH=Mr~xR<$zw)T$e-2#sx6~rJ~{*Idsb55DUQbuks6eS_AhsibBZ2yEqx{E!V*zTeD{~W@=t&Jk1D!i%i4vj7pIybrX`z}*{VIZ`^ePM@%umd<emo(SJzZ7dEvziSN54WgAq^S)p-Sxg>Nt!!(|mC-lvmp_Y;S=-oJO()<YG~=k>)`E+5{qaDcMRsbRoV(JowPFJw@>394{z$jWQiu9$Fk|Mc|Mqeq_`%krFS$K1rx=|ejvmDNM6PYsnVPaE+fLaYP5{n}eLNnEa!`WN*NEE@1EIdXV3yUJ<M`kax~7jKxDp5C){+kJQ6^M<#-g{GY_HL`5q&fT2Ehz&Fpsw<tgLJ2?!kw6R|I&^5ylg}{og5^u1QsVPmxP3n{%R+5^R=8wm^Tf>8W&-7Hr|8M(%v?gJ5Nfk5=ytw5Yd;NP#>^uihWY6G|Ltp^{v45>ch$uMD+hCNA=N{f7Oz^qc*)X{gC`E`+IM*0l-o7>+`~uv7gv_79;)<JbDv#!+4^dKG&(Uhw0!8q@yXF$qkA7eSRbuTOy<WAO~7MaHNJZBf-Q>{_OjY~LjV-O*u@h#FHm5JV|cPqZ^aL?_77Ax46Q#rUC$NAC#O=-=v3|Kcw?})H=%4=&9;dtGguj3zBr?N+3MvciCfMMFCx%ZI8j?c0VM&FzVgE5i?Xr$onO55hMQlyXvwfM^yIw{?s)9U#pkad7#<XHP321Go$b67jvxl*d7jtm3SF{%nF-+ZjP{)Qd6_BjsS?c&>9h$LLJJTp>?daam^C!bWy+4i%#L5Oc1-GY(v*tsXgC!+pDIxRMa=_%a;fyee|Z0GANwpvy6(dDL#qaJX-iE|&5@F&!8Hr}Rt!#$)yDRX9@)KjY)9?*j#_XJY`t@L(i=_ICfBW9ePsWUsnLcytFTq?FYF&&SmpB<l{WQOysJ~ta?kW>QmaKwD6b%0AA2IEa-V=2i~H-&3{Yf|A0+I5^l2WbuH3S!L3s`lFQm=7IzAOEdDY?NOOEY1c<j)@zxtg&`klXf&*1RFd%t?8Z!|8r;(|&~DS+<-c>Z2%oeS+5Hi~yV^2G6@$Ewxp3$DIeyciV7i%lSdHbrdK07a;$&@K!6p?wC5&Vmpsbj;?*O&D@OVX4`f0f4q3&)R?A{HHI5YF<%`uW2*NG*_WiRS{wC*x)&#s~Kk}<}gA)QmiDU?|ti@JHB+Qs$aZj<&t&FGf6waH35*4=9-hGp5bcmf}Vk8efdaj@6)>njak&wGcq;Vn3f*jziaeZ*<y86UNl%vVmr`hF6kLuL?(yJodc<|aiQ*wgynSimQ|G?P@@WHPKK0%#cfG?*;tn`Ib&^^?C8j3)~F$YQPLLfMdyOgB~f4QD_?lkMOz<yYUfkW-tnc|-uTv^I&}DGxwmrY*#576?z69c!|OZ;1eMdAH2@d^8#8|B=!0MVMg%hD#Fk<QL4hdAg@Zh}aZU~vECqUAE0#np?g));iHaR23cUgZXo6W#>+9(7=dm$L#04N=Xr&_|E-c=M)|1ReRPromC!vE&6vwI}S<xtE_BpO<B1>#qp;!|-=pf8gL1d#S=p^k`KB~&rz#0{Q?C_C~|Jw)0$3_O1FI=>GY3e;UZ*NBGt3l|Us0uHh(6?-8`~CxwYuvbQ?M1_tseGX3rQ!L=<kVobyu4DXFoO)K+C0rU_hchU6i$l+B%cAwcs?Qk@F71}1Hfn#x<E<8A(I*cu~$}#8XmbQ!?1MpNx`XjG6X<<&!Yagx187YvmgBEs`cx}>Qkn-T&X5c-h1ES0|#F8>Q`<)?|gVs|NQv?L}aW5%#nlpKKg&&|KRO+#bn~X>Y~*vO{GM+_uh+0C`$rhp!Lbn(xKC0RgFs}#Ig5cZGa>oRZ1HT07<#5-sO23;8v}*Y~qmX$jn)q8bc;BX(J8t(o(5nts!C&Z>-g@+s!LRbNP&jRZXH0RaGzE*oc_2iBUro5$Dc@4nL}@Oi^zoE>{)CHnS6mU{qB@7N%FIwNY@`w-OkNhlj`;N`Qa--9Op&(33r@hkxx)|7hp#?S~KU8#{W$0Fkj!6(Y}|nZOAEVx#q=M<))BE-lBK7gpjt8z35pEr1P`K@vqspoBvxTMii&q5TB;!Z&={o)rZ^&Gz3jzK-x2DGWo6s57<%ldx07J~v!OQ%N~3Q<;=Nl#yR^!MZ(eM}2hqV}JYp6C)@3hI=Aoyvq-4+y40@M^>)i@T%9ocG2>s;+^-RBB5(T;l>FDHL)c$>h&k@f3!Y1{m4TPoY=eH3QxKGrdPaT(Xthp%QdD5h`j^}M?~s!wU$MVQs^K=P$+u?ierjPp*d%G9GR#bMZrr*ku8-<#nuLlOExBoL5QO$oTa6x6qG%iR4RcNjJ0i|c}84e7Ls`pKq584xo8zosEuRqL<NzJ1PW#XJd}(PA`R_$m=F|+LPt=tmH;1ADQd-%3MuFbQIdS=L;rE#op)D;7yQbf{=sE0zy5N5(e(J(bGvpvc-MD!KeN4LA_8%1C7RQxnrwY+r*HTx)+|kocfoI6#G5*fWMM^9^=`JGIejCcePL!?cbH$`sfr{~GEgbG(dp4+BTM=hNGl9-8bp9XJ*0PdVD$wXp1JRd;|C85X{EPEh(R_na8tEy4}EXq=#h(F@Pgq*!^>8!>>cO>piJU@BTb_yQirV8IJ9ry*S`GaqX!N^5J&NegGaO6RfYy$^zxUg7Uy+PVzhZbWY}1v>D)x)pn(*sXWQG&Q=sLyEEc=D&Kf+1A)L-31<HyRoy6n}%(Y^Ln*#^#FEqopXkqgU+VTU;QCM4RJ#X&<%f}Av|I)vF$mQvR3og9srt1YBPAk2=7hiGZ>eXxa?%e&ATfR6wGG>U$P!LL_FosX;J<>RlZtm~DV&NdUsqXf{I13VDB@Y6__ZljD;hB=Z(@p4U`V%Gfd3AVTXvOg8b4QqX!QcV`E5OhQh^-kvu>a0aA0%t41O1DaFZHTD)#}vL)QJ-(DwPTZ)00!7U47XYH5|iA&F7iF>A$?{f-5h}8!3aRi3~N1m^!_B1^=?*ES}{#w}^I~vRxX^(F>n<FlLsvCO$zWB_d{S`K3-hPWz|f-;pt2`SfRxJ+}|l`1No5$+#4`v=M6ZCC_?#`!BlkiX|&oK6KCh58ZQLR-dxgkis(MQ}ySz?^$H{r7MTZ$eh^I@fCbOiJ>GcfHGvwqJ@th9-Eq&7^a0Ff0~DP)5#-Lv{%CF&FdzPkGZMF(L+a8E$(y3P*@_wY|61!ARV9BIXX%JHyhnG^tcd#*pNnsNtKxP?|5$f@F>V4v7nYpq3xCYZD|v;s6ca`l|6d;Tr}&WP)$DbIy+Jzgga+PeN@jN)wGk?@aVDQ-~QSi-n;8wb<+(uzbwmBAyrZV36ZGg-VZEV_{tyoudjd0k1trf*oDS}PIf=DtC42sE$rLe!w%Vhx|l?e;UExLBvLU1SI;1=Gi3ILg_FmNq`7Nkxf6+!M2KJwvz6TEX^N6vv}!2`BZrPPCTfON$a#V%<Jbg$wIM1Qn;2`8*hCQwlQqV$;oyBzVI@#HS@Wq|ykgmp{?uE1mKOl`gjv1^0yq@uw!cYGsP9%SBVf<EQlXtlHTRCFGxJ`-h9hgyx;14q8)=?=FfOW0N%QI2)Uh#Cl9&9*t4(6Go&h9H{}&-(ud9P>zWAawn=iQg8@Jtm`|Z=mYDf2v^$FJZmYf30gbtYQQ{z>9f2i44G;~c!8+pvx=w$uqc(S;+sIyRlKonj8f{h~(SNr=fxcqW!qXi3wR<2%Mo0^WS@!pS&jE)>VIx#-6_M!{!{P5?;cOBaG)Sk`PY*Zy`f)8u+W}CO&b`X&#kidde$=4=plZTHtB)$4IFB@LIJWsRW)}g|^HA5Qu(as#-3{@dv6SGaa0=b4RijX*p(?;IGZH1deT5SQ&gp`flwSC9r=ve<?|EBZL^DaL{c*=`6iFw7Veke}q-~Rl)QR=Q<y=cRtLCvSTSMt#X3Qn|53m2^zn|yL~qS2@iNN-Iv6R}CsKeV7+tu9-!a`CdIOIIw9tSR^O^$!ezAR<s*w0IbzU|O+$EdUP~6J_I#&;7#(rjL!*My7j*dUEy8tJ)Ru3{of}jt}hFRiA7uT)F(ey!j2exKpTxM2Mou&B=ZbH6Yze^X(E-Hrw!a1aA~7aux`H079sF$Ft8$nyp;Bre|oNz(YLAYALC}6P2ER<e8CuM^+eIvaq-88lq=lM*KgZplX*~)&ns_Q}srg=MqQj&)ayz%U-r@^(r<tE+q=}p+$&l=4P_lix9jP2dgJoCqMOT@7VV6lTY4t|G{nhw!Gj1$4)_{d<xVQ0xMKVEZO>4ZDjv(Q5smjY{80UUc5OuPpcMPyl1~3(iG3#&H>Ohrc^YuA))Q8L&RrSIHvI4Z++|u7E}lNZ8=fN`Q(ow0g<r>cJBZBEw}cPT(oN0qB!O(6T{jBHu}LKVJVf$l+`PJ3szrt`T3V#eDUR%8)Ll}g}TfYDn5WYi7x?_(}XY#!-$$n<-F^zeDbdQr;klejZ7rNWhc+WAEcowM-B1Bv5CCya?p!zez{3v)SthiW41;KFca}9_UFu~Tapsi8W+;@JKk<FXq)^zCAC=E+Gxe{6^{d>qoXc&Y)&O|3FPzqGaveBIzBO=>587jgv?sy({7UU|A-XugrOucY}Ca+@-sgj$JRS9&J_XUA|t8bzjmd+wYs5nf+U2T{Ho3CHHjpbtdW&a1q5@9&N<T{W;7=22X^hxy<T|DRj+y7e|1@AR8E20NCaby)6SM9N)*!F&S_z0sB2&Zm=k(JGxn{;u|v;`MT_QVL=fl3Mn(|wi=BW-I*qc94I|1M`9pVptK|J9E0?b+B`VHy5vf1z@b&*ABEgpa-nb+u_8zU*>MFuT>{kJ8xj|Yfw6lC8N)U!GUg})^`WIh+$#qw!d3yZV2x({$cB&X-=#gl}9@w@g8=D?jHvH@F{+~%-RYgt%dZqmf3RMD2E_AkTmbug=rX&*Iiqv#|a;75z02D~`?C9Ym78I8f8%H!Jfrhn}<_Iu<`?haQ9vN9ke8KR-3Y|7e%6|rVQftsderj@L|MorR+|W)GU~6*k4AJP(V~wer1)Um8$rCZz>7x@P`;Uq9>o2=_`NnmrbM46#^IuDw*7q!;ZZ^s75_Ve%j22BOTkiryauPU)lMV#{5NN4dx#-Hv9rW;X`w#AZj_1_6YtxHnj5&Vz*gyT*-^p}s{lLJIBqqt{4EzH`9$GQHX`p}l#IbvBy_47i^98g{kAm0B#F2>h_V%^)x;rTm5Q`nzdpvJQ-?AnD^~c|od(U7NJ~b3sDB_xXPzRT4x7e~<$2XjF&9u9YPv$iIIgP;xAaW`fUVCM<sDFI_;amRY!zPYr-L&J-v<A#}_cPo4$atc<uu_gix`9jZeI!yO-krB_L0@EdKlD^>VzRwg*BOmNMdCqp(dC!r;-hkc$asQ3<)TN#$MzmNzW<oUrC)sa?_GY~waC@@&;;>RYbT;%qdTV2oJ_Z<8>kXZcrj{bYs`SA>g=4y)1V@LEsgw|7ry9%7hK6okKFN{-CK8P5(y~_OwbfaS=9lm^vGS`m0DxVP<6}V0d)fX&ky08g2F=eTGI=C=6jDncHhG$P72#ZPX*6Di^6KKawALk?%YAff(=5_*enyd09{u=E%U^&v0YDYOVjj{>#x4%WiQU_^=8ueDS`gm5-zl5b%nsDo(f|4OsRW@&ivUiddf`d`Nsl4N~{FIYku_gD8<M29sbU(cg7TfSh%Q)Vo`=has1%7@B8Y1e70)smPP$TRze12H}2~DMM7{uf1GSuynw~s@^2rT9+?o!{tOqZ*|dnf_@jpo5mBjJE<TyH4~10^1sUS;L!;c#hD$eIy2V->lEFawyk=;)+)OSwLUL4yeRoZ%>>9vTYieDzFr0T6Uw!48%PugHz2*J?{@5M&#z~LFQO?X7Qu>&Qzx|av(#h!s2@fPOG(f@sAlo?zZLF&zm#<tgSf)q6anEg^{E~@E!b-?be+gMhiHX_QvwFQjB+RNL!n2QWEgAxFL~(7rF?#Tr_kP*N^&7WbkjrT#1Gi>gq+WEet~T$gThuM<yGSaS8*_2apSAx=MJm13U;e}2jTZK$W0QaXJMaFR-~5B!k3XA4iGxC*%=O9op2wdl!(6^@)#AP?yvOrD?*GZeLY`GMTW0v;1^s<aKK;IbKlsev#FS303(g`^cqU_$J3sxU-A_DS?Jf5X_6n4AzP2Mu5!rO2vF(v(rYGw0(uM#1FW+<Ri*Lv?ce?ykcu{Bj{(>Rly(gZhB<3urJ4_k;k@I?~&qZjlBG0mQmu&g<cmMu^WlKl)9Q^tRKJ}+>f9H2^|7O(NM@d4~9zS&S=+1o!u}qCbk`n|_<+Dcy{C_}J;8-*3N_qYAMZ+tH`Wpw2{p0VxCmYM6O7#rtYluuKnK(9b$0u&7I9jw~N&lh&5zk7qdP%X;|JU4mMq74V=Ycy^opZy>?{yAnG;#(A5QG2%q(qvc#3WMiP#(*oElV6q8hfNMZO+i1rDc1TZ0UzAEsr(w3}r~NDJoc^NLmyriUDE(iHt@LozdvrFWzuYRqZ`L>YSUq(f!_~2YcPsec!$JRMn~4r)tM<8z61_=O2H%abkIDe*T~ThhM+y&9{Yi7LyGws<#-sBt-yjKdnPgJ1>n*_KHq!?6>*?Vv?pCh=@Z}@{Ro7A9?q`{+-{R-@Uy;bneix2Y&6}|M~CymxmvG$hF-ok3YAz)|{!}O`B#pK#{xj#+E5Pi4i1W2eP$l@7goJ$><B;e&T=osgM2jpMG9)B_cr;0PT-0j1*(i45CSDpZ$-Y{>1%1bNu-O=|pvA=Ugs6R_yD55hyBxC~0td<f&KO*;cUhbHDu0ZhX_NA!}<XZC(r&c~oWWIBMaWP!wcjn-qXh8>aC9@gu0un)zBY2Ge%5Z#9%oPmG~t31DLEpZ)Id{l#bg@YKPhtms6<@;&$e=<>l+FFf+d+qccW@3O7p+#CAX9z_TMlzj8_*}pz?Y)!b$`al25C*SwsA2T(hL8Odw=@KCrV@$fXxcs>X{_r!u@&8~mH>ufv_0C<_U*>!tAY(M58P$~2*Y>}*|A`lKuW$SD_k8?Uepxl9UPT+w#U3mO;+hR<WgKG&i|jwom8z*v#iw8lb26^#5E%0I${Gdf<OU-^08OSR&?FnL4#9vSYb~ET^@Tt9lgGdF-IK?T({jF&gp?~4$^OpOyRVz71R0yB>%SYJf)#3{_{!qSlPA`mTWUi>+poXkuJ^t3zW2X-e)D{_ng9T(0udm#*BWP!p8DG7zx?Qf554%v6A9D8w)t&W?W%5`*3c)BMh%>SA@{A*s|TMybb4{|y+8RAAN}M%V}>%s^ir8JfOpyQT9+wR6$NZ!C#J`x>x`|qlel)i(um2GosuOUlxk^OtLp~L*@8fT6r{bnLJ+J?R@c^!z4qFl|JDP~KK+ba^A*hg{<XVzS8cc?aPc<`34)bSMRO9;FTZ;Hg|ka5nR94nXJ&4@_bu=I$cK&`IJkYsj$^MKYc*Q?zW4b4$M&_3pGgF1BH4b;Wm~V<E-8Bz>hY~2f~XL10`|E_o?Je@lsTQ*yY1iqmj|X7HhJ%gNZ^ZR$`ZFMxMssQGt;wEDg=*|OwJf<-YCa601#oju`KP}NZ;`t2+Ty)B$aj4`|eQODb@LGb%jv@fB-GCWBK%NKkyfy`jd$YeB`=4yNyb3k+0GaFv=wG2BN6C=0-_16$&QV-)KE|{LI0%)`_f@D;QJHe4ZqU%W_sW%EXe??d<l2nQe2^Tc&e#s>EUerAMt)gUG@Mo_Xcu!DH=)-+SAwzw~ea#pTyt8FGQHPWt*xS;(D;3V<5gE6e01mMGS8rwqi&)GYO@OzWO^gCH@w9b<XRvYlcmgXtq!M)Vb7X%SFR0f|shC06(V6@X|UFl-b%X?R5}TNw(3h1?vur%X)l{7B18NkmkG$bf}S4V@2Y(%bL4=L`S&vmt97$@1N`3CbD>5`YyMLF3L5`r~V$43+KB|GzOr@$QYF0(ww#+0_+u#ok?u0xv9{J+jnTZbK`PhR?*Z1XG=x^pmjTn#-nUr!@pGfsjEFK~OLdDhh#GG}&5y@Y$EozIrC0edkZzfB(;ZWY?bES=Nq*?&#QzNT_ADS!Yn)9Rv{yBvTbYG^$J_C<?#|9u)vs2(1CuqU>s?9YTS^14PgVG}LEH?gTfMyR4CR9%J;4G0aRo@Vx>`Ol5i;qG(izB?JTr-it_*B!Gyh1~3mnL={k^Nb@FZQGf(gM1lY)5~;*oa)>!)X{DkCx~LTXN(EJk*-b9bo%fYAWoAJNArB%%#LN^tF$AM|j!zwatroWJnV+hMydvU38y2h(7aUi3I67I~Zzw9_CIJ925M&gR5H>4qnw!Zs&9p!@hh<Fmtu-Ec>A+-d?z%g!Z<F`lkrsA%000orK@p7_R&(~%Q%7Dn(q3L`=lNTI<Zu1bCqIt0ifd=4*iaP91co@@eP$@tQd|@fWkxLBK?Gpf<j!|ZeNl2{W<&|nO)EnbDWOjhK?MuLNGA~+undhL#NIkAxc2PRkq?Ln0Ff8~L<A9o1~Lqw62V)d3WE^5S1CB1nd1&8>hpGnJ+WtssESFNGLfnlwKht4^>V+|n88y3NtPEYC=nB(_W@MdurW4kH(Z`$5$a4zKH<vWeC5Fhe)G4obLS?l*_I~vU47+@=Cdi=kb|hA1_Z$v{GuFp^?sgs!$n(yfQlk`1_nqlIn>M_e)aUpfUh;0)4R7^b^EnBI4W=>3*J!Bz}}+KCLDO~z?oyGwG}33r*3=eoqy+}ADQ2^1Hc6Di{#Q0(>blABI1J=jY|wf#ALkpDjFn+2;0JP!p!15spfeeql^WF5I_kN!)Yoa5#1#&Zk}hVP^nZ@CC`1_o|!4)y5xDr%z2&@VM4~`E+R@J0ydw08lZco_IfZidRMjkZ6^YE1Zi+3CNC86)d)aUo4^2k#d;UZxlAN<!G=H)adL9{@rNG%jbHt>GsjL$qupc^${M#{wdcm^$r_`@5VWnx8W0gMMBJ*rcHdA;iKqmq$_f_1E@t_|r%vr#Id?h;Dgo*BcilX>bvmf$&_S;(yu6Hb?zJ<=Up}^UX2l1+;r3g8_7{I)*WSyr&_*O8+W|Yl5*G~tMI|PP7HB9$Sez?eaVqX-F$+gUB08=DkOn|iARuOAi@1eyfd=sYwA6nQqS&UTpavZ8qeNcA#&b{iO-c__mS`FUNk=$SfPM!p0-%K4^+hoTL`F{8Dr`jgE{G8GJd+T5?irQPSW1)R?8#GK{cnHu=b!nnjdLrhWy`v`T3s+^&-BznHBr~xJU>%WtRixV`K$%BD2h6Y(_hS)U}sCm?hyr`2vpV%j;l7JlvR(sEEsjJ;iplx96dl}rr0Jaant!_?-zqUdE~V<PS3QmwJZPtSIzDlE~`vbYtvJ~2p||CErc_)Xk05h`uyRu$4=+1tWuk}>GoTH`s2SavoP0ojscRg3TkKSx{9C{z%`xm7dKw6b$PZGKk&haAd$xqG-?&h#u^)s<oGXY2h>xs?67~TwExd8Cc_|84$SZcHn^b;MqF8*v6q;LjU9{r>%Eg9OC%yPvrQ7i_QhwO{oXgfbLhoao_gfbtd%oBf>bdUFichL0`tzv+H}RvPt@kqib`<m>cB}nwp1AuMS?m-0wfev)lh;60K|pRm`SJzEQrv%xS>!E0kHtcDN!Xl3r#4X76254*ptac&gSivcE0A|M5A?VW%XRHfv6e0LqO)~smc0mZEEw>+|GFw)KD;vs77>r2zca$LyJdG`L%Y-WqWVD=7WFl!*{*)Zc*$aK_D8FP|qILyB-%fD+YK#QANd-yHAlwB*2J<8MqI`kI%2uUl<koLQHunq|W6q+5@WAruaHx_OC;T=)D&S!*z{R)fhv}N@UnrV||`~_uCJB=W7pE)AXemUOcq_0OrC03?UH^V}fD(<aCy`+9BUEF?HqU`PId<6V+O3%|wzenAC}P-X(@7tEqv&DpmuB;0-%M5(QDhLTyDV_Lb7%j!}L^RRs#fqNs!l>I56P%SAL7Wpg@jA6Z^J-D;f6shNud$O)9m0-%A(x#>;YHm4J{%FF~OMnOacP@yQ!fP|EwZJu5}`1Fgbi)(G?XSQs*_U0RY;v;`|_m!75+ZpyFbz3rQiZIhlLJIGbc2shgcYvRIbBUP9m}KDE^DgKGpNiLE%6_S!IQK{Org@%?Y=MZ(>+O`I(XIN)Ij<T3bO4%ARg)w^L?bZ*Q<czKi--icy1M$r<BzYMTYCP<eFtCKf9lBbL@2|c-UE;)Oo0GYG#ZZ75Y>!z5S+^r%bO?a(}XqV`FeGJqTXz_+wFX^TAiv*ge*4}tu>8C!&>8mEP0>1;C(<O7hGkscKY0M+l96ZlvqJn%koC<+d;g5B05Du24q!NpQv%l0x~@}J+*nB5}KHrKm!3n&{!yyP*6#fgn&`0-Dn+s<>=a}#e8XvY;ya3cmKpke|qO-JKI@1s0V=lpi)dt60x2TP-A(i&UeF^k3CvMFH?r#V@Z^O<pTsZ#*l?xZs|7CXGR1-kYaE}<)~=xq~ci_!Ia%4$3ph(Wr0r00~Nn0z7O8XsBJ7sEF$-*NTort=p-^(4+7x8P@=HyeVh*I-E>veFtahJB_wWHtfmlp5UjO<Fo60-_W%C+|Mm6H{pH?kcZ+wGN;M}wdE^+jDELsRq`A*R@EQaxiz;|!0MHQCc1xIv7X(Y37z19&ATecGMnoY<2B;CD5(!jEgO>7RhzCD086ya3LY5G7z)TJC=3915ZJ$R=fWjrNZ7A|c6g6fiDIppl*Y>X-I<|CX*|%J4rRl_Px@_l<e&_=q`tbh{Nb@`s?<hJEN~Tm5Vq<Iqr3t1eE(3)%C+1P9ND(iIv0_Z<L{DnRNF<?S0D)3i5d=WAX#z^3N)#JM1W=JemW{z2v1S(`B1s6^Gm>b5igJ<(P^NvUFdO8Upa}>NR3nP3f(9RqF@O+x!Z`;)R7FLTG*M6t?AmRRsJ0c)2@(SvG8U0lC5WH`5q6a55TuACQWfchMHQ+bvmxdz&r~F-R)crJIT49lwzW2>RBLrI#s}|3MZ_3ujqxrISsMU}$OToW05ml{ziI1s2r$2Wp}wgm3Jzdl&jRGSvb-`gJCo&E)@u1?t5Tl;z*eKRbn0BlJzH*PIT%|(WDnVLGYb+JAs{%YRHj<(%owhvoVDA=S_BFpSV@VgTB}uRm9$!IHJa60b#iJ_g13{FQzi$`Joe1$a`USBDVtyp9ss-&00;^aaxe@KC@68(b{zcS{jaSYJGa(qXy&1sPHmpQ<Lz(z;Lm(y=Z>wd_8OC|S1Nh40nUl2S3yK(5>Z>Jm}(6PgAdL-W`qy~(EwAWq9E!+H0TgfeClJ?V#qQK!bv4+Wfr;JTov!54jn-$1;C_9Qm^|UL4q+>qw_>HZ|8`RR4O9D`@pJ5XxJcAtXoe+S(X_#%;a(xcWA@4T4HUq2oQ5`B6@_nMnV-OC>>1zs%n!o7U&5furWYj#i=NH5miM{4JZJ{m`c@Ds(=K5rqDYjx(5&-NQjo#fi1aE5r`BpNmCJ@SnJl-P>a~j0%e^jS51?IsFDIo2^nvb#H5vIb&FP9A%d#ieEBW}SzB(T3v~w>C~=Zt0t?fdBuKShtIgKA+?;1|cJrRi5K#_A5D|#NihKIOCnl$-x8HDCv)v%YnVIR;)zxaXYSN_HY*wpP08kCqG7t(=-2I}jIo_gxswxoy5PJ4V1WF))2GpPi1A?julDD!oX!&#Q)n^a2Flft7wh-njH{E&T`+xfH?Y-uPshwL0P<(EwPCzVR*twv@U`17xnTeFhph*;f(*!G3EOZo2fW0Agj>uAZj>VD`Y%Bm^ny@EOn^&C$3QjH7+be5STG&C60KHQRfHq<13Reo4Or#q105Y5u`)jAxFPQ{XD>jXCg-t4v4UDZ;L?t?%WWdZ32PvxBmE;C|B5aHTfU3)LRmIYxkBF!c0P{TON+lj5#aIctjw~`L*vWY8xu0^&FU+~tJMUdltt{Hxqok7OIj1RGTPVp|iou2zAb=`p2O`sZFCuxCVYJmL#J-CNF^#^Y9s!q0R0T9X*@|9`_v{?x6La;7t*dHKnV6nc0R^horsKd-ji{hP34w&YR)fNYLsY3&o6^u+5~_=aR-^6mwy9{P<zca*Ld~VsMx(WMZp~-y$&|0G)n|8ay7!kqe&bzlO*!#So9&h5zk1N@-adc*%_tIr3*KWP{UelqkSxoRB;~}$xO7zms#5i*_w8Ffd}Q|z{tzUUZsM%QjR_IJ5eRYuaOSZmWby2#dw&3OWyFERdJ)aDEH$Q2;TQs_gaL|=XtBj$CxX}rV3E3Bm{ohPDfn_&3n?U4EP~@zB+D}D#Qw$ls)~RG14)k$XP}ePFQH|-ef@XdwzD>>aPMHE<A)iG$^qRgqCcrK(vIPui2#9-u!Q1@HsRjsQtBCAi9@5&<VZl4lS&dG1o7$>iu0s2%aziy0>mt^LbTGsTZ_G?NdgLIUp>)oG*6y7vwHR{w6be9ZMUZS>Z`|BT$ZP>Fh93_W{cjq{XIYW?wN0XFK@2haNV_l>@z1u<@oXazxSEyTW;QT<F%^BWx4j`Uw5_=CNjja)CL23^0mwhx&vSO^5PRuZ+g@1^({3i?MJ0Js0wH`AcY*l(a(Lcarkik`YTd9%hEMicbI{V=~%xni8^9y=e-$9=D67Cuim2;iHtGo^8wWy5i6C7bPT731p)iB_Ff;&0uimXKF<d}M9{QSVIt{Yb_DD-h@i$iJ#4kx2$*MCuf93joY1|t=Z^pe46Di8PCcMu?SWrV?5LZiwh2WMpwZ^uBGnF0?my~cX^AYmd|`fTW#T(8JU4gMl{=^FH{5p9_4mAag6mvKu6o-Y&m4XUpE?nox5Q)wL?^fGzUdRcWM^kV4OwF=6_@8sMhVn;BmyFpkXGtwtQaH&3YsEi2~gmh{`QAg-u{mI+&myslAr>pfCNA!1p%?dxhjLb`6vHwYjtIIdRwc}9!Q&3Rby?MrhZH*5oTaT){(jpH@P%Tv)pUwH6o#^1_=eaO-YxO@ED~ZQB7<DoM{gZU2IXjH)&;vuLisYMI!Xc!$(0S*Puuw5!z&=Tc+>Y?)yS8VGdqGAngmMmww9%OJRO1tmnOAks<&HAX}p<mJ^r2?rW}n+wFJS#+f(W|K6()?dK<-z5KrW+;^W`dg}SB|JR>;>EUO>S*PHI5%T=tpM9=<?)2un?#!0YojLkSebd%0iGA&BU#(eRzy8*9k3D7cY~kK}8!OA<;49uH&9*L|II`=uTd-O?^yp)A_32&rzrV4xwEFP(R=ulTy|eNBYmLLN*fd!^x8{x>+VYk+XN0F8ePVjcrpw>+W2a9nuI>A7=49&1t8A_6R@aKqufl7IswyEM_o2nCI}IitKE1DtB`jZ{fT~ek!@lnU07CGH-5+<4-ku)u{4XeefvTbd2rvo==zZvz5@6u#@>M=4>f1R2PEJpX#wzY3P5Rh>bG=ief})67J8QLDh)UY~g6>NIJ7`D49Vh}|0GVBwQ`DK=JO9n^|Hps+TfhE+pZ&=0TW`4RO>eo8YnvN-*{ye+K5=N<uAQVPDGQ<zXc^l$b>j4sk56B|wRYJ~Znm<|eBM3td~MU_aPZLa&wtTkimNLpzw}pOaj|{o%<(_{^RwUl*8I*LQ_IVTKlOWyORJafz5MJKzi|Ak->TH=D-S)|{_@v3!}hBummm1!GY|gF!gbf0vrC6Q_4_V&J1)E8<ez@_wMV{HnMjtu@vZE^Z(wM;&_yik%vbO}Tp~Wt1!!ylSE0u%-S^F?y=Wa2LKvCt(9J}?(C`3=nyYL3UwVm6VX-?uDa6Q9km0A4h}f9K+9a_<@bQIYNm@*6<VzM9NUlUs01*|mjE2^Hd&d=*FKpeivb<<3HP>pq_O&n0-gD#eSC8S+nYo*8$Qv#4-c}O;O4_ZL|KyKquN;`(vQU{@n7`@DbSi-a)7qq2n69F=wK{K^GKp$J3pZYAYW0adyJzmXv$k_<h4a04+%tXi4ODToxH`FO_tcIZbpV5A_Ks_P4QH;uV#_^un{7KM$X$N>ofFsJl(N&cbF+JQPj1_3NI{*t2$s`@<57sQv#+xV7f<7XZRyx!N9b4M;K+DTjAr^Gf%3wa0}(BsTRL|1Rko&9ubppH2mla@{Z+#-Q-%=Qt(LJiNz#EYy{do)P_N=uor+iOh*|xEk2|lJggG_s<&~HBJwsm7qyplhxyt9(vg5~&J@~DO+GMh@`Q?{hp5MICY^?cq+jzO={vY<!{Oo`Do&3PduDzVQmNr&JR)b-1&HU*8=HUYxgjX|NZTmd<wwGq+n+?vg&^YTGD?a4GHDq<AnXfe^%l!(hEK=L)>YA=CXW0s8-nUk=_7b@uja*h+4cBTrk+vG5;YgHT%gn}UJeWILvgY@R5Jz~zdOCj{iY!*E)vA@ss;)#aqhs3&K|~7g0uw2O5CRq$gJg}BSThR%35h64lJ@dytJO+vHO7?&ACSn_tKR!cwUQ)htKCYf)x6cxATG;Q0t&|XXd)tt)y>o<c4B(+_~8>r4j#JozPC@zP3I6?8|y##{=DA2^13@-0{7BO2e$6rd2Z>{>7yr`m72Nk=2I)Fx#LbcdgSmo9||>Fz3EQx(=!K;ZoBhshxWht%)<|F!pZ!~>yI2b;EyMjYxgu0bL#QuT39nT-}&0J&q9E?8{WF)@x`xvQ<9p!=9c}BKV4bMtGC>B22y(B38|!d{hRl{@Cq(3P276-+10%L*I(D^q-w7?{KDZYZof^90Tm=bK=nb^Qwr-sGzO+rjU`A2AD?13z+Pj}_$ekMkFY28P_z%6J$EKsT}>-CttP4}iY^4Qc46m^g{@mE)ymc#JLWepG#icOrDf;+($XU4{+Wj#o|&C(HX7dh%sb<e6-d=NU$57Zs6I8h`-;8WcWmFfb62y~+O)8crfI9yN|Q9pvUaQ0Y_(3EI1VaLJo4D=%*^WI($W0~6GA0L<b=r})+eV>0vO(L+nb->x9^q@{%A6ps?t4IT@zgX^5KKlCRg5mt=x7aq7gy7=N=@1pn`z!eGdu*0NkD2y!T(`jaCvNQwaspyz?CaFd*-^=T>6UAc{!ud6xi+g85tb0+IwJMPL+C5V`E;o0V+Pz^eGZ_eD{IfA}6k+dOmjrN8+qdkv(h5WsG`>Wccp9EyO-x-3E?Xl&?Y9j$x7(8-3!aD?l5<p5%izS;|4&W0cT&O?pG#i`k84-i7&v~u@5e(2hpZrrqGbG2SaiuK-#2%xB41?O*i%N?5*Hnm%=%(>IYk3IU;Z$0tVM-#(uzW2WS-v7guT7|8xO-?ANM4es)RMT1w6lxO_(G7ORwO0ee?Qgj&P1B__=N|g@LrbSmH(L#6+dR`g^y1MM_C5Qq4}LJ0uxZQo#N+c%J~=Tnouo-{Zne2Kx3I8%$IgHNWFcB>fK?bt2mk~WfK(v_v~}d*0ZLGF^~j*g))FVGio{qNpcz4c0RXu$1fqgQqqV3(Q-mFWGJ&cM0H#*kw0kEx6;e_VVOy^TjQG-HL#iDQQ^tc&3L|s5W5xJ)iY~+rwXdKQacYKG^I{;)l|TV73oHN?Gq-E|^|#%8?M*jr*|igyHTWQ2wE+1r+KbGLmtS?QN|>0L1BBgIT`@g5_l4j6(|UdCogaAr^v+G<as_bCX&gzZfkwlqmdmdJ6qS=Cs7@`+z5B;M6r58KYb&48|MbXLzw^T5Pn~@A)w#`^#LMiqt<#(5*49?CyqzW!J0>o(CJ`yBg%*5L^wKvI3P45VW=|n)5d<KlqAn$L|LvLHzBf@t=y$FaZ%wT}z2|ah<$;M6P&Fe7s+I_uy6%>Z(b#rMVlFV(Is;Px1Qj7J=5ZriCK2L@usQ9l(uEA*fT5K?^YCNh!(H!s$45W$Ptr715htQP5EL@eNFY9R9u)us0OTrj+qTYc-n4w;?1@w7rnYY?adik`bjnA^t%Ti}9dOPO#&8|D{EEG`O6B0w&%OBU^LOvq1}@JDkj=!*T%DpLT7zhzl4|Mt>NejQvjS+0!0B@pW32TY(+Ilz#RcdBs}w*2kpOyCRxl!f%1Q*C@S-v3w&N;UGD`CX0M#tZsy5wt59fhDMCTlf0A0w8V2pkG@h6`8-Xmnp<~=*piMngG0I<O6!9I@aH~Fey7n)wtAQ}+$dA_#1(y6741xH-yxhMiM004kcNJL^-V{j@mH#vR96<2x*77&Ay5-NHkMN#yK(Lpu*==Cxs0))N~;-`oTkmoK*g_t*ZWU&GURRt6!09F8rc?{CdGFvrcQ69#meXHi}c64}jYi$6;NL$$O(}RFn)*cBPeK9Qul-ZftN|G+}>dgE+gji=n0kntV&fj@S3G;K$zjXG*nY3D+o|^#m@u)9Oy$cOQdrMo8B56^3-h~iE(rTq*Ee90<Eb3rrA$N4bVMi=@--oK0XYC-4fI1Pj<@^Xj0Eluk!7!@oMGzvY_b$sA!6*nqpknuR2u83Q|Fba~oAI2Gip{KNbybv^$6{C2^Y9-t$EeZ^T`M|KuhnaHHfHmdE$bcw5*|N%ByYC2?%uh5_s-!M?2Du>6C+k?6*heK+_|F%53w<EW9vAOE~!~U0v!Et5fY7O9lGLX=Yfb$Gh@al3U0iKuJL?mCOgqn8}G#!9%%{fx)CpMEt}`}J#+HJ@rkL)E!(#0B|z5>l54clOKon(Rx9g1sybLpA%v~FcGl|k5PX(ru(2a0Mo*5sUW)|U^*3Io+w&;N9t(aSld1Z@1CHZ(%<32L!5{)&5cm^`o`3#%pS#)l`RVz&b>m<K5!Y;4ByYfrU-w;gm{L`fiJD2Q1j(|P<n(>9=#Ju~^|b>qv=%rn$6ZNdW6B}UE9}`wG}ZwR^-FZVlf6qJ?Ad!cC8pJEWz80K%gYVv1sCcG#LJW4dqjP>?+4#rt=HGR5~vEO0f3l~AANOod6^Sisa7%OQm>n01Zz*6L`l)0Rz#d_pssr{&%<&65h1Oo>dHtOpG?_TKUo1HAU=ftG_m!Of-;ZB(+(oTwbBQF6a1}je$)K6EsG~kA3boC%A~uJFE5G^F>mL~XO@_#nYA~<JftG1o)OSI`_QA91qXtL2kbqUPD;cW?csg)1Pn!z3ZljUyi4vUI?fQ0Xhi+h;@b@kzDr{(?$nj~zdtVUSh{(A*9t=JeQ0K!%h$i~MGY#19zjqq0WTEMwc3s46+uYrRnQSJL>Em6fQ;N&TKUEozoM$Qz4?x-Z@4}Wej`vK2;jqr)c7%yL~#4>GZFUF#auJ+%Obrc%8vb_OOeoxeV1HPU&SSWGz4c5<C2J8A4gsVCg<j^y!93Z{Mw)Ww{L&x>o%zgVgx?9m;opNAZ2T<Y^{Nbo!T_Nku6OSRlx$EJalaF=y63@X*Mdg>IOH;A(W)f7h1SBHb4VwHmK<!(gjV$mqeY0E_uWQyv0mCt#rhim`Qe_7A~fn*wB!?Rn!%F{h<a;YPEm-Z~x`?>#xC;_NV^MZ@l{Afr?20R4-WVwWlj3=5K%f8>?rRw(Q(?%bV};G0k+ngv4mmZ+_()ZmE$@P2TjDI~0Kw%*M7MI#1D%aYZ{)JihzGf{MVx@#$!!!Gi?#IY=N-D)3=CfH~5Ap+e8UDk1nBi$cF@kU+#sP!$PYycY=of+_@xDkuR}NQE?z1QM@42k&CzgaR560;+UgjDX@L&rl?)*s4;3w<stOU~Hd20ffq7t9aCa8VCYvU=5JB=QhoL^b@~WnVvZF^1*-cGrw^3rGsg8lF|zF724`|CwHR95fvf#K?#>mpE>&COH3W(OJP`)0%i~eQ4mXz+%o*UbitAWSYs;HZ+-qtpZ(PD=OTB%_gx?R-~TBQk}9Gi#@QBtfEa;n1u0?@l<T4bDhRO(qYx@$EG7XI0c9je5u~gLP^<-N`HEu{C||{U2%WDeI-F1d6;J?5v>GNQ6o8I+s;G)0akMCa0Wd&MgXNTzF9^`XREQdHfv{jd(_UUCq9DRdTxJHwtVbV$wFUr!57DlRL;~s}B7kTFO;r^p(mapIEz#LZ03sn4f=^N(B+d&E5|oJz(Mir}BA_ZFqKHN2tEd<@Y)z}(Qc+D3HpV#z!2y6OSZhT<05x~M*>>V3h%we!>+{?>M;H+|K~+fs5T$Kyy!FO=Kk)7^|IvRv_42`g_4EJa1OMPBx9;8jrnlY^B#@~3!P@Owx;_*DLwN6p@BhmO{&?}lgP;9R|M|AJ{{RqSkTPikND);@0VzUa7kX5wQ9(ceL`Hh;l_Q`3y+8csAOD3eu1;^7{egG9J+xYo=Pm^Ay-iG#Br4i!HW4XJ)94rT&gEHd*%)KIb0T6B<Gp8Q5oN<<7!<rX4Gx0FVr0=?LkQrVhy?EeK&UwD(@I4}d<YT(8`C+0V-+&*eGoC$5>kW($h{95(IAu+Kt%}@FsSo+i;N}aPC|CO-3EYar2+tXo+AK7xLamb@Xix)?s5c3Z4y(o<F(j$?rGKTAy_ICMT%6B9Ev@ANQtu%*P@go)%(070%I@S4}vvGX^+qz$6m)}3{U_Ol!!1rJC&BAfDb`J3HB9-UWVatVu%=G+6ZEgx?hZf6ac{!5Rw7<qfdYOv%mXkSZxK+ncdqy_J4kI?{!xP)g60w185K-j@S#R0HVTdKy>Zw;+ZpxkALaGKm66-Y+L<_fBN$u{K)@Uov1t4F4FBm3qN@T>h8F=6bPA<3IO^nf9|m-f92;tzIOB!0@P=x|Cj&clW%(4-Od%@5b**;f>Kh4(%cq5C?h;#3^H`!LkqY)mE5(9fTFHRLIKDoX}Pe_spnL*Tp%wOePM5MOV4Z~qKM=!i#tD+&BeVA37KuFSj6u{wcHw{oEp$5(M6YJ1bCqWx+iv{*nDnZd0)l7_7RphHRLYsh3Zm-+~oy~MEOalDQheZfFt&_Gtgmg0(kGwf)8FouPP8x4-|k6GjowE+;J*lm!mryl_C&gTB&^Pb6@=JfBkEkdogI()Mux&Du4K6|8U3NJ==HgICu8!TBFf!w>8Mr<kZuTKe2P?uD|*6S04NJcel<iR0EzmdbEN5P49o#d;a!^?zsETWTN6VAV>&-5E&4Wl@UY{2}IXc8jnBv1hm{={=uIdd~{#7+EBtDx&O!Re%BA~x%x`+-mvMB1^cF_PZ;do#|t5@N8?2F!FlnDg4zdgg#e6ftc?@gT><Uyuw3Z#4IoI!eIDZ(I?2O@otQAS>3Q6o#s1QFCp|<R4vfEDd;Y1uYtJvN4s_RtWgmhMq4$?s!e$a8TibhW8SrwxUiw7+5~W<7_k$)OEaEDRF@{a(8{Yuu_YD{kneF$!{hh-v?|=63CtrSSU)Ijha6q+5QmNNkt(Ff#MVQF2$(k(!U?LKnxpMc%KJkkW{OZ3ux&N>rsi9l$eal@x{6l+gxF(l;_ntjjyM5}|i9;{GJUctTwz|4<cJbWFQ?KlM?xiQ61psi~1jTClQ~&6HdiRfiz+><(W8{9vajzPyBcNG(?x~L{0lagnQ4)oLiX6;rOsAyCg_ofJubu$}?<7Q+85M*MOf|%#`GW9zgO67aUk-2`u06M}f1A8`HLYi?BEh?Xuj73aASFpZQx5;Iw^141wpG;yuhM^CMT8ErF^r6Z?euK(y+#2oly;LOj3l{x@UOqR@3F^^9XRspfkSzt1p=a)CJ7tUZnudIF`LA;v+N)I+|R!CJ@2f|PcNM~{eS<v-+c5d4<<-n6^PPmCDX8N$M(kBT61+RZ?&O7@Cu@u2&BY;Y5U$iH{N#3)i+-E)*rghX;2XaWt&8(`O<$kU|Z4t_kG6|^lhD*`&>ne81Q~5Kw}dwoh}1OH5Xj+z8<3r8!wP}9zs07fys~^h{?DBgDRBf{Za_&xvaoE?|#tVP_I8`$c*3fD{;Yhu+&Pqr?6hKvAy_xgJn<#lCKAL%CZsH0g><CSWNdu=EM+RVDYr~4HjZ-r)6Ue6EB}Vcjok&!}|{a=;<?OuD<%}TD5xQ=&MPRZr-xFQmw8ouU>c44P;1y*u)+=dh`!I^}scIulULrzkKr83H1V`S-VX{#u`zuX`-ML(^FH^(>r$U+_rQ3-m9*>>W1s)w`>;iF6+X167}zt+B<*oZAZKtV#?m_21~GG6orAJ=V(o2%Gg8S<WT2b-_-XYMR$Iz;(ZsdxiDKO#W<v7AW&$yK`4dVQamd%xcW0Gu=VWI(6gHqr)NhRgDwtEIgsMd4n9PL5O*Q(j5Y3&QVM*AZSVLxN>abb*E752P8shwp2Xg}Abm%4DI8&HEFu@akcf$e9i6z;rFu8a5&I1U?-7s;35F=qgDMaKv0-LKgXr?mnLH*U!-TkaZt2j0L#;-W2o4`Ss0urG?ef8I-m(RmW@ct4XQtCMVZ_WkA3{(;RZyXF-?EA6+3pJ0wDthWc5!yJ)Cr2k>Ra}JB;HHR;p)3zK*Y%R16Itkp%I|9h1(FRl->aVym%k-7-=6t`Lwhc8DkAm--!D6mtM3W1&S&&mMm7nZ72ZZ>hn)`bodz2UQU(*ph#e50F)5O7{H=c@4ZIT6#^3jsLxwn?HeG1tSKQ|W|JVGXn~AMNGcKFEed`dy)r>WB^s_`x{I=5MN}V96+}aD3SBpsF;+xPl31IFf(yP=4JddQ;hN%oO1Uuc)*@nTkU&U81l}{CcV0sPfB*qvNfcE9AZra95RGi2NB~NRsvsypWY{FOLWHi}jw#U*eN<I~DlrK_$ej_5dkiWlW6%(vW@6$bA!fryR8_?LV2riaNGuM5XpLcJRdu<Gr3jcggdm{IMl=wTh>)?U>asS7NC>6AhpLKfD)l-NdGCYwaRv|(6p}Pm(1`EJ#L@SIh~7C>^<E-WP)w#Hf<|N602QIau^Jc>Fr~FRh)M{B<cbIyvMfWyO0^n7Q9OhYjkRoS2ok(EL|HpS0yZXhIUy>jfz%jgLJ|qaB!mT6V6j(;7Pc-?VARqxKp{ZzsuFxiD-}f0wrMpQ01!3MXb&Lfv{tie1rR%RcL_+On6D55047PQ5phtYPz~b)#|(yitF1ny#^$Z21TP{H-qW%X22-urdfkg)2pxYKhY(y2fXoC6QZ5f0qauI?p@f`7^x9@3%3a=Qp{R%{q6SqFAgR}Fl6VO&coko<i54s?K>{%m8&C?WSV?@e><~HUthI)j4Fgd~Jt0V|6>>)qD}@w0leG!gCxDok<7UEMm<@n3V44<BNOYN`m7u{PU`(47AmXUIAVj#h5JK=6#FFvipoC4Nw92(f07w8ugs^*55RoEuLb*ETCzI3wltmN*Q;ehrgir+^vYZqd02Bj&5CU71B+&Kv#zwG`))f?p7?7)ljup>qOw?+E3TbMQ0EsB1aoSC#KGAbbbdh+AVaHuFdQ+eqCW?f}DFSdJ0zw3846-2svK;fk69pw;lPDQg?Br!B0CC|ZHwFM9C;%3@p5@UUe~BQ#)f%dzsJ7dP%pB(#1VIHfhz1c<A`_(`RRA)!YCGel0x2B?6sRcL0$doikW&C9qey_N#<0eY5eN`LgcPkwH7Vfn3T4T#DgYGP7b2R(m?Tc7DG$U5xlJ}jP|^(IW36D&#4`(s$k?C}Sr-9-m`V$*A`w6*JXZk_InkI^%Y;a!aHR?mP??F46h#miZRg~KqBge*2oOrwD1@PWW=kHB?p1N2!6-mke-M>99vP}-fnfmwQBfU?Pf#dsw^v>&ZbdsuOJo!xj4s7BHvpsK9XpC|DNqjo2o*XOPmrQIdHlR5vKOKEp1Y0rX&-}cdqvPFOAH4`bz=KaJI{CTx4rFj%o@F7W$#;*ASyyI(2EiR#_C4py%s9t$eZepx@&-nLyebrz%09CQ7B+qM_X?P-}E*+5N)evYkeOoK%Aw{BQ>ZIju`$0NP|QLr8`X>9Q9E@KVLiN(aaGdNA|uhp1Q~s=kG@W+O76RqXbJ0a8MRUM8vF}1qs9P1|x=de(GQq4PVe|wW4Hkk<Dp8_1?oUA)<56dw(gGxY2|$>LNx>_I8Vah<Tp-{`&Om=>m}eSo<<F<L5yn?*ZuFAkolkJro_C=S%F`*a!>CvUV7iTSGDUcLQu6hn;1a%818@nJ=7caWRC5d6s)OXv!@@?}p=_*4K-IYiAmyjH~bYiipOs5W#t$<-_)TjA3Hqi#*5v*ZK&JF`cRHZH2~?&8WaUI$16n3^o$nUP^MTBX;9Xs?<g)CJYqr{j$AyYF|u9=*3WsnTYo@>QEU&Cp;=AGHM+#`uJWCQ4bcQTznWd0F;JE1RziXA}y_s*n!kkMZB~|dr3iK;XqVm9&}-mfC6Z&GrobXvIs0=6Of=EoL2$Buta64-+gjPqyS_X5aT#w*jAKClo0WPuEdM)1pzI`h(jt%BNoyx$3V0~5MJMHs46fj_o8h^Aa4Nz#WzxlEdT&QbYTrh{>02?5W#xgG!WYyHw2p`S{}h0paQFCpdBP+V>dqf2(dIQ2B>Ia?f3#@qqVzVb5&4KYwb8@2~=V5TvCNtb%w_udA=bk?5i}Q$RBP<D(F&-C+L-0;@fyEZSZVT1!IgcW;i8tJfl}Y#Ka~&+CltSHz<1ybVJO>49boeSK%UR4PFc-X)-iPV+N=kUyAMdIAcu1Ei-|78b&NEkz>g#kN*sM;V#uCaUL2rtCd}egsvxdV>EK0QEVNqP`LhHWY7*#>JnpP%&{@0sA>@CPbx0WBApjp($KLq20^zR%>Z>wr5oX#D5dKl&_8q|2F5`B&s1Sk88Rzwgd%*+Kyy9O)?>Jj;^7+pNOWUM&_`pFDFMJl92_i5A|R+pD4ejpOnLFMgHRx5b+ZyW-$jOZ-VfsAUFz78Vx%{!(og{k@L>!Fo46162drRJGkxg(Vq-lB6e{pQIJT<BVr}CPjsg0PL<LYl2_e=P9uJLer}V+gz(cPwoOTT6F;xu`LI?xwL1Stk5hR3IinO<fXt3G1egFUp;Jh1V?`Xu?c>4hHF%=*Da4&2|V+>s?A%b&$a1T)EWOt2)#?}z`1@r?zVT>5diWb~4q<xqE%nfQes<Eo%P-=N8P>x5cG&~63STsJK8H(lzjOj{4Uya95sj6&-KrV}-!*8_X8=y>>8Td@SAMxN`Diu+8L$|G<&bjfdDvWZIs(R<f<8K+oeFzwWjAc15B-0_f-066<@6pb)P@FU4p)o-LB6;URsTmY9jRGPXW-JXW!|tz(q!>my;AZRwWDG_#T;li@K#Kym15hkcJQ&M9sQ}&;&u7fTj9Kx7g9sw)?Ez3hgNXM7V!IY)oX2x&Ip=!Q1LImV^YA&dZW>QRsA`OfDWBNc5O7?FcU(0ZG|%F=4y8gWf+0a*$PBe18aVj$ywD-*rI@CNBibETs0095YepPcZ_ML6rtuC~`4Djoj_>l|8|3g93_d3LS_>Ck-)IZR`WTo82mbH;HAZ%cEspas8bN~rghjXG+8qF3toW28J{;rp;4o|uLPTzeTIWXFFVF{uH<=AK97!*rkd26QTOT2m@ns{v8q2vA-Dkrgi#_>*W1um5bcV)Mcr3;t|BebIK!^r!Q60m6GqMF$kRW5*14cf#V?@@|(VZZ`ptWuTG??xRfPf-#Ul`9sZICGyKoz_~P?0!5Eu&Q8LE=Ta)m<@WOJ2eRb;VOr=wH7W^FpEwcwS(Jiy(<{P9h*9JeC?^q*de+N8U>aM2afDlfD1|s6c=!0%Zi`x)s4l1WckJ9t)tVPVWf8qY9u3!urCUO8FgQMxK@yT@plPP!P$>C^IYq$JT!%8>PZq6GFhAf?y@kv3ln=@&I+#NQOXDV;8}D4I?7YFR2Sv5Fdu|9TCAhry@hy7MI+Ih>Y|oYKS?UW7%U+LV!_{jD#Rz{UGh#c0?lfRk5U6{HrR#`?9h{9LxH98<&;<5wEcm177%}1nihJkr0MpTVfZu;V2sf04QK*1_Cl7J`>`34#tb`0=@U5GTg>E(ZUfz@FQ8jkOeo~gQ^Y}c8`Ai(zP)V>aZRflSv2>5v7~#*VB3s)QubAkcdZO#g>ZBI$Mt0BqEHCryP?}3u9UZj995C7LP}JRps-<$#487;v6HL*RLxvXP-J8xqeys`&+UE0b_#t2HR19sM3u5(rq9m3QKooG)WG&f*3I!H^?ulT4cQsJB<K>599L3c9QFdhv3{s6T1*1wCEtW#s0dW^aYaq`fum|1AigTOE^5efB*mh07*qoM6N<$f&'
MICHI_IMAGE_DATA = base64.b64encode(base64.b85decode(_MICHI_IMAGE_DATA_B85)).decode('ascii')


def now_string() -> str:
    return datetime.now().strftime('%Y-%m-%d %H:%M')

def today_string() -> str:
    return date.today().isoformat()

def parse_date_string(value, default=None):
    try:
        if not value:
            return default
        return date.fromisoformat(str(value)[:10])
    except Exception:
        return default

def clamp(value, minimum=0, maximum=100):
    try:
        value = int(value)
    except Exception:
        value = minimum
    return max(minimum, min(maximum, value))

def safe_int(value, default=0):
    try:
        return int(value)
    except Exception:
        return default

def safe_float(value, default=0.0):
    try:
        return float(str(value).replace(',', '.'))
    except Exception:
        return default

def hash_password(password: str) -> str:
    salt = secrets.token_hex(16); pw_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 120000).hex(); return f'pbkdf2_sha256${salt}${pw_hash}'

def verify_password(password: str, stored_password: str) -> bool:
    try:
        if stored_password.startswith('pbkdf2_sha256$'):
            _, salt, saved_hash = stored_password.split('$'); new_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 120000).hex(); return secrets.compare_digest(new_hash, saved_hash)
        return password == stored_password
    except Exception:
        return False

class DataManager:

    def __init__(self, file_path=DATA_FILE):
        self.file_path = file_path

    def load(self):
        if not os.path.exists(self.file_path):
            return {}
        try:
            with open(self.file_path, 'r', encoding='utf-8') as fh:
                data = json.load(fh)
            return data if isinstance(data, dict) else {}
        except json.JSONDecodeError:
            backup = self.file_path + '.corrupted_backup'
            try:
                shutil.copy(self.file_path, backup)
            except Exception:
                pass
            return {}
        except Exception:
            return {}

    def save(self, data):
        try:
            payload = json.dumps(data, indent=4, ensure_ascii=False)
            if os.path.exists(self.file_path):
                try:
                    with open(self.file_path, 'r', encoding='utf-8') as fh:
                        if fh.read() == payload:
                            return True
                except Exception:
                    pass
            with open(self.file_path, 'w', encoding='utf-8') as fh:
                fh.write(payload)
            return True
        except Exception as error:
            messagebox.showerror('Guardar', f'No se pudieron guardar los datos:\n{error}'); return False

def default_user(password: str) -> dict:
    return {'password': hash_password(password), 'profile': {'theme_mode': 'light', 'theme_variant': 'strawberry', 'custom_primary': '#ff6b98', 'custom_bg': '#fff7fa', 'spotify_url': 'https://open.spotify.com', 'youtube_url': 'https://www.youtube.com', 'created_at': now_string()}, 'currency': {'fresas': 100, 'xp': 0, 'level': 1}, 'pomodoro': {'study_minutes': 25, 'break_minutes': 5, 'long_break_minutes': 15, 'completed_today': 0}, 'tasks': [], 'moods': [], 'subjects': {}, 'library': [], 'study_plan': '', 'quick_scratch': '', 'pet': {'name': 'Michi', 'species': 'gatito estudio', 'energy': 85, 'happiness': 90, 'hunger': 20, 'level': 1, 'xp': 0, 'accessory': 'Moño verde', 'outfit': 'Vestido fresa', 'base_color': 'Crema', 'hood_color': 'Rojo fresa', 'dress_color': 'Rojo fresa', 'personality': 'Dulce', 'expression': 'Alegre'}, 'inventory': [], 'shop_history': [], 'achievements': [], 'settings': {'pro_home': True, 'auto_optimize': True, 'animations': True, 'compact_tabs': True}, 'metrics': {'pomodoros_completed': 0, 'tasks_completed': 0, 'moods_registered': 0, 'mini_games_won': 0, 'optimizations_run': 0, 'last_optimized': 'Nunca', 'study_streak': 0, 'last_study_day': ''}}

class PomodoroTimer:

    def __init__(self):
        self.seconds_left = 25 * 60; self.total_seconds = self.seconds_left; self.mode = 'study'; self.running = False; self.after_id = None

    def configure(self, minutes: int, mode='study'):
        self.seconds_left = max(1, int(minutes)) * 60; self.total_seconds = self.seconds_left; self.mode = mode

    def start(self, root, on_tick, on_finish):
        if self.running:
            return
        self.running = True; self._tick(root, on_tick, on_finish)

    def _tick(self, root, on_tick, on_finish):
        if not self.running:
            return
        if self.seconds_left <= 0:
            self.running = False; self.after_id = None; on_tick(0); on_finish(self.mode); return
        on_tick(self.seconds_left); self.seconds_left -= 1; self.after_id = root.after(1000, lambda: self._tick(root, on_tick, on_finish))

    def pause(self, root):
        self.running = False
        if self.after_id:
            try:
                root.after_cancel(self.after_id)
            except Exception:
                pass
        self.after_id = None

    def reset(self, root, minutes, mode='study'):
        self.pause(root); self.configure(minutes, mode)

class RoundedFrame(tk.Frame):

    def __init__(self, parent, bg, fill, outline, radius=22, padding=14):
        super().__init__(parent, bg=bg); self.fill = fill; self.outline = outline; self.radius = radius; self.padding = padding; self.canvas = tk.Canvas(self, bg=bg, highlightthickness=0, bd=0); self.canvas.place(x=0, y=0, relwidth=1, relheight=1); self.content = tk.Frame(self, bg=fill); self.content.pack(fill='both', expand=True, padx=padding, pady=padding); self.bind('<Configure>', self.draw); self.canvas.lower('all')

    def draw(self, event=None):
        self.canvas.delete('all'); w = self.winfo_width(); h = self.winfo_height(); r = self.radius
        if w < 2 or h < 2:
            return
        self.canvas.create_arc(1, 1, r * 2, r * 2, start=90, extent=90, fill=self.fill, outline=self.outline); self.canvas.create_arc(w - r * 2 - 1, 1, w - 1, r * 2, start=0, extent=90, fill=self.fill, outline=self.outline); self.canvas.create_arc(1, h - r * 2 - 1, r * 2, h - 1, start=180, extent=90, fill=self.fill, outline=self.outline); self.canvas.create_arc(w - r * 2 - 1, h - r * 2 - 1, w - 1, h - 1, start=270, extent=90, fill=self.fill, outline=self.outline); self.canvas.create_rectangle(r, 1, w - r, h - 1, fill=self.fill, outline=self.fill); self.canvas.create_rectangle(1, r, w - 1, h - r, fill=self.fill, outline=self.fill); self.canvas.create_line(r, 1, w - r, 1, fill=self.outline); self.canvas.create_line(r, h - 1, w - r, h - 1, fill=self.outline); self.canvas.create_line(1, r, 1, h - r, fill=self.outline)
        self.canvas.create_line(w - 1, r, w - 1, h - r, fill=self.outline)

class MichiStudioApp:

    def __init__(self, root):
        self.root = root; self.root.title(APP_NAME); self.data_manager = DataManager(); self.users = self.data_manager.load(); self.current_user = None; self.user_data = None; self.timer = PomodoroTimer(); self.pet_animation_id = None; self.home_pet_canvas = None; self.study_pet_canvas = None; self.shop_preview_canvas = None; self.inventory_preview_canvas = None; self.quick_mood = tk.StringVar(value='😊 Feliz'); self.mood_intensity_var = tk.IntVar(value=7); self.mood_energy_var = tk.IntVar(value=6); self.flash_difficulty_var = tk.StringVar(value='Normal'); self.flash_filter_var = tk.StringVar(value='Todas'); self._subject_order = []; self._shop_index_map = []; self._inventory_index_map = []; self._library_index_map = []; self.show_login()

    def ensure_schema(self):
        template = default_user('temp'); old_password = self.user_data.get('password', ''); self.merge_defaults(self.user_data, template)
        if old_password:
            self.user_data['password'] = old_password
        if isinstance(self.user_data.get('subjects'), list):
            migrated = {}; notes_by_subject = self.user_data.get('notes_by_subject', {})
            for subject in self.user_data.get('subjects', []):
                data = notes_by_subject.get(subject, {})
                if isinstance(data, str):
                    data = {'notes': data, 'grades': [], 'files': [], 'flashcards': []}
                migrated[subject] = {'notes': data.get('notes', ''), 'grades': data.get('grades', []), 'files': data.get('files', []), 'flashcards': data.get('flashcards', [])}
            self.user_data['subjects'] = migrated
        if isinstance(self.user_data.get('notes_by_subject'), dict) and (not self.user_data.get('subjects')):
            migrated = {}
            for subject, data in self.user_data.get('notes_by_subject', {}).items():
                if isinstance(data, str):
                    data = {'notes': data, 'grades': [], 'files': [], 'flashcards': []}
                migrated[subject] = {'notes': data.get('notes', ''), 'grades': data.get('grades', []), 'files': data.get('files', []), 'flashcards': data.get('flashcards', [])}
            self.user_data['subjects'] = migrated
        pet = self.user_data.get('pet', {}); color_map = {'Crema': '#f9f1e3', 'Rosado': '#ffdbe8', 'Gris': '#d8d8de', 'Canela': '#d6b18d', 'Blanco': '#fffafa'}
        if 'base_color' not in pet:
            pet['base_color'] = pet.get('color', 'Crema')
        pet.setdefault('hood_color', 'Rojo fresa'); pet.setdefault('dress_color', 'Rojo fresa'); pet.setdefault('outfit', 'Vestido fresa'); pet.setdefault('expression', 'Alegre'); pet.setdefault('accessory', pet.get('accessory', 'Moño verde')); pet.setdefault('personality', pet.get('personality', 'Dulce')); self.user_data['pet'] = pet
        if not isinstance(self.user_data.get('library'), list):
            self.user_data['library'] = []
        if not isinstance(self.user_data.get('inventory'), list):
            self.user_data['inventory'] = []
        if not isinstance(self.user_data.get('tasks'), list):
            self.user_data['tasks'] = []
        if not isinstance(self.user_data.get('moods'), list):
            self.user_data['moods'] = []
        for subject_data in self.user_data.get('subjects', {}).values():
            if isinstance(subject_data, dict):
                for card in subject_data.setdefault('flashcards', []):
                    if isinstance(card, dict):
                        card.setdefault('created_at', now_string()); card.setdefault('difficulty', 'Normal'); card.setdefault('tags', ''); card.setdefault('due', today_string()); card.setdefault('interval', 0); card.setdefault('ease', 2.5); card.setdefault('reviews', 0); card.setdefault('correct', 0); card.setdefault('lapses', 0); card.setdefault('last_review', '')
        self.save()

    def merge_defaults(self, target, default):
        for key, value in default.items():
            if key not in target:
                target[key] = value
            elif isinstance(value, dict) and isinstance(target.get(key), dict):
                self.merge_defaults(target[key], value)

    def save(self):
        if self.current_user and self.user_data is not None:
            self.users[self.current_user] = self.user_data; self.data_manager.save(self.users)

    def palette(self):
        profile = self.user_data.get('profile', {}) if self.user_data else {}; mode = profile.get('theme_mode', 'light'); variant = profile.get('theme_variant', 'strawberry')
        palettes = {'strawberry': {'light': {'bg': '#fff7fa', 'card': '#ffffff', 'primary': '#ff6b98', 'secondary': '#ffc1d6', 'accent': '#cdeccf', 'danger': '#ffd6db', 'text': '#3b2b34', 'muted': '#7f6b74', 'soft': '#ffeaf1'}, 'dark': {'bg': '#1f161c', 'card': '#2d2027', 'primary': '#ff7ba4', 'secondary': '#6b4155', 'accent': '#72c89f', 'danger': '#7b3347', 'text': '#fff4f8', 'muted': '#d4bcc5', 'soft': '#392732'}}, 'lavender': {'light': {'bg': '#f8f4ff', 'card': '#ffffff', 'primary': '#9b7cf6', 'secondary': '#d8cafe', 'accent': '#cbe7ff', 'danger': '#f5d0e7', 'text': '#2f2740', 'muted': '#756b8a', 'soft': '#eee7ff'}, 'dark': {'bg': '#171322', 'card': '#261f35', 'primary': '#b49cff', 'secondary': '#5b4f7d', 'accent': '#5ab0f5', 'danger': '#7d365e', 'text': '#f8f4ff', 'muted': '#d0c5e6', 'soft': '#302642'}}, 'mint': {'light': {'bg': '#f3fff9', 'card': '#ffffff', 'primary': '#3bc893', 'secondary': '#b2efd7', 'accent': '#bfdbfe', 'danger': '#ffd2d2', 'text': '#1c3a30', 'muted': '#577168', 'soft': '#e2fff1'}, 'dark': {'bg': '#101f18', 'card': '#1a3027', 'primary': '#49d9a2', 'secondary': '#2f5d4b', 'accent': '#6ea8ff', 'danger': '#7f3131', 'text': '#ecfff7', 'muted': '#b7d8c9', 'soft': '#234136'}}, 'blue': {'light': {'bg': '#f3f8ff', 'card': '#ffffff', 'primary': '#4d8df7', 'secondary': '#bfd8ff', 'accent': '#c9f0ff', 'danger': '#ffd6db', 'text': '#233047', 'muted': '#66738c', 'soft': '#e6f0ff'}, 'dark': {'bg': '#111827', 'card': '#1d2a3d', 'primary': '#7db0ff', 'secondary': '#38557a', 'accent': '#5ed0e6', 'danger': '#7b3347', 'text': '#f2f7ff', 'muted': '#c3d2e8', 'soft': '#253852'}}, 'custom': {'light': {'bg': profile.get('custom_bg', '#fff7fa'), 'card': '#ffffff', 'primary': profile.get('custom_primary', '#ff6b98'), 'secondary': '#dfd4f8', 'accent': '#caead1', 'danger': '#ffd6db', 'text': '#342a36', 'muted': '#766b79', 'soft': '#f3eafb'}, 'dark': {'bg': '#17131c', 'card': '#251e2c', 'primary': profile.get('custom_primary', '#ff6b98'), 'secondary': '#5c4d68', 'accent': '#73bda5', 'danger': '#7b3347', 'text': '#faf6ff', 'muted': '#d7cbde', 'soft': '#30263a'}}}
        return palettes.get(variant, palettes['strawberry'])[mode]

    def style_ttk(self):
        c = self.palette(); style = ttk.Style()
        try:
            style.theme_use('clam')
        except Exception:
            pass
        style.configure('TNotebook', background=c['bg'], borderwidth=0); style.configure('TNotebook.Tab', background=c['soft'], foreground=c['text'], padding=[20, 11], font=FONT_BODY_BOLD, borderwidth=0); style.map('TNotebook.Tab', background=[('selected', c['primary'])], foreground=[('selected', 'white')]); style.configure('TCombobox', padding=6, font=FONT_BODY); style.configure('Treeview', font=FONT_BODY, rowheight=28, background=c['card'], fieldbackground=c['card'], foreground=c['text'], borderwidth=0); style.configure('Treeview.Heading', font=FONT_BODY_BOLD, background=c['soft'], foreground=c['text'], padding=6); style.configure('TButton', font=self.app_font(10, 'bold'), padding=[10, 6])

    def clear_root(self):
        if self.pet_animation_id:
            try:
                self.root.after_cancel(self.pet_animation_id)
            except Exception:
                pass
        self.pet_animation_id = None
        for widget in self.root.winfo_children():
            widget.destroy()

    def card(self, parent, title, emoji=''):
        c = self.palette(); outer = RoundedFrame(parent, bg=c['bg'], fill=c['card'], outline=c['secondary'], radius=24, padding=16); frame = outer.content; frame.rounded_outer = outer; title_label = tk.Label(frame, text=f'{emoji} {title}'.strip(), bg=c['card'], fg=c['primary'], font=self.app_font(15, 'bold')); title_label.michi_card_title = True; title_label.pack(anchor='w', pady=(0, 12)); return outer

    def card_content(self, card):
        return getattr(card, 'content', card)

    def progress_bar(self, parent, value, maximum=100, height=14, color=None, bg=None):
        c = self.palette(); color = color or c['primary']; bg = bg or c['soft']; canvas = tk.Canvas(parent, height=height, bg=c['card'], highlightthickness=0); canvas.pack(fill='x', pady=3)

        def draw(event=None):
            width = max(10, canvas.winfo_width()); canvas.delete('all'); percent = max(0, min(1, float(value) / max(1, float(maximum)))); canvas.create_rectangle(0, 0, width, height, fill=bg, outline=''); canvas.create_rectangle(0, 0, int(width * percent), height, fill=color, outline='')
        canvas.bind('<Configure>', draw); draw(); return canvas

    def open_url(self, url):
        try:
            webbrowser.open(url)
        except Exception as error:
            messagebox.showerror('Abrir enlace', f'No se pudo abrir el enlace:\n{error}')

    def show_login(self):
        self.clear_root(); self.root.geometry('560x500'); self.root.minsize(520, 460); bg = '#fff7fa'; self.root.configure(bg=bg); frame = tk.Frame(self.root, bg=bg); frame.place(relx=0.5, rely=0.5, anchor='center'); tk.Label(frame, text='🐱 Michi Studio', font=(FONT_FAMILY, 30, 'bold'), bg=bg, fg='#ff6b98').pack(pady=8); tk.Label(frame, text='estudio · organización · gatito kawaii', font=FONT_SUBTITLE, bg=bg, fg='#4a3740').pack(pady=4); tk.Label(frame, text='Usuario', bg=bg, fg='#4a3740').pack(pady=(18, 2)); self.login_user = tk.Entry(frame, width=34, font=(FONT_FAMILY, 12), relief='flat', bd=6); self.login_user.pack(pady=3); tk.Label(frame, text='Contraseña', bg=bg, fg='#4a3740').pack(pady=(8, 2)); self.login_pass = tk.Entry(frame, width=34, show='*', font=(FONT_FAMILY, 12), relief='flat', bd=6); self.login_pass.pack(pady=3)
        tk.Button(frame, text='Entrar', width=28, bg='#ff6b98', fg='white', font=FONT_BUTTON, relief='flat', bd=0, activebackground='#ff8ab0', command=self.login).pack(pady=12, ipady=6); tk.Button(frame, text='Crear cuenta', width=28, bg='#d8f2da', fg='#3b2b34', font=FONT_BUTTON, relief='flat', bd=0, activebackground='#c6ecc9', command=self.register_window).pack(pady=3, ipady=6)

    def register_window(self):
        win = tk.Toplevel(self.root); win.title('Crear cuenta'); win.geometry('390x340'); win.configure(bg='#fff7fa'); win.resizable(False, False); tk.Label(win, text='Crear cuenta 🐱', font=('Arial', 20, 'bold'), bg='#fff7fa', fg='#ff6b98').pack(pady=15); tk.Label(win, text='Usuario', bg='#fff7fa').pack(); user = tk.Entry(win, width=32); user.pack(pady=4); tk.Label(win, text='Contraseña', bg='#fff7fa').pack(); pw = tk.Entry(win, width=32, show='*'); pw.pack(pady=4); tk.Label(win, text='Confirmar contraseña', bg='#fff7fa').pack(); pw2 = tk.Entry(win, width=32, show='*'); pw2.pack(pady=4)

        def do_register():
            username = user.get().strip(); password = pw.get().strip(); confirm = pw2.get().strip()
            if not username or not password:
                messagebox.showerror('Registro', 'Usuario y contraseña son obligatorios.'); return
            if password != confirm:
                messagebox.showerror('Registro', 'Las contraseñas no coinciden.'); return
            if len(password) < 4:
                messagebox.showerror('Registro', 'La contraseña debe tener al menos 4 caracteres.'); return
            if username in self.users:
                messagebox.showerror('Registro', 'Ese usuario ya existe.'); return
            self.users[username] = default_user(password); self.data_manager.save(self.users); messagebox.showinfo('Registro', 'Cuenta creada correctamente.'); win.destroy()
        tk.Button(win, text='Registrar', width=22, bg='#ff6b98', fg='white', command=do_register).pack(pady=16)

    def login(self):
        username = self.login_user.get().strip(); password = self.login_pass.get().strip()
        if username not in self.users:
            messagebox.showerror('Login', 'El usuario no existe.'); return
        if not verify_password(password, self.users[username].get('password', '')):
            messagebox.showerror('Login', 'Contraseña incorrecta.'); return
        self.current_user = username; self.user_data = self.users[username]; self.ensure_schema(); self.timer.configure(self.user_data['pomodoro']['study_minutes'], 'study'); self.build_main_ui()

    def logout(self):
        self.save(); self.timer.pause(self.root); self.current_user = None; self.user_data = None; self.show_login()

    def build_main_ui(self):
        self.clear_root(); self.style_ttk(); c = self.palette(); self.root.title(APP_NAME); self.root.geometry('1380x860'); self.root.minsize(1150, 740); self.root.configure(bg=c['bg']); header = tk.Frame(self.root, bg=c['primary'], height=60); header.pack(fill='x'); tk.Label(header, text='🐱 Michi Studio', font=(self.app_font_name(), 22, 'bold'), bg=c['primary'], fg='white').pack(side='left', padx=20); self.header_status = tk.Label(header, text='', font=(self.app_font_name(), 11, 'bold'), bg=c['primary'], fg='white'); self.header_status.pack(side='right', padx=10); tk.Button(header, text='Salir', command=self.logout, bg='white').pack(side='right', padx=4); tk.Button(header, text='Exportar', command=self.export_user_data, bg='white').pack(side='right', padx=4)
        tk.Button(header, text='Modo nocturno', command=self.toggle_dark_mode, bg='white').pack(side='right', padx=4); self.notebook = ttk.Notebook(self.root); self.notebook.pack(fill='both', expand=True, padx=12, pady=12); self.home_tab = tk.Frame(self.notebook, bg=c['bg']); self.study_tab = tk.Frame(self.notebook, bg=c['bg']); self.subjects_tab = tk.Frame(self.notebook, bg=c['bg']); self.library_tab = tk.Frame(self.notebook, bg=c['bg']); self.shop_tab = tk.Frame(self.notebook, bg=c['bg']); self.settings_tab = tk.Frame(self.notebook, bg=c['bg']); self.notebook.add(self.home_tab, text='🏠 Inicio'); self.notebook.add(self.study_tab, text='🍅 Estudio'); self.notebook.add(self.subjects_tab, text='📚 Materias'); self.notebook.add(self.library_tab, text='📖 Biblioteca'); self.notebook.add(self.shop_tab, text='🛍 Tienda')
        self.notebook.add(self.settings_tab, text='⚙ Ajustes'); self.build_home_tab(); self.build_study_tab(); self.build_subjects_tab(); self.build_library_tab(); self.build_shop_tab(); self.build_settings_tab(); self.refresh_all(); self.apply_fonts_to_widgets(); self.animate_pet()

    def color_value(self, label):
        mapping = {'Crema': '#f6f0e1', 'Rosado': '#ffdbe7', 'Gris': '#d9dce4', 'Canela': '#d7b08c', 'Blanco': '#fffdfd', 'Marrón': '#9a785f', 'Rojo fresa': '#de4b42', 'Rosa chicle': '#ff7fa7', 'Lavanda': '#b598ff', 'Menta': '#7ed6b3', 'Azul cielo': '#8ac6ff', 'Vainilla': '#f4d98b', 'Verde matcha': '#a8bf67', 'Rojo coral': '#ef675d'}; return mapping.get(label, label if str(label).startswith('#') else '#f6f0e1')

    def ensure_michi_assets(self):
        if getattr(self, 'michi_photo', None) is None:
            try:
                self.michi_photo = tk.PhotoImage(data=MICHI_IMAGE_DATA); self.michi_runner_photo = self.michi_photo.subsample(3, 3)
            except Exception:
                self.michi_photo = None; self.michi_runner_photo = None


    def build_home_tab(self):
        c = self.palette(); main = tk.Frame(self.home_tab, bg=c['bg']); main.pack(fill='both', expand=True, padx=10, pady=10); main.grid_columnconfigure(0, weight=1, uniform='home_cols'); main.grid_columnconfigure(1, weight=1, uniform='home_cols'); main.grid_rowconfigure(0, weight=1); left = tk.Frame(main, bg=c['bg']); left.grid(row=0, column=0, sticky='nsew', padx=(0, 8)); right = tk.Frame(main, bg=c['bg']); right.grid(row=0, column=1, sticky='nsew', padx=(8, 0)); pet_card = self.card(left, 'Tu michi kawaii', '🐾'); pet_card.pack(fill='both', expand=True, pady=6); pet_body = self.card_content(pet_card); self.home_pet_canvas = tk.Canvas(pet_body, width=220, height=245, bg=c['card'], highlightthickness=0); self.home_pet_canvas.pack(pady=4)
        self.pet_speech = tk.Label(pet_body, text='', wraplength=430, bg=c['card'], fg=c['text'], font=('Arial', 11, 'italic')); self.pet_speech.pack(pady=2); self.pet_info = tk.Label(pet_body, text='', bg=c['card'], fg=c['text'], justify='center', font=self.app_font(10, 'bold')); self.pet_info.pack(fill='x', pady=6); actions = tk.Frame(pet_body, bg=c['card']); actions.pack(fill='x'); tk.Button(actions, text='🍓 Alimentar', command=self.feed_pet, bg=c['accent'], relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').pack(side='left', fill='x', expand=True, padx=4, ipady=7); tk.Button(actions, text='🎲 Jugar', command=self.play_pet, bg='#cfe8ff', relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').pack(side='left', fill='x', expand=True, padx=4, ipady=7)
        tk.Button(actions, text='💤 Descansar', command=self.rest_pet, bg='#e4d5ff', relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').pack(side='left', fill='x', expand=True, padx=4, ipady=7); tk.Button(actions, text='🎨 Personalizar', command=self.customize_pet, bg='#fff1b8', relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').pack(side='left', fill='x', expand=True, padx=4, ipady=7); level_card = self.card(right, 'Nivel y progreso', '⭐'); level_card.pack(fill='x', pady=(2, 6)); level_body = self.card_content(level_card); self.level_label = tk.Label(level_body, text='', bg=c['card'], fg=c['text'], font=self.app_font(10, 'bold')); self.level_label.pack(anchor='w'); self.level_holder = tk.Frame(level_body, bg=c['card']); self.level_holder.pack(fill='x')
        quick_card = self.card(right, 'Barra de búsqueda y accesos', '🔎'); quick_card.pack(fill='x', pady=6); quick_body = self.card_content(quick_card); self.home_search_entry = tk.Entry(quick_body, font=self.app_font(11), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary']); self.home_search_entry.pack(fill='x', pady=(0, 8), ipady=8); self.home_search_entry.insert(0, 'Buscar en Google recursos para estudiar...'); q_buttons = tk.Frame(quick_body, bg=c['card']); q_buttons.pack(fill='x', pady=(0, 8))
        for col in range(4):
            q_buttons.grid_columnconfigure(col, weight=1, uniform='home_links')
        tk.Button(q_buttons, text='🔎 Google', command=lambda: self.search_google(self.home_search_entry), bg='#cfe8ff', relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').grid(row=0, column=0, sticky='ew', padx=(0, 4), ipady=7); tk.Button(q_buttons, text='🎧 Spotify', command=self.open_spotify, bg='#b9f2c8', relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').grid(row=0, column=1, sticky='ew', padx=4, ipady=7); tk.Button(q_buttons, text='▶ YouTube', command=self.open_youtube, bg='#ffbcbc', relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').grid(row=0, column=2, sticky='ew', padx=4, ipady=7); tk.Button(q_buttons, text='🎵 Lo-fi', command=self.open_lofi, bg='#ead7ff', relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').grid(row=0, column=3, sticky='ew', padx=(4, 0), ipady=7)
        self.focus_tip = tk.Label(quick_body, text='', bg=c['card'], fg=c['muted'], font=self.app_font(9, 'bold'), anchor='center'); self.focus_tip.pack(fill='x', pady=(2, 4)); task_card = self.card(right, 'To-do rápido', '✅'); task_card.pack(fill='both', expand=True, pady=6); task_body = self.card_content(task_card); entry_row = tk.Frame(task_body, bg=c['card']); entry_row.pack(fill='x', pady=(0, 8)); entry_row.grid_columnconfigure(0, weight=1); entry_row.grid_columnconfigure(1, weight=0); entry_row.grid_columnconfigure(2, weight=0); self.task_entry = tk.Entry(entry_row, font=self.app_font(11), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary']); self.task_entry.grid(row=0, column=0, sticky='ew', padx=(0, 6), ipady=8); self.task_priority = tk.StringVar(value='Normal')
        ttk.Combobox(entry_row, textvariable=self.task_priority, values=['Urgente', 'Alta', 'Normal', 'Baja'], state='readonly', width=10).grid(row=0, column=1, sticky='ns', padx=(0, 6)); tk.Button(entry_row, text='Agregar', command=self.add_task, bg=c['accent'], relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').grid(row=0, column=2, sticky='ns', ipady=7); self.task_list = tk.Listbox(task_body, height=8, relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], font=self.app_font(10)); self.task_list.pack(fill='both', expand=True, pady=(0, 8)); task_buttons = tk.Frame(task_body, bg=c['card']); task_buttons.pack(fill='x')
        tk.Button(task_buttons, text='Completar', command=self.complete_task, bg='#cfe8ff', relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').pack(side='left', fill='x', expand=True, padx=4, ipady=7); tk.Button(task_buttons, text='Eliminar', command=self.delete_task, bg=c['danger'], relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').pack(side='left', fill='x', expand=True, padx=4, ipady=7); mood_card = self.card(left, 'Mood tracker pro', '🌈'); mood_card.pack(fill='x', pady=6); mood_card_body = self.card_content(mood_card); mood_top = tk.Frame(mood_card_body, bg=c['card']); mood_top.pack(fill='x', pady=(0, 6)); moods_frame = tk.Frame(mood_top, bg=c['card']); moods_frame.pack(side='left', fill='x')
        for mood in ['😊 Feliz', '🤩 Motivada', '😌 Tranquila', '😴 Cansada', '😤 Estresada', '🥺 Ansiosa', '😔 Triste']:
            tk.Button(moods_frame, text=mood.split()[0], command=lambda m=mood: self.select_mood(m), bg=c['soft'], relief='flat', width=3, font=(self.app_font_name(), 20), activebackground=c['secondary'], cursor='hand2').pack(side='left', padx=4, pady=4, ipadx=4, ipady=4)
        self.mood_label = tk.Label(mood_card_body, text='Mood actual: 😊 Feliz', bg=c['card'], fg=c['text'], font=(self.app_font_name(), 12, 'bold')); self.mood_label.pack(anchor='w', pady=4); sliders = tk.Frame(mood_top, bg=c['card']); sliders.pack(side='right', fill='x', expand=True, padx=(10, 0)); tk.Label(sliders, text='Intensidad', bg=c['card'], fg=c['text']).grid(row=0, column=0, sticky='w'); tk.Scale(sliders, from_=1, to=10, orient='horizontal', variable=self.mood_intensity_var, bg=c['card'], troughcolor='#ffd9e8', activebackground=c['primary'], highlightthickness=0, length=220).grid(row=0, column=1, sticky='ew'); tk.Label(sliders, text='Energía', bg=c['card'], fg=c['text']).grid(row=1, column=0, sticky='w')
        tk.Scale(sliders, from_=1, to=10, orient='horizontal', variable=self.mood_energy_var, bg=c['card'], troughcolor='#d6f5df', activebackground='#49d9a2', highlightthickness=0, length=220).grid(row=1, column=1, sticky='ew'); sliders.grid_columnconfigure(1, weight=1); self.mood_note = tk.Entry(mood_card_body, font=self.app_font(10), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary']); self.mood_note.pack(fill='x', pady=(4, 6), ipady=7); self.mood_note.insert(0, '¿Cómo te sientes hoy? ¿Qué pasó?'); self.mood_tags_entry = tk.Entry(mood_card_body, font=self.app_font(10), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary']); self.mood_tags_entry.pack(fill='x', pady=(0, 8), ipady=7)
        self.mood_tags_entry.insert(0, 'Tags: sueño, escuela, amigas, familia...'); mood_actions = tk.Frame(mood_card_body, bg=c['card']); mood_actions.pack(fill='x', pady=2); tk.Button(mood_actions, text='Guardar +2🍓', command=self.save_mood, bg=c['accent'], relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').pack(side='left', fill='x', expand=True, padx=4, ipady=7); tk.Button(mood_actions, text='Tendencia', command=self.show_mood_insights, bg='#cfe8ff', relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').pack(side='left', fill='x', expand=True, padx=4, ipady=7); tk.Button(mood_actions, text='Plan suave', command=self.mood_self_care_plan, bg='#e4d5ff', relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').pack(side='left', fill='x', expand=True, padx=4, ipady=7)
        mood_result = tk.Frame(mood_card_body, bg=c['card']); mood_result.pack(fill='x', pady=(4, 2)); mood_result.grid_columnconfigure(0, weight=1); mood_result.grid_columnconfigure(1, weight=1); self.mood_canvas = tk.Canvas(mood_result, height=74, bg=c['card'], highlightthickness=0); self.mood_canvas.grid(row=0, column=0, sticky='ew', padx=(0, 8)); self.mood_summary = tk.Label(mood_result, text='', bg=c['card'], fg=c['muted'], wraplength=260, justify='left', font=self.app_font(9)); self.mood_summary.grid(row=0, column=1, sticky='nsew', padx=(8, 0))


    def build_subjects_tab(self):
        c = self.palette(); main = tk.Frame(self.subjects_tab, bg=c['bg']); main.pack(fill='both', expand=True, padx=10, pady=10); main.grid_columnconfigure(0, weight=1, uniform='subjects_cols'); main.grid_columnconfigure(1, weight=1, uniform='subjects_cols'); main.grid_rowconfigure(0, weight=1); left = tk.Frame(main, bg=c['bg']); left.grid(row=0, column=0, sticky='nsew', padx=(0, 8)); right = tk.Frame(main, bg=c['bg']); right.grid(row=0, column=1, sticky='nsew', padx=(8, 0)); subjects = self.card(left, 'Ingresa tus materias', '📚'); subjects.pack(fill='both', expand=True, pady=6); subjects_body = self.card_content(subjects); form = tk.Frame(subjects_body, bg=c['card']); form.pack(fill='x', pady=(0, 8))
        self.subject_entry = tk.Entry(form, font=self.app_font(11), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary']); self.subject_entry.pack(side='left', fill='x', expand=True, padx=(0, 6), ipady=8); tk.Button(form, text='Agregar', command=self.add_subject, bg=c['accent'], relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').pack(side='left', padx=(0, 0), ipady=7); self.subject_list = tk.Listbox(subjects_body, height=12, relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], font=self.app_font(10)); self.subject_list.pack(fill='both', expand=True, pady=(0, 8)); self.subject_list.bind('<<ListboxSelect>>', lambda e: self.load_selected_subject())
        tk.Button(subjects_body, text='Eliminar materia', command=self.delete_subject, bg=c['danger'], relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').pack(fill='x', pady=(0, 4), ipady=7); grade_card = self.card(left, 'Calificaciones', '🧮'); grade_card.pack(fill='both', expand=True, pady=6); grade_body = self.card_content(grade_card); self.grade_title = tk.Label(grade_body, text='Selecciona una materia para ver sus calificaciones', bg=c['card'], fg=c['text'], font=self.app_font(11, 'bold')); self.grade_title.pack(anchor='w', pady=(0, 6)); self.subjects_summary_label = tk.Label(grade_body, text='', bg=c['soft'], fg=c['muted'], font=self.app_font(9, 'bold'), justify='left', wraplength=440, padx=10, pady=6); self.subjects_summary_label.pack(fill='x', pady=(0, 8)); gform = tk.Frame(grade_body, bg=c['card'])
        gform.pack(fill='x', pady=(0, 8)); gform.grid_columnconfigure(0, weight=2); gform.grid_columnconfigure(1, weight=1); gform.grid_columnconfigure(2, weight=1); gform.grid_columnconfigure(3, weight=0); self.grade_name_entry = tk.Entry(gform, font=self.app_font(10), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary']); self.grade_name_entry.grid(row=0, column=0, sticky='ew', padx=(0, 5), ipady=7); self.grade_name_entry.insert(0, 'Actividad'); self.grade_value_entry = tk.Entry(gform, font=self.app_font(10), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary'], justify='center'); self.grade_value_entry.grid(row=0, column=1, sticky='ew', padx=5, ipady=7); self.grade_value_entry.insert(0, '5.0')
        self.grade_weight_entry = tk.Entry(gform, font=self.app_font(10), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary'], justify='center'); self.grade_weight_entry.grid(row=0, column=2, sticky='ew', padx=5, ipady=7); self.grade_weight_entry.insert(0, '%'); tk.Button(gform, text='Agregar', command=self.add_grade, bg=c['accent'], relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').grid(row=0, column=3, sticky='ns', padx=(5, 0), ipady=7); self.grade_list = ttk.Treeview(grade_body, columns=('name', 'value', 'weight'), show='headings', height=7); self.grade_list.heading('name', text='Actividad'); self.grade_list.heading('value', text='Nota'); self.grade_list.heading('weight', text='%'); self.grade_list.column('name', width=170, anchor='w')
        self.grade_list.column('value', width=70, anchor='center'); self.grade_list.column('weight', width=70, anchor='center'); self.grade_list.pack(fill='both', expand=True, pady=(0, 6)); tk.Button(grade_body, text='Eliminar nota', command=self.delete_grade, bg=c['danger'], relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').pack(fill='x', pady=4, ipady=7); self.grade_average = tk.Label(grade_body, text='', bg=c['card'], fg=c['primary'], font=self.app_font(11, 'bold')); self.grade_average.pack(anchor='center', pady=4); notes = self.card(right, 'Apuntes y archivos', '📝'); notes.pack(fill='both', expand=True, pady=6); notes_body = self.card_content(notes); self.notes_title = tk.Label(notes_body, text='Selecciona o crea una materia', bg=c['card'], fg=c['text'], font=self.app_font(11, 'bold'))
        self.notes_title.pack(anchor='w', pady=(0, 6)); self.subject_notes_text = tk.Text(notes_body, wrap='word', height=8, font=self.app_font(10), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary'], padx=10, pady=8); self.subject_notes_text.pack(fill='both', expand=True, pady=(0, 8)); btns = tk.Frame(notes_body, bg=c['card']); btns.pack(fill='x', pady=(0, 8)); tk.Button(btns, text='Guardar apuntes', command=self.save_subject_notes, bg=c['accent'], relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').pack(side='left', fill='x', expand=True, padx=(0, 4), ipady=7); tk.Button(btns, text='Subir archivo', command=self.add_subject_file, bg='#cfe8ff', relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').pack(side='left', fill='x', expand=True, padx=(4, 0), ipady=7)
        self.subject_files_list = tk.Listbox(notes_body, height=4, relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], font=self.app_font(10)); self.subject_files_list.pack(fill='x', pady=(0, 8)); file_btns = tk.Frame(notes_body, bg=c['card']); file_btns.pack(fill='x'); tk.Button(file_btns, text='Abrir archivo', command=self.open_subject_file, bg='#e4d5ff', relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').pack(side='left', fill='x', expand=True, padx=(0, 4), ipady=7); tk.Button(file_btns, text='Quitar archivo', command=self.delete_subject_file, bg=c['danger'], relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').pack(side='left', fill='x', expand=True, padx=(4, 0), ipady=7); flash = self.card(right, 'Flashcards pro con repaso', '🃏'); flash.pack(fill='both', expand=True, pady=6)
        flash_body = self.card_content(flash); flash_form = tk.Frame(flash_body, bg=c['card']); flash_form.pack(fill='x', pady=(0, 8)); flash_form.grid_columnconfigure(0, weight=1); flash_form.grid_columnconfigure(1, weight=1); flash_form.grid_columnconfigure(2, weight=0); self.flash_q_entry = tk.Entry(flash_form, font=self.app_font(10), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary']); self.flash_q_entry.grid(row=0, column=0, sticky='ew', padx=(0, 4), ipady=7); self.flash_q_entry.insert(0, 'Pregunta'); self.flash_a_entry = tk.Entry(flash_form, font=self.app_font(10), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary']); self.flash_a_entry.grid(row=0, column=1, sticky='ew', padx=4, ipady=7); self.flash_a_entry.insert(0, 'Respuesta')
        tk.Button(flash_form, text='Agregar', command=self.add_flashcard, bg=c['accent'], relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').grid(row=0, column=2, sticky='ns', padx=(4, 0), ipady=7); flash_meta = tk.Frame(flash_body, bg=c['card']); flash_meta.pack(fill='x', pady=(0, 8)); flash_meta.grid_columnconfigure(1, weight=1); ttk.Combobox(flash_meta, textvariable=self.flash_difficulty_var, values=['Fácil', 'Normal', 'Difícil'], state='readonly', width=9).grid(row=0, column=0, sticky='ns', padx=(0, 4)); self.flash_tags_entry = tk.Entry(flash_meta, font=self.app_font(10), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary']); self.flash_tags_entry.grid(row=0, column=1, sticky='ew', padx=4, ipady=7); self.flash_tags_entry.insert(0, 'Tags: examen, vocabulario...')
        ttk.Combobox(flash_meta, textvariable=self.flash_filter_var, values=['Todas', 'Para hoy', 'Favoritas', 'Difíciles'], state='readonly', width=10).grid(row=0, column=2, sticky='ns', padx=4); tk.Button(flash_meta, text='Filtrar', command=self.load_selected_subject, bg='#fff1b8', relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').grid(row=0, column=3, sticky='ns', padx=(4, 0), ipady=7); self.flash_stats_label = tk.Label(flash_body, text='', bg=c['card'], fg=c['muted'], justify='left'); self.flash_stats_label.pack(anchor='w', pady=2); self.flash_list = tk.Listbox(flash_body, height=6, relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], font=self.app_font(10)); self.flash_list.pack(fill='both', expand=True, pady=(0, 8)); fbtns = tk.Frame(flash_body, bg=c['card']); fbtns.pack(fill='x')
        for col in range(5):
            fbtns.grid_columnconfigure(col, weight=1, uniform='flash_buttons')
        tk.Button(fbtns, text='Practicar', command=self.practice_flashcards, bg='#cfe8ff', relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').grid(row=0, column=0, sticky='ew', padx=(0, 3), ipady=7); tk.Button(fbtns, text='Hoy', command=lambda: self.practice_flashcards(only_due=True), bg='#d6f5df', relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').grid(row=0, column=1, sticky='ew', padx=3, ipady=7); tk.Button(fbtns, text='Editar', command=self.edit_flashcard, bg='#fff1b8', relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').grid(row=0, column=2, sticky='ew', padx=3, ipady=7); tk.Button(fbtns, text='Auto', command=self.auto_flashcards_from_notes, bg='#e4d5ff', relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').grid(row=0, column=3, sticky='ew', padx=3, ipady=7)
        tk.Button(fbtns, text='Eliminar', command=self.delete_flashcard, bg=c['danger'], relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2').grid(row=0, column=4, sticky='ew', padx=(3, 0), ipady=7)

    def app_font_name(self):
        if self.user_data:
            return self.user_data.get('profile', {}).get('app_font', 'Segoe UI')
        return 'Segoe UI'

    def app_font(self, size=10, weight=None):
        if weight:
            return (self.app_font_name(), size, weight)
        return (self.app_font_name(), size)


    def apply_fonts_to_widgets(self, parent=None):
        parent = parent or self.root; mood_emojis = ['😊', '🤩', '😌', '😴', '😤', '🥺', '😔']
        for widget in parent.winfo_children():
            try:
                widget_class = widget.winfo_class()
                if widget_class == 'Button':
                    text = widget.cget('text').strip()
                    if text in mood_emojis:
                        widget.configure(font=self.app_font(20))
                    else:
                        widget.configure(font=self.app_font(10, 'bold'))
                elif widget_class == 'Label':
                    if widget is getattr(self, 'timer_label', None):
                        widget.configure(font=('Consolas', 88, 'bold'))
                    elif getattr(widget, 'michi_card_title', False):
                        widget.configure(font=self.app_font(15, 'bold'))
                    else:
                        current = str(widget.cget('font'))
                        if 'bold' in current:
                            widget.configure(font=self.app_font(10, 'bold'))
                        else:
                            widget.configure(font=self.app_font(10))
                elif widget_class in ('Entry', 'Text', 'Listbox'):
                    widget.configure(font=self.app_font(10))
                elif widget_class == 'Checkbutton':
                    widget.configure(font=self.app_font(10))
            except Exception:
                pass
            self.apply_fonts_to_widgets(widget)



    def build_settings_tab(self):
        c = self.palette(); main = tk.Frame(self.settings_tab, bg=c['bg']); main.pack(fill='both', expand=True, padx=10, pady=10); left = tk.Frame(main, bg=c['bg']); left.pack(side='left', fill='both', expand=True, padx=8); right = tk.Frame(main, bg=c['bg']); right.pack(side='right', fill='both', expand=True, padx=8); themes = self.card(left, 'Temas personalizables', '🎨'); themes.pack(fill='x', pady=6); self.theme_variant = tk.StringVar(value=self.user_data['profile'].get('theme_variant', 'strawberry')); ttk.Combobox(themes, textvariable=self.theme_variant, values=['strawberry', 'lavender', 'mint', 'custom'], state='readonly').pack(fill='x', pady=4); tk.Label(themes, text='Tipografía de la app', bg=c['card'], fg=c['text'], font=(self.app_font_name(), 10, 'bold')).pack(anchor='w', pady=(8, 2))
        self.font_var = tk.StringVar(value=self.user_data['profile'].get('app_font', 'Segoe UI')); ttk.Combobox(themes, textvariable=self.font_var, values=APP_FONTS, state='readonly').pack(fill='x', pady=4); tk.Button(themes, text='Aplicar tipografía', command=self.apply_app_font, bg='#ffd9e8').pack(fill='x', pady=3); tk.Button(themes, text='Aplicar tema', command=self.apply_theme_variant, bg=c['accent']).pack(fill='x', pady=3); tk.Button(themes, text='Color principal personalizado', command=self.choose_primary_color, bg='#cfe8ff').pack(fill='x', pady=3); tk.Button(themes, text='Color de fondo personalizado', command=self.choose_bg_color, bg='#e4d5ff').pack(fill='x', pady=3); tk.Button(themes, text='Alternar claro / nocturno', command=self.toggle_dark_mode, bg='#fff1b8').pack(fill='x', pady=3); media = self.card(left, 'Conexiones y accesos', '🎧')
        media.pack(fill='x', pady=6); tk.Label(media, text='Spotify URL', bg=c['card'], fg=c['text']).pack(anchor='w'); self.spotify_entry = tk.Entry(media); self.spotify_entry.pack(fill='x', pady=3); self.spotify_entry.insert(0, self.user_data['profile'].get('spotify_url', 'https://open.spotify.com')); tk.Label(media, text='YouTube URL', bg=c['card'], fg=c['text']).pack(anchor='w'); self.youtube_entry = tk.Entry(media); self.youtube_entry.pack(fill='x', pady=3); self.youtube_entry.insert(0, self.user_data['profile'].get('youtube_url', 'https://www.youtube.com')); tk.Button(media, text='Guardar enlaces', command=self.save_media_links, bg=c['accent']).pack(fill='x', pady=3); opt = self.card(right, 'Acciones de optimización', '⚡'); opt.pack(fill='x', pady=6)
        tk.Button(opt, text='Optimizar datos ahora', command=self.optimize_user_data, bg=c['accent']).pack(fill='x', pady=3); tk.Button(opt, text='Crear backup rápido', command=self.create_quick_backup, bg='#cfe8ff').pack(fill='x', pady=3); tk.Button(opt, text='Importar backup', command=self.import_backup, bg='#e4d5ff').pack(fill='x', pady=3); pro = self.card(right, 'Inicio Pro y centro de control', '🎛'); pro.pack(fill='both', expand=True, pady=6); self.pro_home_var = tk.BooleanVar(value=self.user_data['settings'].get('pro_home', True)); self.animations_var = tk.BooleanVar(value=self.user_data['settings'].get('animations', True)); self.auto_opt_var = tk.BooleanVar(value=self.user_data['settings'].get('auto_optimize', True))
        for text, var in [('Inicio Pro activado', self.pro_home_var), ('Animaciones del michi', self.animations_var), ('Auto optimización', self.auto_opt_var)]:
            tk.Checkbutton(pro, text=text, variable=var, bg=c['card'], fg=c['text'], selectcolor=c['soft'], command=self.save_settings_toggles).pack(anchor='w', pady=2)
        self.control_text = tk.Text(pro, height=15, wrap='word'); self.control_text.pack(fill='both', expand=True, pady=5); tk.Button(pro, text='Actualizar centro de control', command=self.refresh_control_center, bg=c['accent']).pack(fill='x', pady=3)

    def refresh_all(self):
        self.refresh_header(); self.refresh_pet(); self.refresh_level(); self.refresh_tasks(); self.refresh_moods(); self.refresh_pomodoro(); self.refresh_subjects(); self.refresh_library(); self.refresh_shop(); self.refresh_inventory(); self.refresh_control_center(); self.refresh_game_status(); self.refresh_focus_tip()

    def refresh_header(self):
        c = self.user_data['currency']; self.header_status.config(text=f"{self.current_user} | 🍓 {c['fresas']} | Nivel {c['level']} | XP {c['xp']}/100")

    def refresh_level(self):
        cur = self.user_data['currency']; self.level_label.config(text=f"⭐ Nivel {cur['level']}   XP {cur['xp']}/100")
        for widget in self.level_holder.winfo_children():
            widget.destroy()
        self.progress_bar(self.level_holder, cur['xp'], 100)

    def pet_state(self):
        pet = self.user_data['pet']
        if pet.get('hunger', 0) >= 75:
            return 'hambriento'
        if pet.get('energy', 0) <= 25:
            return 'cansado'
        if pet.get('happiness', 0) <= 30:
            return 'triste'
        if self.timer.running and self.timer.mode == 'study':
            return 'estudiando'
        if pet.get('happiness', 0) >= 90:
            return 'feliz'
        return 'tranquilo'

    def refresh_pet(self):
        if not self.user_data:
            return
        pet = self.user_data['pet']; state = self.pet_state(); self.draw_cat(self.home_pet_canvas, pet, studying=state == 'estudiando'); self.draw_cat(self.study_pet_canvas, pet, studying=self.timer.mode == 'study' and self.timer.running); self.pet_info.config(text=f"🐱 {pet['name']} · 👗 {pet.get('outfit', 'Vestido fresa')} · 🎀 {pet.get('accessory', 'Ninguno')}\n⚡ {pet['energy']}% · 💖 {pet['happiness']}% · 🍓 {pet['hunger']}% · ⭐ Nv.{pet['level']} · XP {pet['xp']}/100")
        messages = {'estudiando': 'Tu michi está estudiando contigo con su libro en el pomodoro 📚', 'hambriento': 'Tu michi tiene hambre. Un snack o unas fresitas le caerían bien 🍓', 'cansado': 'Está cansadito. Dale un descanso para recuperar energía 💤', 'triste': 'Quiere jugar o un accesorio nuevo para animarse 🥺', 'feliz': 'Tu michi está adorable y súper feliz hoy ✨', 'tranquilo': 'Todo va bien. Haz una tarea pequeña y suma progreso 🌸'}; self.pet_speech.config(text=messages.get(state, 'Tu michi te acompaña.'))

    def refresh_tasks(self):
        self.task_list.delete(0, tk.END); tasks = self.user_data.get('tasks', [])
        if not tasks:
            self.task_list.insert(tk.END, 'No tienes tareas. Agrega una arriba ✨'); return
        order = {'Urgente': 0, 'Alta': 1, 'Normal': 2, 'Baja': 3}
        for task in sorted(tasks, key=lambda t: (t.get('done', False), order.get(t.get('priority', 'Normal'), 2))):
            status = '✅' if task.get('done') else '⬜'; self.task_list.insert(tk.END, f"{status} [{task.get('priority', 'Normal')}] {task.get('text', '')}")


    def mood_score(self, mood_entry):
        mood = mood_entry.get('mood', '') if isinstance(mood_entry, dict) else str(mood_entry); base = 6
        if 'Motivada' in mood or 'Feliz' in mood:
            base = 8
        elif 'Tranquila' in mood:
            base = 7
        elif 'Cansada' in mood:
            base = 5
        elif 'Estresada' in mood or 'Ansiosa' in mood:
            base = 4
        elif 'Triste' in mood:
            base = 3
        intensity = safe_int(mood_entry.get('intensity', 7), 7) if isinstance(mood_entry, dict) else 7; energy = safe_int(mood_entry.get('energy', 6), 6) if isinstance(mood_entry, dict) else 6; return clamp(round(base * 0.65 + energy * 0.2 + intensity * 0.15), 1, 10)


    def mood_recommendation(self, entry):
        mood = entry.get('mood', ''); energy = safe_int(entry.get('energy', 6), 6); intensity = safe_int(entry.get('intensity', 7), 7)
        if 'Ansiosa' in mood or 'Estresada' in mood:
            return 'Michi sugiere: 3 respiraciones lentas, dividir la tarea en 1 paso de 10 minutos y poner música suave.'
        if 'Cansada' in mood or energy <= 3:
            return 'Michi sugiere: descanso corto, agua, estirarte y hacer solo una tarea ligera antes de seguir.'
        if 'Triste' in mood:
            return 'Michi sugiere: escribir qué necesitas, hablar con alguien de confianza y elegir una meta pequeñita.'
        if 'Motivada' in mood or 'Feliz' in mood or intensity >= 8:
            return 'Michi sugiere: aprovecha para estudiar lo más difícil o repasar flashcards pendientes.'
        return 'Michi sugiere: mantén el ritmo con una sesión corta y recompensa al terminar.'

    def show_mood_insights(self):
        moods = self.user_data.get('moods', [])
        if not moods:
            messagebox.showinfo('Mood', 'Aún no hay moods para analizar.'); return
        last = moods[-14:]; avg = sum((self.mood_score(m) for m in last)) / len(last); common_tags = {}
        for m in last:
            for tag in str(m.get('tags', '')).replace(',', ' ').split():
                common_tags[tag.lower()] = common_tags.get(tag.lower(), 0) + 1
        tags = ', '.join([k for k, _ in sorted(common_tags.items(), key=lambda x: x[1], reverse=True)[:5]]) or 'sin tags aún'; best = max(last, key=self.mood_score); low = min(last, key=self.mood_score); text = f"Resumen de tus últimos {len(last)} registros:\n\n• Promedio emocional: {avg:.1f}/10\n• Tags más repetidos: {tags}\n• Mejor registro: {best.get('date', '')[:10]} · {best.get('mood', '')}\n• Registro más bajo: {low.get('date', '')[:10]} · {low.get('mood', '')}\n\nTip: usa tags simples para descubrir patrones: sueño, examen, comida, amigas, familia, ejercicio."; messagebox.showinfo('Tendencia de mood', text)

    def mood_self_care_plan(self):
        entry = {'mood': self.quick_mood.get(), 'energy': self.mood_energy_var.get(), 'intensity': self.mood_intensity_var.get()}; plan = self.mood_recommendation(entry) + '\n\nPlan de 15 minutos:\n1) 2 min respirar y tomar agua.\n2) 8 min hacer una sola micro-tarea.\n3) 3 min ordenar escritorio.\n4) 2 min marcar progreso y darle cariño a Michi.'; messagebox.showinfo('Plan suave de Michi', plan)

    def refresh_pomodoro(self):
        p = self.user_data['pomodoro']
        for entry, value in [(self.study_entry, p['study_minutes']), (self.break_entry, p['break_minutes']), (self.long_break_entry, p['long_break_minutes'])]:
            entry.delete(0, tk.END); entry.insert(0, str(value))
        self.update_timer_label(self.timer.seconds_left); self.study_plan_text.delete('1.0', tk.END); self.study_plan_text.insert('1.0', self.user_data.get('study_plan', '')); self.scratch_text.delete('1.0', tk.END); self.scratch_text.insert('1.0', self.user_data.get('quick_scratch', ''))

    def refresh_subjects(self):
        self.subject_list.delete(0, tk.END); self._subject_order = sorted(self.user_data.get('subjects', {}).keys()); summary_parts = []
        for subject in self._subject_order:
            grades = self.subject_data(subject).get('grades', []); avg = self.calculate_average(grades); total_weight = sum((safe_float(g.get('weight', 0), 0.0) for g in grades)); suffix = f' · promedio {avg:.2f} · {total_weight:.0f}%' if grades else ''; self.subject_list.insert(tk.END, f'📚 {subject}{suffix}'); summary_parts.append(f'{subject}: {avg:.2f}' if grades else f'{subject}: sin notas')
        if hasattr(self, 'subjects_summary_label'):
            self.subjects_summary_label.config(text='Resumen: ' + '  ·  '.join(summary_parts[:4]) if summary_parts else 'Resumen: agrega materias y notas para ver promedios.')
        if self._subject_order:
            if not self.subject_list.curselection():
                self.subject_list.selection_set(0)
            self.load_selected_subject()
        else:
            self.notes_title.config(text='Selecciona o crea una materia'); self.subject_notes_text.delete('1.0', tk.END)
            if hasattr(self.grade_list, 'get_children'):
                for item in self.grade_list.get_children():
                    self.grade_list.delete(item)
            else:
                self.grade_list.delete(0, tk.END)
            if hasattr(self, 'grade_title'):
                self.grade_title.config(text='Selecciona una materia para ver sus calificaciones')
            self.grade_average.config(text=''); self.subject_files_list.delete(0, tk.END); self.flash_list.delete(0, tk.END)

    def refresh_library(self):
        self.library_list.delete(0, tk.END); self._library_index_map = list(self.user_data.get('library', []))
        if not self._library_index_map:
            self.library_list.insert(tk.END, 'Tu biblioteca está vacía. Agrega recursos 📚'); self.library_detail.delete('1.0', tk.END); self.library_detail.insert('1.0', 'Aquí puedes guardar libros, enlaces, PDFs, apuntes y cualquier recurso útil para estudiar.'); return
        for item in self._library_index_map:
            status = '✅' if item.get('done') else '📌'; self.library_list.insert(tk.END, f"{status} {item.get('title', 'Recurso')} · {item.get('type', 'recurso')}")
        if not self.library_list.curselection():
            self.library_list.selection_set(0)
        self.preview_library_item()



    def refresh_control_center(self):
        metrics = self.user_data.get('metrics', {}); cur = self.user_data.get('currency', {}); pending = len([t for t in self.user_data.get('tasks', []) if not t.get('done')]); subjects = len(self.user_data.get('subjects', {})); resources = len(self.user_data.get('library', []))
        text = f"CENTRO DE CONTROL\n\nUsuario: {self.current_user}\nFresas: {cur.get('fresas', 0)}\nNivel: {cur.get('level', 1)} · XP: {cur.get('xp', 0)}/100\nTareas pendientes: {pending}\nPomodoros completados: {metrics.get('pomodoros_completed', 0)}\nMoods registrados: {metrics.get('moods_registered', 0)}\nMinijuegos ganados: {metrics.get('mini_games_won', 0)}\nRacha de estudio: {metrics.get('study_streak', 0)} días\nMaterias: {subjects}\nRecursos en biblioteca: {resources}\nÚltima optimización: {metrics.get('last_optimized', 'Nunca')}\n\nMichi Studio reúne organización, estudio y personalización del gatito en menos pestañas y con más funciones útiles."; self.control_text.delete('1.0', tk.END); self.control_text.insert('1.0', text)


    def refresh_focus_tip(self):
        mood = self.quick_mood.get()
        if 'Cansada' in mood:
            tip = 'Tip: si estás cansada, prueba un bloque de 15-20 minutos y una tarea sencilla primero.'
        elif 'Ansiosa' in mood or 'Estresada' in mood:
            tip = 'Tip: elige 1 sola materia, anota 3 mini pasos y hazlos uno por uno.'
        elif 'Motivada' in mood or 'Feliz' in mood:
            tip = 'Tip: estás en buen momento para avanzar la tarea más difícil o practicar flashcards.'
        else:
            tip = 'Tip: usa Pomodoro + to-do + biblioteca personal para mantener tu estudio ordenado.'
        self.focus_tip.config(text=tip)

    def add_rewards(self, fresas=0, xp=0, pet_xp=0):
        cur = self.user_data['currency']; cur['fresas'] += fresas; cur['xp'] += xp
        while cur['xp'] >= 100:
            cur['xp'] -= 100; cur['level'] += 1; self.add_achievement(f"Subiste al nivel {cur['level']} ⭐")
        if pet_xp:
            pet = self.user_data['pet']; pet['xp'] += pet_xp
            while pet['xp'] >= 100:
                pet['xp'] -= 100; pet['level'] += 1; pet['happiness'] = 100; self.add_achievement(f"{pet['name']} subió al nivel {pet['level']} 🐾")
        self.save()

    def add_achievement(self, text):
        achievements = self.user_data.setdefault('achievements', [])
        if text not in achievements:
            achievements.append(text)

    def update_streak(self):
        metrics = self.user_data['metrics']; today = today_string(); last = metrics.get('last_study_day', '')
        if last == today:
            return
        if not last:
            metrics['study_streak'] = 1
        else:
            try:
                last_date = datetime.strptime(last, '%Y-%m-%d').date(); metrics['study_streak'] = metrics.get('study_streak', 0) + 1 if (date.today() - last_date).days == 1 else 1
            except Exception:
                metrics['study_streak'] = 1
        metrics['last_study_day'] = today

    def feed_pet(self):
        if self.user_data['currency']['fresas'] < 10:
            messagebox.showerror('Mascota', 'Necesitas 10 fresas para alimentarlo.'); return
        self.user_data['currency']['fresas'] -= 10; pet = self.user_data['pet']; pet['hunger'] = clamp(pet['hunger'] - 30); pet['happiness'] = clamp(pet['happiness'] + 8); self.save(); self.refresh_all()

    def play_pet(self):
        pet = self.user_data['pet']
        if pet['energy'] < 12:
            messagebox.showinfo('Mascota', 'Tu michi está cansado. Mejor déjalo descansar.'); return
        pet['energy'] = clamp(pet['energy'] - 10); pet['happiness'] = clamp(pet['happiness'] + 15); pet['hunger'] = clamp(pet['hunger'] + 7); self.add_rewards(fresas=3, xp=4, pet_xp=6); self.refresh_all()

    def rest_pet(self):
        pet = self.user_data['pet']; pet['energy'] = clamp(pet['energy'] + 24); pet['hunger'] = clamp(pet['hunger'] + 3); self.save(); self.refresh_all()

    def customize_pet(self):
        win = tk.Toplevel(self.root); win.title('Personalizar michi'); win.geometry('430x520'); c = self.palette(); win.configure(bg=c['bg']); tk.Label(win, text='Personalización de tu michi', bg=c['bg'], fg=c['primary'], font=('Arial', 16, 'bold')).pack(pady=10); preview = tk.Canvas(win, width=220, height=270, bg=c['card'], highlightthickness=0); preview.pack(pady=4); name = tk.Entry(win); name.pack(fill='x', padx=20, pady=3); name.insert(0, self.user_data['pet'].get('name', 'Michi'))
        vars_map = {'base_color': tk.StringVar(value=self.user_data['pet'].get('base_color', 'Crema')), 'hood_color': tk.StringVar(value=self.user_data['pet'].get('hood_color', 'Rojo fresa')), 'dress_color': tk.StringVar(value=self.user_data['pet'].get('dress_color', 'Rojo fresa')), 'accessory': tk.StringVar(value=self.user_data['pet'].get('accessory', 'Moño verde')), 'outfit': tk.StringVar(value=self.user_data['pet'].get('outfit', 'Vestido fresa')), 'personality': tk.StringVar(value=self.user_data['pet'].get('personality', 'Dulce')), 'expression': tk.StringVar(value=self.user_data['pet'].get('expression', 'Alegre'))}
        options = {'Color base': (vars_map['base_color'], ['Crema', 'Rosado', 'Gris', 'Canela', 'Blanco']), 'Color capucha': (vars_map['hood_color'], ['Rojo fresa', 'Rosa chicle', 'Lavanda', 'Menta', 'Azul cielo', 'Vainilla']), 'Color vestido': (vars_map['dress_color'], ['Rojo fresa', 'Rosa chicle', 'Lavanda', 'Menta', 'Azul cielo', 'Vainilla']), 'Accesorio': (vars_map['accessory'], ['Moño verde', 'Moño rosa', 'Corona', 'Lentes', 'Estrellita', 'Libro mini', 'Ninguno']), 'Vestido': (vars_map['outfit'], ['Vestido fresa', 'Vestido lavanda', 'Vestido menta', 'Vestido cielo', 'Vestido vainilla']), 'Personalidad': (vars_map['personality'], ['Dulce', 'Estudiosa', 'Traviesa', 'Dormilona', 'Elegante']), 'Expresión': (vars_map['expression'], ['Alegre', 'Guiño', 'Enfocado', 'Dormido'])}
        for label, (var, values) in options.items():
            tk.Label(win, text=label, bg=c['bg'], fg=c['text']).pack(anchor='w', padx=20); box = ttk.Combobox(win, textvariable=var, values=values, state='readonly'); box.pack(fill='x', padx=20, pady=2); box.bind('<<ComboboxSelected>>', lambda e: redraw())

        def preview_pet_data():
            return {**self.user_data['pet'], 'name': name.get().strip() or self.user_data['pet'].get('name', 'Michi'), **{k: v.get() for k, v in vars_map.items()}}

        def redraw():
            self.draw_cat(preview, pet=preview_pet_data(), studying=False)
        redraw()

        def save_pet():
            if name.get().strip():
                self.user_data['pet']['name'] = name.get().strip()
            for key, var in vars_map.items():
                self.user_data['pet'][key] = var.get()
            self.save(); self.refresh_all(); win.destroy()
        tk.Button(win, text='Guardar cambios', command=save_pet, bg=c['accent']).pack(fill='x', padx=20, pady=14)

    def add_task(self):
        text = self.task_entry.get().strip()
        if not text:
            messagebox.showerror('Tareas', 'Escribe una tarea.'); return
        self.user_data['tasks'].append({'text': text, 'priority': self.task_priority.get(), 'done': False, 'created_at': now_string()}); self.task_entry.delete(0, tk.END); self.save(); self.refresh_all()

    def displayed_task_to_index(self):
        sel = self.task_list.curselection()
        if not sel:
            return None
        visible = self.task_list.get(sel[0])
        if visible.startswith('No tienes'):
            return None
        text = visible.split('] ', 1)[-1] if '] ' in visible else visible
        for i, task in enumerate(self.user_data['tasks']):
            if task.get('text') == text:
                return i
        return None

    def complete_task(self):
        idx = self.displayed_task_to_index()
        if idx is None:
            messagebox.showerror('Tareas', 'Selecciona una tarea.'); return
        task = self.user_data['tasks'][idx]
        if task.get('done'):
            messagebox.showinfo('Tareas', 'Esa tarea ya está completada.'); return
        task['done'] = True; self.user_data['metrics']['tasks_completed'] += 1; self.add_rewards(fresas=15, xp=20, pet_xp=10); self.refresh_all(); messagebox.showinfo('Tareas', 'Tarea completada. +15 fresas, +20 XP.')

    def delete_task(self):
        idx = self.displayed_task_to_index()
        if idx is None:
            messagebox.showerror('Tareas', 'Selecciona una tarea.'); return
        if messagebox.askyesno('Tareas', '¿Eliminar esta tarea?'):
            del self.user_data['tasks'][idx]; self.save(); self.refresh_all()

    def select_mood(self, mood):
        self.quick_mood.set(mood); self.mood_label.config(text=f'Mood actual: {mood}'); self.refresh_focus_tip(); pet = self.user_data['pet']
        if 'Cansada' in mood:
            pet['expression'] = 'Dormido'; self.mood_energy_var.set(3); self.pet_speech.config(text='Está bien bajar el ritmo. Prueba un Pomodoro cortito 😴')
        elif 'Ansiosa' in mood or 'Estresada' in mood:
            pet['expression'] = 'Enfocado'; self.mood_energy_var.set(4); self.pet_speech.config(text='Divide tu tarea en pasos mini y respira profundo 🧘')
        elif 'Triste' in mood:
            pet['expression'] = 'Tímido'; self.mood_energy_var.set(3); self.pet_speech.config(text='Michi se queda cerquita. Hagamos una meta pequeñita 🥺')
        elif 'Motivada' in mood or 'Feliz' in mood:
            pet['expression'] = 'Alegre'; self.mood_energy_var.set(8); self.pet_speech.config(text='¡Aprovecha la energía! Es buen momento para avanzar mucho ✨')
        self.refresh_pet()

    def save_mood(self):
        note = self.mood_note.get().strip()
        if note.startswith('¿Cómo te sientes') or note == 'Guardado ✨':
            note = ''
        tags = self.mood_tags_entry.get().strip() if hasattr(self, 'mood_tags_entry') else ''
        if tags.startswith('Tags:'):
            tags = ''
        entry = {'date': now_string(), 'mood': self.quick_mood.get(), 'note': note, 'intensity': safe_int(self.mood_intensity_var.get(), 7), 'energy': safe_int(self.mood_energy_var.get(), 6), 'tags': tags, 'recommendation': self.mood_recommendation({'mood': self.quick_mood.get(), 'energy': self.mood_energy_var.get(), 'intensity': self.mood_intensity_var.get()})}; self.user_data['moods'].append(entry); self.user_data['metrics']['moods_registered'] += 1; self.user_data['pet']['happiness'] = clamp(self.user_data['pet']['happiness'] + 3); self.mood_note.delete(0, tk.END); self.mood_note.insert(0, 'Guardado ✨')
        if hasattr(self, 'mood_tags_entry'):
            self.mood_tags_entry.delete(0, tk.END); self.mood_tags_entry.insert(0, 'Tags: sueño, escuela, amigas, familia...')
        self.add_rewards(fresas=2, xp=3, pet_xp=2); self.save(); self.refresh_all()

    def save_pomodoro_settings(self):
        study = safe_int(self.study_entry.get(), 25); short = safe_int(self.break_entry.get(), 5); long = safe_int(self.long_break_entry.get(), 15)
        if study <= 0 or short <= 0 or long <= 0:
            messagebox.showerror('Pomodoro', 'Los tiempos deben ser mayores que cero.'); return
        self.user_data['pomodoro'].update({'study_minutes': min(study, 180), 'break_minutes': min(short, 60), 'long_break_minutes': min(long, 120)}); self.timer.reset(self.root, self.user_data['pomodoro']['study_minutes'], 'study'); self.save(); self.refresh_all()

    def start_study_timer(self):
        self.timer.configure(self.user_data['pomodoro']['study_minutes'], 'study'); self.timer.start(self.root, self.update_timer_label, self.finish_timer); self.refresh_pet()

    def start_break_timer(self):
        self.timer.configure(self.user_data['pomodoro']['break_minutes'], 'break'); self.timer.start(self.root, self.update_timer_label, self.finish_timer); self.refresh_pet()

    def start_long_break_timer(self):
        self.timer.configure(self.user_data['pomodoro']['long_break_minutes'], 'long_break'); self.timer.start(self.root, self.update_timer_label, self.finish_timer); self.refresh_pet()

    def pause_timer(self):
        self.timer.pause(self.root); self.refresh_pet()

    def reset_timer(self):
        self.timer.reset(self.root, self.user_data['pomodoro']['study_minutes'], 'study'); self.update_timer_label(self.timer.seconds_left); self.refresh_pet()

    def update_timer_label(self, seconds):
        minutes, secs = divmod(max(0, int(seconds)), 60); self.timer_label.config(text=f'{minutes:02d}:{secs:02d}')

    def finish_timer(self, mode):
        pet = self.user_data['pet']
        if mode == 'study':
            self.user_data['metrics']['pomodoros_completed'] += 1; self.user_data['pomodoro']['completed_today'] += 1; self.update_streak(); pet['energy'] = clamp(pet['energy'] - 8); pet['hunger'] = clamp(pet['hunger'] + 7); pet['happiness'] = clamp(pet['happiness'] + 5); self.add_rewards(fresas=20, xp=35, pet_xp=25); messagebox.showinfo('Pomodoro', '¡Pomodoro completado! +20 fresas y +35 XP.')
        else:
            pet['energy'] = clamp(pet['energy'] + (25 if mode == 'long_break' else 12)); messagebox.showinfo('Descanso', 'Descanso terminado.')
        self.reset_timer(); self.save(); self.refresh_all()

    def save_study_plan(self):
        self.user_data['study_plan'] = self.study_plan_text.get('1.0', tk.END).strip(); self.save(); messagebox.showinfo('Plan', 'Plan de estudio guardado.')

    def save_quick_scratch(self):
        self.user_data['quick_scratch'] = self.scratch_text.get('1.0', tk.END).strip(); self.save(); messagebox.showinfo('Bloc', 'Notas rápidas guardadas.')

    def subject_data(self, subject):
        if subject not in self.user_data['subjects']:
            self.user_data['subjects'][subject] = {'notes': '', 'grades': [], 'files': [], 'flashcards': []}
        return self.user_data['subjects'][subject]

    def selected_subject(self):
        sel = self.subject_list.curselection()
        if not sel or sel[0] >= len(self._subject_order):
            return None
        return self._subject_order[sel[0]]

    def add_subject(self):
        subject = self.subject_entry.get().strip()
        if not subject:
            messagebox.showerror('Materia', 'Escribe el nombre de la materia.'); return
        if subject in self.user_data['subjects']:
            messagebox.showinfo('Materia', 'Esa materia ya existe.'); return
        self.user_data['subjects'][subject] = {'notes': '', 'grades': [], 'files': [], 'flashcards': []}; self.subject_entry.delete(0, tk.END); self.save(); self.refresh_subjects()

    def delete_subject(self):
        subject = self.selected_subject()
        if not subject:
            messagebox.showerror('Materia', 'Selecciona una materia.'); return
        if messagebox.askyesno('Materia', f'¿Eliminar {subject}?'):
            self.user_data['subjects'].pop(subject, None); self.save(); self.refresh_subjects()

    def load_selected_subject(self):
        subject = self.selected_subject()
        if not subject:
            return
        data = self.subject_data(subject); self.notes_title.config(text=f'Apuntes de {subject}')
        if hasattr(self, 'grade_title'):
            self.grade_title.config(text=f'Calificaciones de {subject}')
        self.subject_notes_text.delete('1.0', tk.END); self.subject_notes_text.insert('1.0', data.get('notes', ''))
        for item in self.grade_list.get_children():
            self.grade_list.delete(item)
        for g in data.get('grades', []):
            self.grade_list.insert('', tk.END, values=(g.get('name', 'Nota'), g.get('value', 0), f"{safe_float(g.get('weight', 0), 0):.0f}%"))
        avg = self.calculate_average(data.get('grades', [])); total_weight = sum((safe_float(g.get('weight', 0), 0.0) for g in data.get('grades', []))); self.grade_average.config(text=f'Promedio ponderado: {avg:.2f} · porcentaje usado: {total_weight:.0f}/100%' if data.get('grades') else 'Sin notas aún · agrega nota y porcentaje'); self.subject_files_list.delete(0, tk.END)
        for path in data.get('files', []):
            self.subject_files_list.insert(tk.END, os.path.basename(path))
        self.flash_list.delete(0, tk.END); cards = data.get('flashcards', []); today = date.today(); filtered = []; mode = self.flash_filter_var.get() if hasattr(self, 'flash_filter_var') else 'Todas'
        for idx, card in enumerate(cards):
            due_date = parse_date_string(card.get('due'), today)
            if mode == 'Para hoy' and due_date and (due_date > today):
                continue
            if mode == 'Favoritas' and (not card.get('favorite')):
                continue
            if mode == 'Difíciles' and card.get('difficulty') != 'Difícil' and (safe_int(card.get('lapses', 0), 0) < 2):
                continue
            filtered.append((idx, card))
        self._flash_index_map = [idx for idx, _ in filtered]
        for idx, card in filtered:
            due = card.get('due', today_string()); flag = '⭐' if card.get('favorite') else ''; status = '📌' if parse_date_string(due, today) <= today else '⏳'; self.flash_list.insert(tk.END, f"{status}{flag} {card.get('q', '')} · {card.get('difficulty', 'Normal')} · due {due}")
        due_count = sum((1 for card in cards if parse_date_string(card.get('due'), today) <= today)); mastered = sum((1 for card in cards if safe_int(card.get('interval', 0), 0) >= 14))
        if hasattr(self, 'flash_stats_label'):
            self.flash_stats_label.config(text=f'Total: {len(cards)} · Para hoy: {due_count} · Dominadas: {mastered} · Filtro: {mode}')

    def save_subject_notes(self):
        subject = self.selected_subject()
        if not subject:
            messagebox.showerror('Apuntes', 'Selecciona una materia.'); return
        self.subject_data(subject)['notes'] = self.subject_notes_text.get('1.0', tk.END).strip(); self.save(); messagebox.showinfo('Apuntes', 'Apuntes guardados.')

    def add_grade(self):
        subject = self.selected_subject()
        if not subject:
            messagebox.showerror('Notas', 'Selecciona una materia.'); return
        name = self.grade_name_entry.get().strip() or 'Nota'; value = safe_float(self.grade_value_entry.get(), None); weight = safe_float(self.grade_weight_entry.get(), None)
        if value is None:
            messagebox.showerror('Notas', 'La calificación debe ser numérica.'); return
        if weight is None:
            messagebox.showerror('Notas', 'El porcentaje debe ser numérico.'); return
        if weight <= 0:
            messagebox.showerror('Notas', 'El porcentaje debe ser mayor que 0.'); return
        grades = self.subject_data(subject).setdefault('grades', []); used_weight = sum((safe_float(g.get('weight', 0), 0.0) for g in grades))
        if used_weight + weight > 100:
            remaining = max(0, 100 - used_weight); messagebox.showerror('Notas', f'La suma de porcentajes no puede pasar de 100%.\nTe queda disponible: {remaining:.0f}%.'); return
        grades.append({'name': name, 'value': value, 'weight': weight, 'date': now_string()}); self.grade_name_entry.delete(0, tk.END); self.grade_name_entry.insert(0, 'Actividad'); self.grade_value_entry.delete(0, tk.END); self.grade_value_entry.insert(0, '5.0'); self.grade_weight_entry.delete(0, tk.END); self.grade_weight_entry.insert(0, '%'); self.save(); self.load_selected_subject(); self.refresh_subjects()

    def delete_grade(self):
        subject = self.selected_subject(); sel = self.grade_list.selection()
        if not subject or not sel:
            messagebox.showerror('Notas', 'Selecciona una nota.'); return
        grades = self.subject_data(subject).setdefault('grades', []); index = self.grade_list.index(sel[0])
        if index < len(grades):
            del grades[index]; self.save(); self.load_selected_subject(); self.refresh_subjects()

    def calculate_average(self, grades):
        if not grades:
            return 0.0
        total_weight = sum((safe_float(g.get('weight', 0), 0.0) for g in grades))
        if total_weight > 0:
            weighted_sum = sum((safe_float(g.get('value', 0), 0.0) * safe_float(g.get('weight', 0), 0.0) for g in grades)); return weighted_sum / total_weight
        values = [safe_float(g.get('value', 0), 0.0) for g in grades]; return sum(values) / len(values) if values else 0.0

    def allowed_subject_file_extensions(self):
        return {'.pdf', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.txt', '.rtf', '.csv', '.png', '.jpg', '.jpeg', '.gif', '.mp3', '.mp4', '.wav', '.zip'}

    def validate_subject_file(self, path, show_message=True):
        if not path:
            if show_message:
                messagebox.showerror('Archivo', 'No se seleccionó ningún archivo.')
            return False
        path = os.path.abspath(path)
        if not os.path.exists(path):
            if show_message:
                messagebox.showerror('Archivo', 'El archivo ya no existe o fue movido de carpeta.')
            return False
        if not os.path.isfile(path):
            if show_message:
                messagebox.showerror('Archivo', 'Selecciona un archivo válido, no una carpeta.')
            return False
        if os.path.getsize(path) == 0:
            if show_message:
                messagebox.showerror('Archivo', 'El archivo está vacío y no se puede abrir correctamente.')
            return False
        ext = os.path.splitext(path)[1].lower()
        if ext not in self.allowed_subject_file_extensions():
            if show_message:
                messagebox.showerror('Archivo', 'Tipo de archivo no permitido. Puedes subir PDF, Word, PowerPoint, Excel, TXT, imágenes, audio, video o ZIP.')
            return False
        try:
            with open(path, 'rb') as fh:
                fh.read(1)
        except Exception as error:
            if show_message:
                messagebox.showerror('Archivo', f'No tengo permiso para leer este archivo:\n{error}')
            return False
        return True

    def add_subject_file(self):
        subject = self.selected_subject()
        if not subject:
            messagebox.showerror('Archivo', 'Selecciona una materia.'); return
        filetypes = [('Archivos de estudio', '*.pdf *.doc *.docx *.ppt *.pptx *.xls *.xlsx *.txt *.rtf *.csv *.png *.jpg *.jpeg *.gif *.mp3 *.mp4 *.wav *.zip'), ('Todos los archivos', '*.*')]; path = filedialog.askopenfilename(title='Selecciona un archivo para tus apuntes', filetypes=filetypes)
        if not path:
            return
        path = os.path.abspath(path)
        if not self.validate_subject_file(path):
            return
        files = self.subject_data(subject).setdefault('files', [])
        if path in files:
            messagebox.showinfo('Archivo', 'Este archivo ya está agregado en esta materia.'); return
        files.append(path); self.save(); self.load_selected_subject(); messagebox.showinfo('Archivo', 'Archivo agregado y validado correctamente. Ya puedes abrirlo desde la materia.')



    def add_flashcard(self):
        subject = self.selected_subject()
        if not subject:
            messagebox.showerror('Flashcards', 'Selecciona una materia.'); return
        q = self.flash_q_entry.get().strip(); a = self.flash_a_entry.get().strip()
        if not q or q == 'Pregunta' or (not a) or (a == 'Respuesta'):
            messagebox.showerror('Flashcards', 'Escribe pregunta y respuesta.'); return
        tags = self.flash_tags_entry.get().strip() if hasattr(self, 'flash_tags_entry') else ''
        if tags.startswith('Tags:'):
            tags = ''
        self.subject_data(subject).setdefault('flashcards', []).append({'q': q, 'a': a, 'created_at': now_string(), 'difficulty': self.flash_difficulty_var.get() if hasattr(self, 'flash_difficulty_var') else 'Normal', 'tags': tags, 'favorite': False, 'due': today_string(), 'interval': 0, 'ease': 2.5, 'reviews': 0, 'correct': 0, 'lapses': 0, 'last_review': ''}); self.flash_q_entry.delete(0, tk.END); self.flash_a_entry.delete(0, tk.END)
        if hasattr(self, 'flash_tags_entry'):
            self.flash_tags_entry.delete(0, tk.END); self.flash_tags_entry.insert(0, 'Tags: examen, vocabulario...')
        self.save(); self.load_selected_subject()




    def practice_flashcards(self, only_due=False):
        subject = self.selected_subject()
        if not subject:
            messagebox.showerror('Flashcards', 'Selecciona una materia.'); return
        all_cards = self.subject_data(subject).get('flashcards', [])
        if not all_cards:
            messagebox.showinfo('Flashcards', 'No hay fichas para practicar.'); return
        today = date.today(); pairs = [(idx, card) for idx, card in enumerate(all_cards)]
        if only_due:
            pairs = [(idx, card) for idx, card in pairs if parse_date_string(card.get('due'), today) <= today]
            if not pairs:
                messagebox.showinfo('Flashcards', 'No tienes fichas pendientes hoy. Michi está orgulloso ✨'); return
        pairs.sort(key=lambda item: (parse_date_string(item[1].get('due'), today), -safe_int(item[1].get('lapses', 0), 0))); cards = [card for _, card in pairs]; c = self.palette(); win = tk.Toplevel(self.root); win.title(f'Repaso inteligente · {subject}'); win.geometry('620x560'); win.configure(bg=c['bg']); tk.Label(win, text=f'Repaso inteligente · {subject}', bg=c['bg'], fg=c['primary'], font=('Arial', 15, 'bold')).pack(pady=10); tk.Label(win, text='Primero responde mentalmente, voltea y califica cómo te fue. El sistema programa el próximo repaso.', bg=c['bg'], fg=c['muted'], wraplength=560, justify='center').pack(); state = {'index': 0, 'front': True, 'reviewed': 0, 'session_correct': 0}; card_frame = tk.Frame(win, bg='#fffdfd', highlightbackground=c['secondary'], highlightthickness=2)
        card_frame.pack(fill='both', expand=True, padx=32, pady=18); side_label = tk.Label(card_frame, text='Pregunta', bg='#fffdfd', fg=c['primary'], font=('Arial', 11, 'bold')); side_label.pack(pady=(20, 5)); card_text = tk.Label(card_frame, text='', bg='#fffdfd', fg=c['text'], font=('Arial', 18, 'bold'), wraplength=500, justify='center'); card_text.pack(expand=True, pady=20); meta_label = tk.Label(card_frame, text='', bg='#fffdfd', fg=c['muted'], font=('Arial', 10, 'italic'), wraplength=500); meta_label.pack(pady=(0, 18)); bottom = tk.Frame(win, bg=c['bg']); bottom.pack(fill='x', padx=20, pady=6); progress_label = tk.Label(bottom, text='', bg=c['bg'], fg=c['text'], font=('Arial', 10, 'bold')); progress_label.pack(side='left'); session_label = tk.Label(bottom, text='', bg=c['bg'], fg=c['muted'], font=('Arial', 10))
        session_label.pack(side='right')

        def current_card():
            return cards[state['index']]

        def render_card():
            card = current_card(); front = state['front']; bg = '#fffdfd' if front else '#fff2f7'; card_frame.configure(bg=bg); side_label.configure(text='Pregunta' if front else 'Respuesta', bg=bg, fg=c['primary']); card_text.configure(text=card.get('q', '') if front else card.get('a', ''), bg=bg, fg=c['text']); due = card.get('due', today_string()); interval = safe_int(card.get('interval', 0), 0); ease = safe_float(card.get('ease', 2.5), 2.5); tags = card.get('tags', ''); hint = 'Piensa la respuesta y voltea.' if front else 'Ahora califica tu recuerdo abajo.'; meta_label.configure(text=f"{hint} · Dificultad: {card.get('difficulty', 'Normal')} · intervalo: {interval}d · facilidad: {ease:.1f} · due: {due}" + (f' · tags: {tags}' if tags else ''), bg=bg, fg=c['muted']); progress_label.configure(text=f"Ficha {state['index'] + 1} de {len(cards)}")
            session_label.configure(text=f"Sesión: {state['reviewed']} revisadas · {state['session_correct']} bien"); flip_btn.configure(text='Ver pregunta' if not front else 'Voltear')

        def flip_card(event=None):
            state['front'] = not state['front']; render_card()

        def next_card(step=1):
            state['index'] = (state['index'] + step) % len(cards); state['front'] = True; render_card()

        def grade_card(quality):
            card = current_card(); old_interval = safe_int(card.get('interval', 0), 0); ease = safe_float(card.get('ease', 2.5), 2.5)
            if quality == 'again':
                interval = 0; ease = max(1.3, ease - 0.25); card['lapses'] = safe_int(card.get('lapses', 0), 0) + 1
            elif quality == 'hard':
                interval = max(1, old_interval if old_interval else 1); ease = max(1.3, ease - 0.1)
            elif quality == 'good':
                interval = 1 if old_interval == 0 else max(2, round(old_interval * ease)); card['correct'] = safe_int(card.get('correct', 0), 0) + 1; state['session_correct'] += 1
            else:
                interval = 3 if old_interval == 0 else max(4, round(old_interval * (ease + 0.35))); ease = min(3.2, ease + 0.15); card['correct'] = safe_int(card.get('correct', 0), 0) + 1; state['session_correct'] += 1
            if card.get('difficulty') == 'Difícil' and quality in ('again', 'hard'):
                interval = min(interval, 1)
            elif card.get('difficulty') == 'Fácil' and quality in ('good', 'easy'):
                interval += 1
            card['interval'] = interval; card['ease'] = round(ease, 2); card['reviews'] = safe_int(card.get('reviews', 0), 0) + 1; card['last_review'] = today_string(); card['due'] = (date.today() + timedelta(days=interval)).isoformat(); state['reviewed'] += 1; self.add_rewards(fresas=3 if quality in ('good', 'easy') else 1, xp=6 if quality in ('good', 'easy') else 2, pet_xp=3); self.save(); self.load_selected_subject()
            if state['index'] == len(cards) - 1:
                messagebox.showinfo('Repaso', f"Sesión terminada: {state['reviewed']} revisadas, {state['session_correct']} bien. ¡Buen trabajo!"); win.destroy(); self.refresh_all(); return
            next_card(1)
        card_frame.bind('<Button-1>', flip_card); side_label.bind('<Button-1>', flip_card); card_text.bind('<Button-1>', flip_card); meta_label.bind('<Button-1>', flip_card); nav = tk.Frame(win, bg=c['bg']); nav.pack(fill='x', padx=20, pady=(0, 8)); tk.Button(nav, text='◀', command=lambda: next_card(-1), bg='#d7ecff').pack(side='left', fill='x', expand=True, padx=3); flip_btn = tk.Button(nav, text='Voltear', command=flip_card, bg=c['accent']); flip_btn.pack(side='left', fill='x', expand=True, padx=3); tk.Button(nav, text='▶', command=lambda: next_card(1), bg='#d6f5df').pack(side='left', fill='x', expand=True, padx=3); grades = tk.Frame(win, bg=c['bg']); grades.pack(fill='x', padx=20, pady=(0, 15)); tk.Button(grades, text='Olvidé', command=lambda: grade_card('again'), bg=c['danger']).pack(side='left', fill='x', expand=True, padx=3)
        tk.Button(grades, text='Difícil', command=lambda: grade_card('hard'), bg='#fff1b8').pack(side='left', fill='x', expand=True, padx=3); tk.Button(grades, text='Bien', command=lambda: grade_card('good'), bg='#cfe8ff').pack(side='left', fill='x', expand=True, padx=3); tk.Button(grades, text='Fácil', command=lambda: grade_card('easy'), bg='#d6f5df').pack(side='left', fill='x', expand=True, padx=3); render_card()

    def add_library_item(self):
        c = self.palette(); win = tk.Toplevel(self.root); win.title('Agregar recurso'); win.geometry('420x420'); win.configure(bg=c['bg']); tk.Label(win, text='Nuevo recurso', bg=c['bg'], fg=c['primary'], font=('Arial', 16, 'bold')).pack(pady=10); fields = {}
        for label in ['Título', 'Autor/Fuente', 'URL o ruta', 'Notas']:
            tk.Label(win, text=label, bg=c['bg'], fg=c['text']).pack(anchor='w', padx=20); ent = tk.Entry(win); ent.pack(fill='x', padx=20, pady=3); fields[label] = ent
        tk.Label(win, text='Tipo', bg=c['bg'], fg=c['text']).pack(anchor='w', padx=20); type_var = tk.StringVar(value='Libro'); ttk.Combobox(win, textvariable=type_var, values=['Libro', 'PDF', 'Video', 'Playlist', 'Link', 'Apunte'], state='readonly').pack(fill='x', padx=20, pady=3)

        def save_item():
            title = fields['Título'].get().strip()
            if not title:
                messagebox.showerror('Biblioteca', 'El título es obligatorio.'); return
            self.user_data['library'].append({'title': title, 'author': fields['Autor/Fuente'].get().strip(), 'type': type_var.get(), 'location': fields['URL o ruta'].get().strip(), 'notes': fields['Notas'].get().strip(), 'done': False, 'created_at': now_string()}); self.save(); self.refresh_library(); win.destroy()
        tk.Button(win, text='Guardar recurso', command=save_item, bg=c['accent']).pack(fill='x', padx=20, pady=12)

    def add_library_file(self):
        path = filedialog.askopenfilename()
        if not path:
            return
        self.user_data['library'].append({'title': os.path.basename(path), 'author': 'Archivo local', 'type': 'Archivo', 'location': path, 'notes': '', 'done': False, 'created_at': now_string()}); self.save(); self.refresh_library()

    def library_selection_index(self):
        sel = self.library_list.curselection()
        if not sel or not self._library_index_map:
            return None
        if self.library_list.get(sel[0]).startswith('Tu biblioteca'):
            return None
        return sel[0]

    def preview_library_item(self):
        idx = self.library_selection_index()
        if idx is None:
            return
        item = self._library_index_map[idx]; text = f"Título: {item.get('title', '')}\nTipo: {item.get('type', '')}\nAutor/Fuente: {item.get('author', '')}\nUbicación: {item.get('location', '')}\nEstado: {('Terminado' if item.get('done') else 'Pendiente')}\n\nNotas:\n{item.get('notes', '')}"; self.library_detail.delete('1.0', tk.END); self.library_detail.insert('1.0', text)

    def open_library_item(self):
        idx = self.library_selection_index()
        if idx is None:
            messagebox.showerror('Biblioteca', 'Selecciona un recurso.'); return
        item = self._library_index_map[idx]; location = item.get('location', '')
        if not location:
            messagebox.showinfo('Biblioteca', 'Ese recurso no tiene enlace o archivo.'); return
        if location.startswith('http://') or location.startswith('https://'):
            self.open_url(location)
        else:
            self.open_path(location)

    def delete_library_item(self):
        idx = self.library_selection_index()
        if idx is None:
            messagebox.showerror('Biblioteca', 'Selecciona un recurso.'); return
        if messagebox.askyesno('Biblioteca', '¿Eliminar este recurso?'):
            del self.user_data['library'][idx]; self.save(); self.refresh_library()

    def toggle_library_done(self):
        idx = self.library_selection_index()
        if idx is None:
            messagebox.showerror('Biblioteca', 'Selecciona un recurso.'); return
        item = self.user_data['library'][idx]; item['done'] = not item.get('done', False); self.save(); self.refresh_library()

    def save_library_notes(self):
        idx = self.library_selection_index()
        if idx is None:
            messagebox.showerror('Biblioteca', 'Selecciona un recurso.'); return
        content = self.library_detail.get('1.0', tk.END); notes_marker = 'Notas:\n'; notes = content.split(notes_marker, 1)[1].strip() if notes_marker in content else ''; self.user_data['library'][idx]['notes'] = notes; self.save(); self.refresh_library(); messagebox.showinfo('Biblioteca', 'Notas del recurso guardadas.')

    def shop_items(self):
        return [{'name': 'Moño rosa', 'icon': '🎀', 'slot': 'accessory', 'price': 40, 'effect': 'Se ve más cute y felicidad +10'}, {'name': 'Corona', 'icon': '👑', 'slot': 'accessory', 'price': 70, 'effect': 'Look de princesa y felicidad +15'}, {'name': 'Lentes', 'icon': '👓', 'slot': 'accessory', 'price': 55, 'effect': 'Modo nerd adorable'}, {'name': 'Estrellita', 'icon': '⭐', 'slot': 'accessory', 'price': 45, 'effect': 'Clip brillante y tierno'}, {'name': 'Libro mini', 'icon': '📘', 'slot': 'accessory', 'price': 60, 'effect': 'Accesorio de estudio'}, {'name': 'Vestido lavanda', 'icon': '👗', 'slot': 'outfit', 'price': 80, 'effect': 'Vestido color lavanda', 'dress_color': 'Lavanda'}, {'name': 'Vestido menta', 'icon': '👗', 'slot': 'outfit', 'price': 80, 'effect': 'Vestido color menta', 'dress_color': 'Menta'}, {'name': 'Vestido cielo', 'icon': '👗', 'slot': 'outfit', 'price': 80, 'effect': 'Vestido color azul cielo', 'dress_color': 'Azul cielo'}, {'name': 'Vestido vainilla', 'icon': '👗', 'slot': 'outfit', 'price': 80, 'effect': 'Vestido color vainilla', 'dress_color': 'Vainilla'}, {'name': 'Paleta lavanda', 'icon': '🎨', 'slot': 'palette', 'price': 65, 'effect': 'Capucha y vestido lavanda', 'hood_color': 'Lavanda', 'dress_color': 'Lavanda'}, {'name': 'Paleta menta', 'icon': '🎨', 'slot': 'palette', 'price': 65, 'effect': 'Capucha y vestido menta', 'hood_color': 'Menta', 'dress_color': 'Menta'}, {'name': 'Paleta cielo', 'icon': '🎨', 'slot': 'palette', 'price': 65, 'effect': 'Capucha y vestido azul cielo', 'hood_color': 'Azul cielo', 'dress_color': 'Azul cielo'}, {'name': 'Snack premium', 'icon': '🍰', 'slot': 'consumable_happiness', 'price': 25, 'effect': 'Felicidad +35'}, {'name': 'Bebida energética', 'icon': '⚡', 'slot': 'consumable_energy', 'price': 25, 'effect': 'Energía +35'}, {'name': 'Fresitas', 'icon': '🍓', 'slot': 'consumable_food', 'price': 18, 'effect': 'Hambre -35'}]



    def apply_consumable(self, item):
        pet = self.user_data['pet']
        if item['slot'] == 'consumable_happiness':
            pet['happiness'] = clamp(pet['happiness'] + 35)
        elif item['slot'] == 'consumable_energy':
            pet['energy'] = clamp(pet['energy'] + 35)
        elif item['slot'] == 'consumable_food':
            pet['hunger'] = clamp(pet['hunger'] - 35)


    def use_inventory_item(self):
        sel = self.inventory_list.curselection()
        if not sel or not self._inventory_index_map or self.inventory_list.get(sel[0]).startswith('Tu inventario'):
            messagebox.showerror('Inventario', 'Selecciona un item.'); return
        item = self._inventory_index_map[sel[0]]; pet = self.user_data['pet']; slot = item.get('slot')
        if slot == 'accessory':
            pet['accessory'] = item.get('name', pet.get('accessory')); pet['happiness'] = clamp(pet['happiness'] + 10)
        elif slot == 'outfit':
            pet['outfit'] = item.get('name', pet.get('outfit'))
            if item.get('dress_color'):
                pet['dress_color'] = item.get('dress_color')
        elif slot == 'palette':
            pet['hood_color'] = item.get('hood_color', pet.get('hood_color')); pet['dress_color'] = item.get('dress_color', pet.get('dress_color'))
        self.save(); self.refresh_all(); messagebox.showinfo('Inventario', f"Tu michi ahora usa: {item.get('name', 'item')}")

    def delete_inventory_item(self):
        sel = self.inventory_list.curselection()
        if not sel or not self._inventory_index_map or self.inventory_list.get(sel[0]).startswith('Tu inventario'):
            messagebox.showerror('Inventario', 'Selecciona un item.'); return
        if messagebox.askyesno('Inventario', '¿Eliminar este item?'):
            del self.user_data['inventory'][sel[0]]; self.save(); self.refresh_all()


    def reward_game_win(self, label='Minijuego ganado'):
        self.user_data['metrics']['mini_games_won'] += 1; self.user_data['pet']['happiness'] = clamp(self.user_data['pet']['happiness'] + 8); self.add_rewards(fresas=8, xp=10, pet_xp=8); self.refresh_all(); messagebox.showinfo('Minijuego', f'{label}. +8 fresas, +10 XP.')

    def open_guess_game(self):
        number = random.randint(1, 20); attempts = {'n': 0}; c = self.palette(); win = tk.Toplevel(self.root); win.title('Adivina el número'); win.geometry('320x230'); win.configure(bg=c['bg']); tk.Label(win, text='Adivina un número del 1 al 20', bg=c['bg'], fg=c['text'], font=('Arial', 12, 'bold')).pack(pady=12); entry = tk.Entry(win); entry.pack(pady=5); result = tk.Label(win, text='', bg=c['bg'], fg=c['primary']); result.pack(pady=8)

        def check():
            attempts['n'] += 1; guess = safe_int(entry.get(), -1)
            if guess == number:
                self.reward_game_win('¡Adivinaste el número!'); win.destroy()
            elif attempts['n'] >= 5:
                result.config(text=f'Se acabaron los intentos. Era {number}.')
            elif guess < number:
                result.config(text='Más alto ⬆')
            else:
                result.config(text='Más bajo ⬇')
        tk.Button(win, text='Probar', command=check, bg=c['accent']).pack(fill='x', padx=20, pady=8)

    def open_memory_game(self):
        emojis = ['🍓', '📚', '🐱', '⭐', '🌸', '🍅']; sequence = [random.choice(emojis) for _ in range(4)]; c = self.palette(); win = tk.Toplevel(self.root); win.title('Memoria de emojis'); win.geometry('380x260'); win.configure(bg=c['bg']); tk.Label(win, text='Memoriza la secuencia', bg=c['bg'], fg=c['text'], font=('Arial', 12, 'bold')).pack(pady=8); seq_label = tk.Label(win, text=' '.join(sequence), bg=c['bg'], fg=c['primary'], font=('Arial', 26)); seq_label.pack(pady=8); entry = tk.Entry(win, font=('Arial', 14)); entry.pack(fill='x', padx=20, pady=8); tk.Label(win, text='Escríbela separada por espacios', bg=c['bg'], fg=c['muted'], wraplength=330).pack(pady=4); win.after(3500, lambda: seq_label.config(text='? ? ? ?') if win.winfo_exists() else None)

        def check():
            typed = entry.get().strip().split()
            if typed == sequence:
                self.reward_game_win('¡Memoria perfecta!'); win.destroy()
            else:
                messagebox.showinfo('Memoria', 'Casi. Intenta otra ronda después.')
        tk.Button(win, text='Comprobar', command=check, bg=c['accent']).pack(fill='x', padx=20, pady=10)

    def open_reaction_game(self):
        c = self.palette(); win = tk.Toplevel(self.root); win.title('Reflejos'); win.geometry('340x240'); win.configure(bg=c['bg']); ready = {'go': False}; label = tk.Label(win, text='Espera a que diga ¡YA!', bg=c['bg'], fg=c['text'], font=('Arial', 16, 'bold')); label.pack(pady=30); delay = random.randint(1500, 4200)

        def set_go():
            if win.winfo_exists():
                ready['go'] = True; label.config(text='¡YA! ⚡', fg=c['primary'])
        win.after(delay, set_go)

        def click():
            if ready['go']:
                self.reward_game_win('¡Buenos reflejos!'); win.destroy()
            else:
                label.config(text='Muy pronto 😅 espera el YA')
        tk.Button(win, text='Click', command=click, bg=c['accent'], font=('Arial', 14, 'bold')).pack(fill='x', padx=40, pady=20)

    def open_math_game(self):
        a = random.randint(2, 12); b = random.randint(2, 12); op = random.choice(['+', '-']); answer_value = a + b if op == '+' else a - b; c = self.palette(); win = tk.Toplevel(self.root); win.title('Quiz matemático'); win.geometry('340x220'); win.configure(bg=c['bg']); tk.Label(win, text='Resuelve la operación', bg=c['bg'], fg=c['text'], font=('Arial', 12, 'bold')).pack(pady=12); tk.Label(win, text=f'{a} {op} {b} = ?', bg=c['bg'], fg=c['primary'], font=('Arial', 24, 'bold')).pack(pady=6); entry = tk.Entry(win); entry.pack(pady=8)

        def check():
            if safe_int(entry.get(), 99999) == answer_value:
                self.reward_game_win('¡Respuesta correcta!'); win.destroy()
            else:
                messagebox.showinfo('Quiz', f'No era. La respuesta correcta era {answer_value}.')
        tk.Button(win, text='Comprobar', command=check, bg=c['accent']).pack(fill='x', padx=20, pady=8)

    def open_word_game(self):
        words = ['pomodoro', 'biblioteca', 'resumen', 'materia', 'estudio', 'organizar', 'apuntes']; word = random.choice(words); letters = list(word); random.shuffle(letters); scrambled = ''.join(letters); c = self.palette(); win = tk.Toplevel(self.root); win.title('Ordena la palabra'); win.geometry('380x250'); win.configure(bg=c['bg']); tk.Label(win, text='Ordena la palabra', bg=c['bg'], fg=c['text'], font=('Arial', 12, 'bold')).pack(pady=12); tk.Label(win, text=scrambled, bg=c['bg'], fg=c['primary'], font=('Arial', 24, 'bold')).pack(pady=6); entry = tk.Entry(win); entry.pack(fill='x', padx=20, pady=8)

        def check():
            if entry.get().strip().lower() == word:
                self.reward_game_win('¡Palabra correcta!'); win.destroy()
            else:
                messagebox.showinfo('Palabra', f'Casi. La palabra era: {word}')
        tk.Button(win, text='Comprobar', command=check, bg=c['accent']).pack(fill='x', padx=20, pady=8)





    def save_media_links(self):
        self.user_data['profile']['spotify_url'] = self.spotify_entry.get().strip() or 'https://open.spotify.com'; self.user_data['profile']['youtube_url'] = self.youtube_entry.get().strip() or 'https://www.youtube.com'; self.save(); messagebox.showinfo('Conexiones', 'Enlaces guardados correctamente.')

    def save_settings_toggles(self):
        self.user_data['settings']['pro_home'] = bool(self.pro_home_var.get()); self.user_data['settings']['animations'] = bool(self.animations_var.get()); self.user_data['settings']['auto_optimize'] = bool(self.auto_opt_var.get()); self.save()

    def optimize_user_data(self):
        self.user_data['moods'] = self.user_data.get('moods', [])[-150:]; self.user_data['shop_history'] = self.user_data.get('shop_history', [])[-150:]; seen = set(); tasks = []
        for task in self.user_data.get('tasks', []):
            key = (task.get('text', ''), task.get('created_at', ''))
            if key not in seen:
                seen.add(key); tasks.append(task)
        self.user_data['tasks'] = tasks; self.user_data['metrics']['optimizations_run'] += 1; self.user_data['metrics']['last_optimized'] = now_string(); self.save(); self.refresh_all(); messagebox.showinfo('Optimización', 'Datos optimizados correctamente.')

    def create_quick_backup(self):
        if not self.current_user:
            return
        filename = f"{self.current_user}_michi_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        try:
            with open(filename, 'w', encoding='utf-8') as fh:
                json.dump(self.user_data, fh, indent=4, ensure_ascii=False)
            messagebox.showinfo('Backup', f'Backup creado:\n{filename}')
        except Exception as error:
            messagebox.showerror('Backup', f'No se pudo crear el backup:\n{error}')

    def import_backup(self):
        path = filedialog.askopenfilename(filetypes=[('JSON', '*.json')])
        if not path:
            return
        if not messagebox.askyesno('Importar', 'Esto reemplazará los datos actuales. ¿Continuar?'):
            return
        try:
            with open(path, 'r', encoding='utf-8') as fh:
                imported = json.load(fh)
            if not isinstance(imported, dict):
                raise ValueError('Formato inválido')
            imported['password'] = self.user_data.get('password', ''); self.user_data = imported; self.users[self.current_user] = imported; self.ensure_schema(); self.save(); self.build_main_ui(); messagebox.showinfo('Importar', 'Backup importado correctamente.')
        except Exception as error:
            messagebox.showerror('Importar', f'No se pudo importar:\n{error}')

    def export_user_data(self):
        path = filedialog.asksaveasfilename(defaultextension='.json', filetypes=[('JSON', '*.json')], initialfile=f'{self.current_user}_michi_studio_backup.json')
        if not path:
            return
        data = dict(self.user_data); data['exported_at'] = now_string()
        try:
            with open(path, 'w', encoding='utf-8') as fh:
                json.dump(data, fh, indent=4, ensure_ascii=False)
            messagebox.showinfo('Exportar', 'Datos exportados correctamente.')
        except Exception as error:
            messagebox.showerror('Exportar', f'No se pudo exportar:\n{error}')

    def search_google(self, entry_widget):
        query = entry_widget.get().strip()
        if query and 'Buscar' not in query and ('Google' not in query):
            self.open_url(f'https://www.google.com/search?q={quote_plus(query)}')

    def open_spotify(self):
        self.open_url(self.user_data['profile'].get('spotify_url', 'https://open.spotify.com'))

    def open_youtube(self):
        self.open_url(self.user_data['profile'].get('youtube_url', 'https://www.youtube.com'))

    def open_lofi(self):
        self.open_url('https://www.youtube.com/results?search_query=lofi+study+music')

    def open_path(self, path):
        if not os.path.exists(path):
            messagebox.showerror('Archivo', 'El archivo ya no existe.'); return
        try:
            if sys.platform.startswith('win'):
                os.startfile(path)
            elif sys.platform.startswith('darwin'):
                subprocess.call(['open', path])
            else:
                subprocess.call(['xdg-open', path])
        except Exception as error:
            messagebox.showerror('Archivo', f'No se pudo abrir:\n{error}')

    def animate_pet(self):
        if not self.user_data:
            return
        if self.user_data.get('settings', {}).get('animations', True):
            phrases = ['Tu michi cree en ti 🐾', 'Una tarea pequeña también cuenta ✨', 'Pomodoro + mood + tareas = progreso suave 📚', 'Revisa tu biblioteca personal para estudiar mejor 📖']
            if random.randint(1, 4) == 1:
                self.pet_speech.config(text=random.choice(phrases))
        self.refresh_pet(); self.pet_animation_id = self.root.after(random.randint(2500, 4500), self.animate_pet)

    def on_close(self):
        self.save(); self.timer.pause(self.root); self.root.destroy()

# Export every runtime name so the legacy patch modules share the same namespace.
__all__ = [name for name in globals() if not name.startswith("__")]


# =============================================================================
# Parches optimizados conservadores
# =============================================================================
import calendar as _ms_v6_calendar
import calendar as _ms_v7_calendar
_MS_V30_ROOM_DRAWERS = None

def _ms_v2_ensure_schema(self):
    _ms_old_ensure_schema(self); self.user_data.setdefault('planner_events', []); self.user_data.setdefault('flashcard_categories', ['General', 'Definiciones', 'Fórmulas', 'Fechas', 'Vocabulario']); self.user_data.setdefault('achievement_claims', {}); self.user_data.setdefault('daily_checklist', []); self.user_data.setdefault('arcade_best', {}); self.user_data['metrics'].setdefault('planner_events_completed', 0); self.user_data['metrics'].setdefault('flashcards_practiced', 0); self.user_data['metrics'].setdefault('runner_best_score', 0)
    for subject, data in self.user_data.get('subjects', {}).items():
        for card in data.get('flashcards', []):
            card.setdefault('category', 'General')
    self.save()

def _ms_v2_build_main_ui(self):
    _ms_old_build_main_ui(self); c = self.palette(); self.planner_tab = tk.Frame(self.notebook, bg=c['bg']); self.achievements_tab = tk.Frame(self.notebook, bg=c['bg']); self.notebook.add(self.planner_tab, text='📅 Planificador'); self.notebook.add(self.achievements_tab, text='🏆 Logros'); self.build_planner_tab(); self.build_achievements_tab(); self.add_arcade_extra_panel(); self.refresh_planner_events(); self.refresh_achievements()

def _ms_v2_refresh_all(self):
    _ms_old_refresh_all(self)
    if hasattr(self, 'planner_list'):
        self.refresh_planner_events()
    if hasattr(self, 'achievement_list'):
        self.refresh_achievements()

def _ms_v2_load_selected_subject(self):
    _ms_old_load_selected_subject(self)
    if hasattr(self, 'flash_category_var'):
        cats = self.user_data.get('flashcard_categories', ['General'])
        if self.flash_category_var.get() not in cats:
            self.flash_category_var.set(cats[0] if cats else 'General')

def add_flashcard_category(self):
    name = simpledialog.askstring('Categoría', 'Nombre de la categoría:')
    if not name:
        return
    name = name.strip(); cats = self.user_data.setdefault('flashcard_categories', ['General'])
    if name not in cats:
        cats.append(name)
    self.save(); self.build_main_ui()

def open_skater_game(self):
    c = self.palette(); self.ensure_michi_assets(); win = tk.Toplevel(self.root); win.title('Michi Skater'); win.geometry('520x420'); win.configure(bg=c['bg']); canvas = tk.Canvas(win, width=500, height=330, bg='#fff8fb', highlightthickness=0); canvas.pack(pady=10); info = tk.Label(win, text='Espacio = saltar. Esquiva charcos y junta estrellas.', bg=c['bg'], fg=c['text'], font=('Arial', 10, 'bold')); info.pack(); state = {'x': 90, 'y': 250, 'vy': 0, 'jump': False, 'score': 0, 'stars': 0, 'running': True, 'speed': 7}; items = []

    def spawn():
        kind = 'star' if random.random() < 0.35 else 'puddle'; items.append({'x': 520, 'y': 255 if kind == 'puddle' else random.randint(145, 230), 'kind': kind})

    def draw():
        canvas.delete('all'); canvas.create_rectangle(0, 278, 500, 330, fill='#d8b494', outline=''); canvas.create_line(0, 278, 500, 278, fill='#9a785f', width=3)
        for i in range(0, 520, 40):
            canvas.create_text((i - state['score'] * 3) % 520, 40 + i % 80, text='☁', font=('Arial', 16), fill='#f3cbd8')
        if getattr(self, 'michi_runner_photo', None):
            canvas.create_image(state['x'], state['y'] - 35, image=self.michi_runner_photo)
        else:
            canvas.create_text(state['x'], state['y'] - 35, text='🐱', font=('Arial', 36))
        canvas.create_rectangle(state['x'] - 28, state['y'] + 10, state['x'] + 28, state['y'] + 16, fill='#ff7fa7', outline=''); canvas.create_oval(state['x'] - 26, state['y'] + 13, state['x'] - 16, state['y'] + 23, fill='#333', outline=''); canvas.create_oval(state['x'] + 16, state['y'] + 13, state['x'] + 26, state['y'] + 23, fill='#333', outline='')
        for obj in items:
            if obj['kind'] == 'star':
                canvas.create_text(obj['x'], obj['y'], text='⭐', font=('Arial', 22))
            else:
                canvas.create_oval(obj['x'] - 28, obj['y'] - 8, obj['x'] + 28, obj['y'] + 8, fill='#87ceeb', outline='#4aa3c7')
        canvas.create_text(10, 10, anchor='nw', text=f"Puntos {state['score']} · Estrellas {state['stars']}", fill=c['text'], font=('Arial', 11, 'bold'))

    def end_game():
        state['running'] = False; reward_fresas = max(5, state['stars'] * 3 + state['score'] // 25); reward_xp = max(8, state['score'] // 4); self.user_data['metrics']['mini_games_won'] += 1; self.add_rewards(fresas=reward_fresas, xp=reward_xp, pet_xp=reward_xp // 2); self.refresh_all(); canvas.create_rectangle(115, 115, 385, 220, fill='#fff', outline=c['secondary'], width=2); canvas.create_text(250, 145, text='Fin del juego', fill=c['primary'], font=('Arial', 18, 'bold')); canvas.create_text(250, 180, text=f'Ganaste {reward_fresas} fresas y {reward_xp} XP', fill=c['text'], font=('Arial', 11))

    def step():
        if not state['running'] or not win.winfo_exists():
            return
        state['score'] += 1
        if state['score'] % 110 == 0:
            state['speed'] += 1
        if random.random() < 0.07:
            spawn()
        if state['jump']:
            state['y'] += state['vy']; state['vy'] += 2
            if state['y'] >= 250:
                state['y'] = 250; state['vy'] = 0; state['jump'] = False
        keep = []
        for obj in items:
            obj['x'] -= state['speed']
            if obj['x'] < -40:
                continue
            if abs(obj['x'] - state['x']) < 36 and abs(obj['y'] - state['y']) < 42:
                if obj['kind'] == 'star':
                    state['stars'] += 1; state['score'] += 15; continue
                if not state['jump']:
                    draw(); end_game(); return
            keep.append(obj)
        items[:] = keep; draw(); win.after(40, step)

    def key(event):
        if event.keysym == 'space' and (not state['jump']):
            state['jump'] = True; state['vy'] = -24
    win.bind('<space>', key); win.focus_force(); draw(); step()

def open_catch_game(self):
    c = self.palette(); win = tk.Toplevel(self.root); win.title('Atrapa fresas'); win.geometry('420x520'); win.configure(bg=c['bg']); canvas = tk.Canvas(win, width=390, height=430, bg='#fff8fb', highlightthickness=0); canvas.pack(pady=10); state = {'x': 195, 'score': 0, 'miss': 0, 'running': True}; drops = []

    def spawn():
        drops.append({'x': random.randint(25, 365), 'y': -20, 'kind': 'bad' if random.random() < 0.2 else 'berry'})

    def draw():
        canvas.delete('all'); canvas.create_rectangle(0, 0, 390, 430, fill='#fff8fb', outline=''); canvas.create_text(state['x'], 395, text='🧺', font=('Arial', 34))
        for d in drops:
            canvas.create_text(d['x'], d['y'], text='💧' if d['kind'] == 'bad' else '🍓', font=('Arial', 22))
        canvas.create_text(10, 10, anchor='nw', text=f"Fresas {state['score']} · Fallos {state['miss']}/3", fill=c['text'], font=('Arial', 11, 'bold'))

    def end():
        state['running'] = False; reward = max(4, state['score']); self.user_data['metrics']['mini_games_won'] += 1; self.add_rewards(fresas=reward, xp=reward * 2, pet_xp=reward); self.refresh_all(); canvas.create_rectangle(75, 160, 315, 250, fill='#fff', outline=c['secondary'], width=2); canvas.create_text(195, 190, text='Fin', fill=c['primary'], font=('Arial', 18, 'bold')); canvas.create_text(195, 220, text=f'Ganaste {reward} fresas', fill=c['text'])

    def step():
        if not state['running'] or not win.winfo_exists():
            return
        if random.random() < 0.12:
            spawn()
        keep = []
        for d in drops:
            d['y'] += 7
            if d['y'] > 380 and abs(d['x'] - state['x']) < 42:
                if d['kind'] == 'berry':
                    state['score'] += 1
                else:
                    state['miss'] += 1
                continue
            if d['y'] > 450:
                if d['kind'] == 'berry':
                    state['miss'] += 1
                continue
            keep.append(d)
        drops[:] = keep
        if state['miss'] >= 3:
            draw(); end(); return
        draw(); win.after(45, step)

    def key(event):
        if event.keysym in ('Left', 'a', 'A'):
            state['x'] = max(30, state['x'] - 35)
        elif event.keysym in ('Right', 'd', 'D'):
            state['x'] = min(360, state['x'] + 35)
        draw()
    win.bind('<Left>', key); win.bind('<Right>', key); win.bind('a', key); win.bind('d', key); win.focus_force(); draw(); step()

def achievement_rules(self):
    m = self.user_data.get('metrics', {}); cur = self.user_data.get('currency', {}); return [('Primer paso', m.get('tasks_completed', 0) >= 1, 'Completa tu primera tarea'), ('Modo foco', m.get('pomodoros_completed', 0) >= 1, 'Completa tu primer Pomodoro'), ('Constancia', m.get('study_streak', 0) >= 3, 'Alcanza una racha de 3 días'), ('Arcade Michi', m.get('mini_games_won', 0) >= 5, 'Gana 5 minijuegos'), ('Coleccionista', len(self.user_data.get('inventory', [])) >= 3, 'Ten 3 items en inventario'), ('Bibliotecaria', len(self.user_data.get('library', [])) >= 3, 'Guarda 3 recursos en biblioteca'), ('Repaso inteligente', m.get('flashcards_practiced', 0) >= 10, 'Practica 10 fichas'), ('Planificadora', m.get('planner_events_completed', 0) >= 3, 'Completa 3 eventos del calendario'), ('Nivel 5', cur.get('level', 1) >= 5, 'Llega al nivel 5')]

def _ms_v3_ensure_schema(self):
    _ms_v3_prev_ensure_schema(self); self.user_data.setdefault('arcade_best', {})
    for key in ['bubble_pop', 'flash_quiz', 'skater', 'catch']:
        self.user_data['arcade_best'].setdefault(key, 0)
    self.user_data.setdefault('flashcard_categories', ['General', 'Definiciones', 'Fórmulas', 'Fechas', 'Vocabulario'])
    for subject, data in self.user_data.get('subjects', {}).items():
        for card in data.get('flashcards', []):
            card.setdefault('category', 'General'); card.setdefault('stats', {'ok': 0, 'review': 0, 'seen': 0, 'last_review': ''})

def _ms_v3_build_study_tab(self):
    c = self.palette(); main = tk.Frame(self.study_tab, bg=c['bg']); main.pack(fill='both', expand=True, padx=10, pady=10); left = tk.Frame(main, bg=c['bg']); left.pack(side='left', fill='both', expand=True, padx=8); right = tk.Frame(main, bg=c['bg']); right.pack(side='right', fill='both', expand=True, padx=8); pomo = self.card(left, 'Pomodoro focus principal', '🍅'); pomo.pack(fill='both', expand=True, pady=6); pomo_body = self.card_content(pomo); focus_banner = tk.Frame(pomo_body, bg=c['primary'], padx=18, pady=14); focus_banner.pack(fill='x', pady=(0, 12)); tk.Label(focus_banner, text='Sesión Pomodoro', bg=c['primary'], fg='white', font=self.app_font(18, 'bold')).pack(anchor='w')
    tk.Label(focus_banner, text='El temporizador es el centro de tu estudio. Prepara tu bloque y empieza.', bg=c['primary'], fg='white', font=self.app_font(10)).pack(anchor='w', pady=(2, 0)); self.study_pet_canvas = tk.Canvas(pomo_body, width=250, height=265, bg=c['card'], highlightthickness=0); self.study_pet_canvas.pack(pady=(2, 8)); timer_box = tk.Frame(pomo_body, bg=c['soft'], highlightbackground=c['secondary'], highlightthickness=1, padx=20, pady=18); timer_box.pack(fill='x', pady=(4, 12)); self.timer_label = tk.Label(timer_box, text='25:00', font=('Consolas', 58, 'bold'), bg=c['soft'], fg=c['primary']); self.timer_label.pack(); tk.Label(timer_box, text='Bloque actual de concentración', bg=c['soft'], fg=c['muted'], font=self.app_font(11, 'bold')).pack(pady=(0, 2)); config = tk.Frame(pomo_body, bg=c['card']); config.pack(fill='x', pady=8)
    for col in range(7):
        config.grid_columnconfigure(col, weight=1, uniform='pomodoro_config')
    tk.Label(config, text='Estudio', bg=c['card'], fg=c['text'], font=self.app_font(10, 'bold')).grid(row=0, column=0, padx=4, sticky='e'); self.study_entry = tk.Entry(config, width=6, justify='center', font=self.app_font(11), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary']); self.study_entry.grid(row=0, column=1, padx=4, ipady=5, sticky='ew'); tk.Label(config, text='Descanso', bg=c['card'], fg=c['text'], font=self.app_font(10, 'bold')).grid(row=0, column=2, padx=4, sticky='e'); self.break_entry = tk.Entry(config, width=6, justify='center', font=self.app_font(11), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary']); self.break_entry.grid(row=0, column=3, padx=4, ipady=5, sticky='ew')
    tk.Label(config, text='Largo', bg=c['card'], fg=c['text'], font=self.app_font(10, 'bold')).grid(row=0, column=4, padx=4, sticky='e'); self.long_break_entry = tk.Entry(config, width=6, justify='center', font=self.app_font(11), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary']); self.long_break_entry.grid(row=0, column=5, padx=4, ipady=5, sticky='ew'); tk.Button(config, text='Guardar', command=self.save_pomodoro_settings, bg='#cfe8ff', relief='flat', bd=0, font=self.app_font(10, 'bold')).grid(row=0, column=6, padx=4, ipady=6, sticky='ew'); buttons = tk.Frame(pomo_body, bg=c['card']); buttons.pack(fill='x', pady=(12, 4))
    tk.Button(buttons, text='▶ Estudiar', command=self.start_study_timer, bg=c['primary'], fg='white', relief='flat', bd=0, font=self.app_font(13, 'bold')).pack(side='left', fill='x', expand=True, padx=4, ipady=12); tk.Button(buttons, text='☕ Descanso', command=self.start_break_timer, bg='#e4d5ff', relief='flat', bd=0, font=self.app_font(11, 'bold')).pack(side='left', fill='x', expand=True, padx=4, ipady=10); tk.Button(buttons, text='🌙 Largo', command=self.start_long_break_timer, bg='#d8cbff', relief='flat', bd=0, font=self.app_font(11, 'bold')).pack(side='left', fill='x', expand=True, padx=4, ipady=10); tk.Button(buttons, text='⏸ Pausa', command=self.pause_timer, bg='#fff1b8', relief='flat', bd=0, font=self.app_font(11, 'bold')).pack(side='left', fill='x', expand=True, padx=4, ipady=10)
    tk.Button(buttons, text='🔄 Reiniciar', command=self.reset_timer, bg=c['danger'], relief='flat', bd=0, font=self.app_font(11, 'bold')).pack(side='left', fill='x', expand=True, padx=4, ipady=10); games = self.card(right, 'Arcade del michi · juegos más divertidos', '🎮'); games.pack(fill='x', pady=(6, 4)); games_body = self.card_content(games); tk.Label(games_body, text='Descansos rápidos con premios.', bg=c['card'], fg=c['muted'], font=self.app_font(9, 'bold')).pack(anchor='center', pady=(0, 5))
    for text_btn, cmd, bg in [('🏃 Michi Runner', self.open_runner_game, '#ffd9e8'), ('🛹 Michi Skater', self.open_skater_game, '#d7ecff'), ('🧺 Atrapa fresas', self.open_catch_game, '#d6f5df'), ('🎈 Bubble Pop', self.open_bubble_pop_game, '#fff1b8'), ('🃏 Flash Quiz', self.practice_flashcards_quiz, '#e4d5ff')]:
        tk.Button(games_body, text=text_btn, command=cmd, bg=bg, fg=c['text'], relief='flat', bd=0, activebackground=c['secondary'], font=self.app_font(10, 'bold'), cursor='hand2', anchor='center').pack(fill='x', pady=3, ipady=7)
    self.game_status = tk.Label(games_body, text='', bg=c['card'], fg=c['muted'], wraplength=450, justify='center', font=self.app_font(9, 'bold')); self.game_status.pack(fill='x', pady=(3, 0)); tools = self.card(right, 'Herramientas para estudiar', '🧰'); tools.pack(fill='both', expand=True, pady=(4, 6)); tools_body = self.card_content(tools); self.study_search_entry = tk.Entry(tools_body, font=self.app_font(11), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary']); self.study_search_entry.pack(fill='x', pady=(0, 8), ipady=8); self.study_search_entry.insert(0, 'Buscar tema o material en Google...'); row = tk.Frame(tools_body, bg=c['card']); row.pack(fill='x', pady=(0, 12))
    for col in range(4):
        row.grid_columnconfigure(col, weight=1, uniform='study_links')
    tk.Button(row, text='🔎 Google', command=lambda: self.search_google(self.study_search_entry), bg='#cfe8ff', relief='flat', bd=0, font=self.app_font(11, 'bold'), cursor='hand2').grid(row=0, column=0, sticky='ew', padx=(0, 4), ipady=7); tk.Button(row, text='🎧 Spotify', command=self.open_spotify, bg='#b9f2c8', relief='flat', bd=0, font=self.app_font(11, 'bold'), cursor='hand2').grid(row=0, column=1, sticky='ew', padx=4, ipady=7); tk.Button(row, text='▶ YouTube', command=self.open_youtube, bg='#ffbcbc', relief='flat', bd=0, font=self.app_font(11, 'bold'), cursor='hand2').grid(row=0, column=2, sticky='ew', padx=4, ipady=7)
    tk.Button(row, text='📚 Classroom', command=lambda: self.open_url('https://classroom.google.com'), bg='#ead7ff', relief='flat', bd=0, font=self.app_font(11, 'bold'), cursor='hand2').grid(row=0, column=3, sticky='ew', padx=(4, 0), ipady=7); tk.Label(tools_body, text='Plan de estudio de hoy', bg=c['card'], fg=c['text'], font=self.app_font(11, 'bold')).pack(anchor='w', pady=(6, 3)); self.study_plan_text = tk.Text(tools_body, height=3, wrap='word', font=self.app_font(9), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary'], padx=8, pady=5); self.study_plan_text.pack(fill='x', pady=(0, 6)); tk.Button(tools_body, text='Guardar plan', command=self.save_study_plan, bg=c['accent'], relief='flat', bd=0, font=self.app_font(11, 'bold'), cursor='hand2').pack(fill='x', pady=(0, 10), ipady=7)
    tk.Label(tools_body, text='Bloc de notas rápido', bg=c['card'], fg=c['text'], font=self.app_font(11, 'bold')).pack(anchor='w', pady=(4, 3)); self.scratch_text = tk.Text(tools_body, height=3, wrap='word', font=self.app_font(9), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary'], padx=8, pady=5); self.scratch_text.pack(fill='x', pady=(0, 6)); tk.Button(tools_body, text='Guardar bloc', command=self.save_quick_scratch, bg='#cfe8ff', relief='flat', bd=0, font=self.app_font(11, 'bold'), cursor='hand2').pack(fill='x', pady=(0, 4), ipady=7)

def update_arcade_best(self, key, score):
    bests = self.user_data.setdefault('arcade_best', {}); previous = int(bests.get(key, 0) or 0)
    if int(score) > previous:
        bests[key] = int(score); self.save(); return True
    return False

def refresh_game_status_v3(self):
    wins = self.user_data.get('metrics', {}).get('mini_games_won', 0); bests = self.user_data.get('arcade_best', {}); text = f"🏆 Ganadas: {wins}   🏃 {bests.get('runner_pro', bests.get('runner', 0))}   🛹 {bests.get('skater', 0)}   🧺 {bests.get('catch', 0)}   🎈 {bests.get('bubble_pop', 0)}   🃏 {bests.get('flash_quiz', 0)}"
    if hasattr(self, 'game_status'):
        self.game_status.config(text=text)

def bulk_add_flashcards(self):
    subject = self.selected_subject()
    if not subject:
        messagebox.showerror('Flashcards', 'Selecciona una materia.'); return
    c = self.palette(); win = tk.Toplevel(self.root); win.title('Importar flashcards'); win.geometry('560x470'); win.configure(bg=c['bg']); tk.Label(win, text=f'Importar lote · {subject}', bg=c['bg'], fg=c['primary'], font=('Arial', 15, 'bold')).pack(pady=10); tk.Label(win, text='Pega una ficha por línea con este formato: pregunta | respuesta | categoría(opcional)', bg=c['bg'], fg=c['text'], wraplength=500, justify='left').pack(padx=18); cat_row = tk.Frame(win, bg=c['bg']); cat_row.pack(fill='x', padx=18, pady=6); tk.Label(cat_row, text='Categoría por defecto', bg=c['bg'], fg=c['text']).pack(side='left'); default_cat = tk.StringVar(value=self.flash_category_var.get() if hasattr(self, 'flash_category_var') else 'General')
    ttk.Combobox(cat_row, textvariable=default_cat, values=self.user_data.get('flashcard_categories', ['General']), state='readonly', width=18).pack(side='left', padx=6); box = tk.Text(win, wrap='word', height=16); box.pack(fill='both', expand=True, padx=18, pady=8); box.insert('1.0', 'Capital de Francia | París | Geografía\nMitocondria | Produce energía en la célula | Biología')

    def save_bulk():
        raw = box.get('1.0', tk.END).strip()
        if not raw:
            messagebox.showerror('Flashcards', 'Pega al menos una línea.'); return
        cards = self.subject_data(subject).setdefault('flashcards', []); cats = self.user_data.setdefault('flashcard_categories', ['General']); added = 0
        for line in raw.splitlines():
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = [p.strip() for p in line.split('|')]
            if len(parts) < 2:
                parts = [p.strip() for p in line.split('\t')]
            if len(parts) < 2:
                continue
            q, a = (parts[0], parts[1]); cat = parts[2] if len(parts) >= 3 and parts[2] else default_cat.get() or 'General'
            if cat not in cats:
                cats.append(cat)
            cards.append({'q': q, 'a': a, 'category': cat, 'stats': {'ok': 0, 'review': 0, 'seen': 0, 'last_review': ''}}); added += 1
        if not added:
            messagebox.showerror('Flashcards', 'No pude leer líneas válidas. Usa pregunta | respuesta | categoría.'); return
        self.save(); self.load_selected_subject(); win.destroy(); messagebox.showinfo('Flashcards', f'Se importaron {added} fichas.')
    tk.Button(win, text='Importar fichas', command=save_bulk, bg=c['accent']).pack(fill='x', padx=18, pady=(0, 12))

def practice_flashcards_quiz(self):
    subject = self.selected_subject()
    if not subject:
        messagebox.showerror('Flash Quiz', 'Selecciona una materia para usar sus flashcards.'); return
    cards = list(self.subject_data(subject).get('flashcards', []))
    if hasattr(self, 'flash_category_filter_var'):
        selected = self.flash_category_filter_var.get()
        if selected and selected != 'Todas':
            cards = [c for c in cards if c.get('category', 'General') == selected]
    if len(cards) < 2:
        messagebox.showinfo('Flash Quiz', 'Necesitas al menos 2 fichas para jugar este modo.'); return
    c = self.palette(); win = tk.Toplevel(self.root); win.title(f'Flash Quiz · {subject}'); win.geometry('620x520'); win.configure(bg=c['bg']); tk.Label(win, text=f'Flash Quiz · {subject}', bg=c['bg'], fg=c['primary'], font=('Arial', 16, 'bold')).pack(pady=10); info = tk.Label(win, text='', bg=c['bg'], fg=c['muted'], font=('Arial', 10, 'bold')); info.pack(); question = tk.Label(win, text='', bg=c['bg'], fg=c['text'], wraplength=520, justify='center', font=('Arial', 18, 'bold')); question.pack(fill='x', padx=20, pady=18); feedback = tk.Label(win, text='', bg=c['bg'], fg=c['primary'], font=('Arial', 11, 'bold')); feedback.pack(); opts_frame = tk.Frame(win, bg=c['bg']); opts_frame.pack(fill='both', expand=True, padx=22, pady=12); option_buttons = []
    for _ in range(4):
        btn = tk.Button(opts_frame, text='', wraplength=480, height=2, bg='#fffdfd'); btn.pack(fill='x', pady=5); option_buttons.append(btn)
    order = random.sample(cards, min(8, len(cards))); state = {'idx': 0, 'score': 0}

    def render_question():
        if state['idx'] >= len(order):
            end_quiz(); return
        card = order[state['idx']]; info.config(text=f"Pregunta {state['idx'] + 1} de {len(order)} · Puntaje: {state['score']}"); question.config(text=card.get('q', '')); feedback.config(text=''); answers = [c.get('a', '') for c in cards if c is not card and c.get('a', '') != card.get('a', '')]; random.shuffle(answers); options = [card.get('a', '')] + answers[:3]
        while len(options) < 4:
            options.append(card.get('a', ''))
        random.shuffle(options)
        for btn, text_btn in zip(option_buttons, options):
            btn.configure(text=text_btn, state='normal', command=lambda ans=text_btn, expected=card.get('a', ''): answer(ans, expected))

    def answer(chosen, expected):
        for btn in option_buttons:
            btn.configure(state='disabled')
        current = order[state['idx']]; stats = current.setdefault('stats', {'ok': 0, 'review': 0, 'seen': 0, 'last_review': ''}); stats['seen'] = int(stats.get('seen', 0)) + 1; stats['last_review'] = now_string(); self.user_data['metrics']['flashcards_practiced'] = int(self.user_data.get('metrics', {}).get('flashcards_practiced', 0)) + 1
        if chosen == expected:
            state['score'] += 1; stats['ok'] = int(stats.get('ok', 0)) + 1; feedback.config(text='¡Correcto! +1 punto')
        else:
            stats['review'] = int(stats.get('review', 0)) + 1; feedback.config(text=f'Casi. La respuesta correcta era: {expected}')
        self.save(); self.load_selected_subject(); win.after(850, next_question)

    def next_question():
        state['idx'] += 1; render_question()

    def end_quiz():
        best = self.update_arcade_best('flash_quiz', state['score']); reward_fresas = max(4, state['score'] * 2); reward_xp = max(8, state['score'] * 4); self.user_data['metrics']['mini_games_won'] = int(self.user_data.get('metrics', {}).get('mini_games_won', 0)) + 1; self.add_rewards(fresas=reward_fresas, xp=reward_xp, pet_xp=max(4, state['score'] * 2)); self.save(); self.refresh_all(); question.config(text=f"Fin del Flash Quiz ✨\n\nPuntaje: {state['score']} / {len(order)}"); info.config(text=f'Ganaste {reward_fresas}🍓 y {reward_xp} XP' + (' · Nuevo récord' if best else '')); feedback.config(text='Puedes cerrar la ventana o volver a jugar más tarde.')
        for btn in option_buttons:
            btn.destroy()
    render_question()

def open_bubble_pop_game(self):
    c = self.palette(); win = tk.Toplevel(self.root); win.title('Bubble Pop'); win.geometry('520x560'); win.configure(bg=c['bg']); tk.Label(win, text='Bubble Pop', bg=c['bg'], fg=c['primary'], font=('Arial', 18, 'bold')).pack(pady=(10, 4)); tk.Label(win, text='Haz click en las burbujas buenas y evita las bombas.', bg=c['bg'], fg=c['muted']).pack(); canvas = tk.Canvas(win, width=490, height=420, bg='#fff8fb', highlightthickness=0); canvas.pack(pady=10); status = tk.Label(win, text='', bg=c['bg'], fg=c['text'], font=('Arial', 10, 'bold')); status.pack(); state = {'score': 0, 'lives': 3, 'time': 25, 'running': True}; bubbles = []

    def spawn():
        kind = random.choices(['berry', 'book', 'star', 'bomb'], weights=[45, 25, 18, 12])[0]; radius = random.randint(22, 32); bubbles.append({'x': random.randint(radius + 10, 480 - radius), 'y': 440 + radius, 'r': radius, 'speed': random.uniform(2.0, 4.2), 'kind': kind})

    def draw():
        canvas.delete('all')
        for i in range(0, 520, 52):
            canvas.create_text((i + state['score'] * 7) % 520, 26 + i % 60, text='✨', font=('Arial', 12), fill='#f3cbd8')
        for bubble in bubbles:
            x, y, r, kind = (bubble['x'], bubble['y'], bubble['r'], bubble['kind']); fill = {'berry': '#ffd9e8', 'book': '#d7ecff', 'star': '#fff1b8', 'bomb': '#d9dce4'}[kind]; label = {'berry': '🍓', 'book': '📚', 'star': '⭐', 'bomb': '💣'}[kind]; canvas.create_oval(x - r, y - r, x + r, y + r, fill=fill, outline='#ffffff', width=2); canvas.create_text(x, y, text=label, font=('Arial', 18))
        status.config(text=f"Puntos: {state['score']} · Vidas: {state['lives']} · Tiempo: {state['time']}s")

    def finish():
        if not state['running']:
            return
        state['running'] = False; best = self.update_arcade_best('bubble_pop', state['score']); reward_fresas = max(5, state['score']); reward_xp = max(8, state['score'] * 2); self.user_data['metrics']['mini_games_won'] = int(self.user_data.get('metrics', {}).get('mini_games_won', 0)) + 1; self.add_rewards(fresas=reward_fresas, xp=reward_xp, pet_xp=max(4, state['score'])); self.save(); self.refresh_all(); canvas.create_rectangle(95, 150, 395, 260, fill='#ffffff', outline=c['secondary'], width=2); canvas.create_text(245, 180, text='Fin del juego', font=('Arial', 18, 'bold'), fill=c['primary']); canvas.create_text(245, 213, text=f"Puntaje: {state['score']} · Ganaste {reward_fresas}🍓 y {reward_xp} XP", font=('Arial', 11), fill=c['text'], width=250)
        canvas.create_text(245, 240, text='Nuevo récord ✨' if best else 'Cierra la ventana para salir.', font=('Arial', 10), fill=c['muted'])

    def tick():
        if not state['running'] or not win.winfo_exists():
            return
        state['time'] -= 1
        if state['time'] <= 0:
            draw(); finish(); return
        win.after(1000, tick)

    def animate():
        if not state['running'] or not win.winfo_exists():
            return
        if random.random() < 0.22:
            spawn()
        keep = []
        for bubble in bubbles:
            bubble['y'] -= bubble['speed']
            if bubble['y'] + bubble['r'] < -5:
                if bubble['kind'] != 'bomb':
                    state['lives'] -= 1
                if state['lives'] <= 0:
                    draw(); finish(); return
                continue
            keep.append(bubble)
        bubbles[:] = keep; draw(); win.after(45, animate)

    def click(event):
        if not state['running']:
            return
        hit = None
        for bubble in reversed(bubbles):
            if (event.x - bubble['x']) ** 2 + (event.y - bubble['y']) ** 2 <= bubble['r'] ** 2:
                hit = bubble; break
        if not hit:
            return
        bubbles.remove(hit)
        if hit['kind'] == 'berry':
            state['score'] += 1
        elif hit['kind'] == 'book':
            state['score'] += 2
        elif hit['kind'] == 'star':
            state['score'] += 3
        else:
            state['lives'] -= 1
        if state['lives'] <= 0:
            draw(); finish(); return
        draw()
    canvas.bind('<Button-1>', click); draw(); tick(); animate()

def add_arcade_extra_panel_v3(self):
    return

def _ms_v4_today():
    return today_string()

def _ms_v4_default_missions():
    return [{'id': 'pomodoro', 'icon': '🍅', 'title': 'Completa 1 pomodoro', 'goal': 1, 'progress': 0, 'reward_fresas': 25, 'reward_xp': 35, 'done': False}, {'id': 'tasks', 'icon': '✅', 'title': 'Completa 3 tareas', 'goal': 3, 'progress': 0, 'reward_fresas': 30, 'reward_xp': 35, 'done': False}, {'id': 'flashcards', 'icon': '🃏', 'title': 'Practica 10 fichas', 'goal': 10, 'progress': 0, 'reward_fresas': 35, 'reward_xp': 45, 'done': False}, {'id': 'mood', 'icon': '🌈', 'title': 'Registra tu mood', 'goal': 1, 'progress': 0, 'reward_fresas': 15, 'reward_xp': 20, 'done': False}, {'id': 'arcade', 'icon': '🎮', 'title': 'Juega 1 minijuego', 'goal': 1, 'progress': 0, 'reward_fresas': 20, 'reward_xp': 25, 'done': False}]

def _ms_v4_ensure_schema(self):
    _ms_v4_prev_ensure_schema(self); self.user_data.setdefault('daily_missions', {'date': _ms_v4_today(), 'missions': _ms_v4_default_missions()})
    if self.user_data['daily_missions'].get('date') != _ms_v4_today():
        self.user_data['daily_missions'] = {'date': _ms_v4_today(), 'missions': _ms_v4_default_missions()}
    self.user_data.setdefault('arcade_best', {}); self.user_data['arcade_best'].setdefault('runner_pro', 0); self.user_data.setdefault('unlocked_collections', []); self.user_data.setdefault('backup_log', []); self.user_data.setdefault('pro_feedback', [])
    for subject, data in self.user_data.get('subjects', {}).items():
        for card in data.get('flashcards', []):
            card.setdefault('difficulty', 'Normal'); card.setdefault('favorite', False); card.setdefault('interval', 1); card.setdefault('ease', 2.3); card.setdefault('next_review', today_string()); card.setdefault('stats', {'ok': 0, 'review': 0, 'seen': 0, 'last_review': ''})
    self.save()

def _ms_v4_save(self):
    try:
        stamp = datetime.now().strftime('%Y%m%d_%H'); key = f'autosave_{stamp}'
        if self.current_user and self.user_data is not None and (key not in self.user_data.get('backup_log', [])):
            if os.path.exists(DATA_FILE):
                backup = f'michi_studio_autobackup_{self.current_user}_{stamp}.json'; shutil.copy(DATA_FILE, backup); self.user_data.setdefault('backup_log', []).append(key); self.user_data['backup_log'] = self.user_data['backup_log'][-24:]
    except Exception:
        pass
    return _ms_v4_prev_save(self)

def _ms_v4_build_main_ui(self):
    _ms_v4_prev_build_main_ui(self)
    try:
        header = self.root.winfo_children()[0]; tk.Button(header, text='Misiones', command=self.open_daily_missions_window, bg='white').pack(side='right', padx=4); tk.Button(header, text='Backup', command=self.open_backup_manager, bg='white').pack(side='right', padx=4); tk.Button(header, text='Pro', command=self.open_pro_dashboard, bg='white').pack(side='right', padx=4)
    except Exception:
        pass

def _ms_v4_missions(self):
    dm = self.user_data.setdefault('daily_missions', {'date': _ms_v4_today(), 'missions': _ms_v4_default_missions()})
    if dm.get('date') != _ms_v4_today():
        dm.clear(); dm.update({'date': _ms_v4_today(), 'missions': _ms_v4_default_missions()})
    return dm['missions']

def _ms_v4_update_mission(self, mission_id, amount=1):
    try:
        for m in self.get_daily_missions():
            if m.get('id') == mission_id and (not m.get('done')):
                m['progress'] = min(int(m.get('goal', 1)), int(m.get('progress', 0)) + int(amount))
        self.save()
    except Exception:
        pass

def _ms_v4_claim_mission(self, mission_id):
    for m in self.get_daily_missions():
        if m.get('id') == mission_id:
            if m.get('done'):
                messagebox.showinfo('Misiones', 'Ya reclamaste esta misión.'); return
            if int(m.get('progress', 0)) < int(m.get('goal', 1)):
                messagebox.showinfo('Misiones', 'Aún no está completa.'); return
            m['done'] = True; self.add_rewards(fresas=int(m.get('reward_fresas', 0)), xp=int(m.get('reward_xp', 0)), pet_xp=10); self.add_achievement(f"Misión diaria: {m.get('title', '')}"); self.save(); self.refresh_all(); messagebox.showinfo('Misiones', f"Recompensa reclamada: +{m['reward_fresas']}🍓 +{m['reward_xp']} XP"); return

def _ms_v4_open_missions(self):
    c = self.palette(); win = tk.Toplevel(self.root); win.title('Misiones diarias'); win.geometry('560x430'); win.configure(bg=c['bg']); tk.Label(win, text='Misiones diarias Pro', bg=c['bg'], fg=c['primary'], font=('Arial', 18, 'bold')).pack(pady=12); holder = tk.Frame(win, bg=c['bg']); holder.pack(fill='both', expand=True, padx=15, pady=5)
    for m in self.get_daily_missions():
        row = tk.Frame(holder, bg=c['card'], highlightbackground=c['secondary'], highlightthickness=1, padx=10, pady=8); row.pack(fill='x', pady=5); pct = f"{m.get('progress', 0)}/{m.get('goal', 1)}"; status = 'Reclamada' if m.get('done') else 'Lista' if m.get('progress', 0) >= m.get('goal', 1) else 'Pendiente'; tk.Label(row, text=f"{m.get('icon', '⭐')} {m.get('title', '')} · {pct} · {status}", bg=c['card'], fg=c['text'], font=('Arial', 10, 'bold')).pack(side='left', fill='x', expand=True, anchor='w'); tk.Button(row, text='Reclamar', command=lambda mid=m.get('id'): self.claim_mission(mid), bg=c['accent']).pack(side='right')

def _ms_v4_backup_manager(self):
    c = self.palette(); win = tk.Toplevel(self.root); win.title('Backups'); win.geometry('500x340'); win.configure(bg=c['bg']); tk.Label(win, text='Centro de backups', bg=c['bg'], fg=c['primary'], font=('Arial', 16, 'bold')).pack(pady=12); info = tk.Label(win, text='Crea respaldos manuales o restaura un JSON exportado.', bg=c['bg'], fg=c['text'], wraplength=440); info.pack(padx=20, pady=6)

    def manual_backup():
        filename = f"michi_studio_backup_{self.current_user}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as fh:
            json.dump(self.user_data, fh, indent=4, ensure_ascii=False)
        messagebox.showinfo('Backup', f'Backup creado:\n{filename}')
    tk.Button(win, text='Crear backup manual', command=manual_backup, bg=c['accent']).pack(fill='x', padx=35, pady=8); tk.Button(win, text='Importar backup', command=self.import_backup, bg='#e4d5ff').pack(fill='x', padx=35, pady=8); tk.Button(win, text='Exportar datos', command=self.export_user_data, bg='#cfe8ff').pack(fill='x', padx=35, pady=8)

def _ms_v4_pro_dashboard(self):
    c = self.palette(); best = self.user_data.get('arcade_best', {}); win = tk.Toplevel(self.root); win.title('Michi Studio Pro'); win.geometry('580x470'); win.configure(bg=c['bg']); tk.Label(win, text='Panel Pro', bg=c['bg'], fg=c['primary'], font=('Arial', 18, 'bold')).pack(pady=10); txt = tk.Text(win, wrap='word', height=18); txt.pack(fill='both', expand=True, padx=18, pady=8); missions_done = len([m for m in self.get_daily_missions() if m.get('done')])
    content = f"Mejoras Pro activas:\n\n• Misiones diarias con recompensas.\n• Runner Pro con power-ups, niveles, vidas, fresas y récord.\n• Flashcards con dificultad, favoritos y repaso espaciado.\n• Tienda con rarezas, colecciones y vista previa.\n• Backups automáticos por hora y backup manual.\n• Michi con más estados visuales y animaciones en canvas.\n\nMisiones reclamadas hoy: {missions_done}/{len(self.get_daily_missions())}\nRécord Runner Pro: {best.get('runner_pro', 0)}\nRécord Bubble Pop: {best.get('bubble_pop', 0)}\n"; txt.insert('1.0', content); txt.configure(state='disabled')

def _ms_v4_runner(self):
    c = self.palette(); win = tk.Toplevel(self.root); win.title('Michi Runner Pro'); win.geometry('470x660'); win.configure(bg=c['bg']); win.resizable(False, False); tk.Label(win, text='Michi Runner Pro', bg=c['bg'], fg=c['primary'], font=('Arial', 18, 'bold')).pack(pady=(10, 2)); tk.Label(win, text='← → para cambiar carril · espacio para saltar · junta fresas y power-ups', bg=c['bg'], fg=c['muted'], wraplength=420).pack(); canvas = tk.Canvas(win, width=420, height=540, bg='#fff8fb', highlightthickness=0); canvas.pack(pady=8); lanes = [105, 210, 315]; state = {'lane': 1, 'y': 465, 'jump': 0, 'vy': 0, 'score': 0, 'coins': 0, 'lives': 3, 'speed': 7, 'level': 1, 'shield': 0, 'magnet': 0, 'running': True, 'tick': 0}; objs = []

    def spawn():
        kind = random.choices(['box', 'cone', 'coin', 'heart', 'shield', 'magnet'], [38, 25, 28, 3, 3, 3])[0]; objs.append({'lane': random.randrange(3), 'y': -30, 'kind': kind})

    def draw():
        canvas.delete('all'); canvas.create_rectangle(55, 0, 365, 540, fill='#dfe8f2', outline='')
        for xline in [155, 265]:
            for yy in range(-40, 580, 55):
                canvas.create_rectangle(xline, yy + state['tick'] % 55, xline + 5, yy + 28 + state['tick'] % 55, fill='white', outline='')
        canvas.create_text(10, 10, anchor='nw', text=f"Puntos {state['score']} · 🍓 {state['coins']} · Vidas {state['lives']} · Nivel {state['level']}", font=('Arial', 10, 'bold'), fill=c['text'])
        if state['shield'] > 0:
            canvas.create_text(15, 34, anchor='nw', text=f"🛡 {state['shield']}", font=('Arial', 10), fill=c['primary'])
        if state['magnet'] > 0:
            canvas.create_text(72, 34, anchor='nw', text=f"🧲 {state['magnet']}", font=('Arial', 10), fill=c['primary'])
        px = lanes[state['lane']]; py = state['y']; canvas.create_oval(px - 24, py - 48, px + 24, py, fill='#ff6b98' if state['shield'] > 0 else '#fffdfd', outline=c['primary'], width=2); canvas.create_text(px, py - 25, text='🐱', font=('Arial', 27))
        for o in objs:
            ox = lanes[o['lane']]; oy = o['y']; labels = {'box': '📦', 'cone': '🚧', 'coin': '🍓', 'heart': '💖', 'shield': '🛡', 'magnet': '🧲'}; canvas.create_text(ox, oy, text=labels[o['kind']], font=('Arial', 23))

    def finish():
        state['running'] = False; best = self.update_arcade_best('runner_pro', state['score']); self.update_mission_progress('arcade', 1); rf = max(10, state['coins'] + state['score'] // 20); rx = max(15, state['score'] // 3); self.user_data['metrics']['mini_games_won'] = int(self.user_data.get('metrics', {}).get('mini_games_won', 0)) + 1; self.add_rewards(fresas=rf, xp=rx, pet_xp=rx // 2); self.refresh_all(); canvas.create_rectangle(65, 205, 355, 330, fill='white', outline=c['secondary'], width=2); canvas.create_text(210, 235, text='Fin del juego', font=('Arial', 18, 'bold'), fill=c['primary']); canvas.create_text(210, 270, text=f"Puntaje {state['score']} · +{rf}🍓 +{rx} XP", font=('Arial', 11), fill=c['text']); canvas.create_text(210, 303, text='Nuevo récord ✨' if best else 'Sigue practicando', font=('Arial', 10), fill=c['muted'])

    def step():
        if not state['running'] or not win.winfo_exists():
            return
        state['tick'] += 1; state['score'] += 1
        if state['score'] % 140 == 0:
            state['level'] += 1; state['speed'] += 1
        if random.random() < 0.1 + min(0.06, state['level'] * 0.01):
            spawn()
        if state['jump']:
            state['y'] += state['vy']; state['vy'] += 2
            if state['y'] >= 465:
                state['y'] = 465; state['jump'] = 0; state['vy'] = 0
        if state['shield'] > 0:
            state['shield'] -= 1
        if state['magnet'] > 0:
            state['magnet'] -= 1
        keep = []
        for o in objs:
            o['y'] += state['speed']; hit = o['lane'] == state['lane'] and abs(o['y'] - (state['y'] - 25)) < 36; near = state['magnet'] > 0 and o['kind'] == 'coin' and (abs(o['y'] - (state['y'] - 25)) < 80)
            if hit or near:
                if o['kind'] == 'coin':
                    state['coins'] += 1; state['score'] += 15; continue
                if o['kind'] == 'heart':
                    state['lives'] = min(5, state['lives'] + 1); continue
                if o['kind'] == 'shield':
                    state['shield'] = 120; continue
                if o['kind'] == 'magnet':
                    state['magnet'] = 150; continue
                if state['jump'] and state['y'] < 430:
                    keep.append(o); continue
                if state['shield'] > 0:
                    state['shield'] = 0; continue
                state['lives'] -= 1
                if state['lives'] <= 0:
                    draw(); finish(); return
                continue
            if o['y'] < 570:
                keep.append(o)
        objs[:] = keep; draw(); win.after(38, step)

    def key(e):
        if e.keysym in ('Left', 'a', 'A') and state['lane'] > 0:
            state['lane'] -= 1
        elif e.keysym in ('Right', 'd', 'D') and state['lane'] < 2:
            state['lane'] += 1
        elif e.keysym in ('space', 'Up', 'w', 'W') and (not state['jump']):
            state['jump'] = 1; state['vy'] = -24
        draw()
    win.bind('<Left>', key); win.bind('<Right>', key); win.bind('<space>', key); win.bind('<Up>', key); win.bind('<a>', key); win.bind('<d>', key); win.focus_force(); draw(); step()

def _ms_v4_shop_items(self):
    items = _ms_v4_prev_shop_items(self); extra = [{'name': 'Colección Sakura', 'icon': '🌸', 'slot': 'palette', 'price': 120, 'rarity': 'Épico', 'collection': 'Sakura', 'effect': 'Desbloquea look sakura', 'hood_color': 'Rosa chicle', 'dress_color': 'Lavanda'}, {'name': 'Colección Galaxia', 'icon': '🌌', 'slot': 'palette', 'price': 140, 'rarity': 'Legendario', 'collection': 'Galaxia', 'effect': 'Look galaxia', 'hood_color': 'Lavanda', 'dress_color': 'Azul cielo'}, {'name': 'Patines del runner', 'icon': '🛼', 'slot': 'accessory', 'price': 100, 'rarity': 'Raro', 'collection': 'Arcade', 'effect': 'Accesorio arcade'}, {'name': 'Mochila pro', 'icon': '🎒', 'slot': 'accessory', 'price': 90, 'rarity': 'Raro', 'collection': 'Estudio', 'effect': 'Para estudiar con estilo'}]
    for it in items:
        it.setdefault('rarity', 'Común'); it.setdefault('collection', 'Básica')
    return items + extra

def _ms_v4_complete_task(self):
    before = len([t for t in self.user_data.get('tasks', []) if t.get('done')]); _ms_v4_prev_complete_task(self); after = len([t for t in self.user_data.get('tasks', []) if t.get('done')])
    if after > before:
        self.update_mission_progress('tasks', after - before)

def _ms_v4_finish_timer(self, mode):
    _ms_v4_prev_finish_timer(self, mode)
    if mode == 'study':
        self.update_mission_progress('pomodoro', 1)

def _ms_v5_ensure_schema(self):
    _ms_v4_ensure_schema(self)
    for subject, data in self.user_data.get('subjects', {}).items():
        for card in data.get('flashcards', []):
            card.setdefault('created_at', now_string()); card.setdefault('difficulty', card.get('difficulty', 'Normal')); card.setdefault('tags', card.get('category', '')); card.setdefault('favorite', False); card.setdefault('due', card.get('next_review', today_string())); card.setdefault('next_review', card.get('due', today_string())); card.setdefault('interval', safe_int(card.get('interval', 0), 0)); card.setdefault('ease', safe_float(card.get('ease', 2.5), 2.5)); card.setdefault('reviews', safe_int(card.get('reviews', 0), 0)); card.setdefault('correct', safe_int(card.get('correct', 0), 0)); card.setdefault('lapses', safe_int(card.get('lapses', 0), 0)); card.setdefault('last_review', '')
    self.save()

def _ms_v5_add_flashcard(self):
    subject = self.selected_subject()
    if not subject:
        messagebox.showerror('Flashcards', 'Selecciona una materia.'); return
    q = self.flash_q_entry.get().strip(); a = self.flash_a_entry.get().strip()
    if not q or q == 'Pregunta' or (not a) or (a == 'Respuesta'):
        messagebox.showerror('Flashcards', 'Escribe pregunta y respuesta.'); return
    tags = self.flash_tags_entry.get().strip() if hasattr(self, 'flash_tags_entry') else ''
    if tags.startswith('Tags:'):
        tags = ''
    difficulty = self.flash_difficulty_var.get() if hasattr(self, 'flash_difficulty_var') else 'Normal'; category = tags.split(',')[0].strip() if tags else 'General'; self.subject_data(subject).setdefault('flashcards', []).append({'q': q, 'a': a, 'category': category, 'difficulty': difficulty, 'tags': tags, 'favorite': False, 'created_at': now_string(), 'due': today_string(), 'next_review': today_string(), 'interval': 0, 'ease': 2.5, 'reviews': 0, 'correct': 0, 'lapses': 0, 'last_review': '', 'stats': {'ok': 0, 'review': 0, 'seen': 0, 'last_review': ''}}); self.flash_q_entry.delete(0, tk.END); self.flash_a_entry.delete(0, tk.END)
    if hasattr(self, 'flash_tags_entry'):
        self.flash_tags_entry.delete(0, tk.END); self.flash_tags_entry.insert(0, 'Tags: examen, vocabulario...')
    self.save(); self.load_selected_subject()

def _ms_v5_load_selected_subject(self):
    _ms_v3_prev_load_selected_subject(self); subject = self.selected_subject()
    if not subject:
        return
    data = self.subject_data(subject); cards = data.get('flashcards', []); today = date.today(); mode = self.flash_filter_var.get() if hasattr(self, 'flash_filter_var') else 'Todas'; filtered = []
    for idx, card in enumerate(cards):
        card.setdefault('due', card.get('next_review', today_string())); card.setdefault('next_review', card.get('due', today_string())); due_date = parse_date_string(card.get('due'), today)
        if mode == 'Para hoy' and due_date and (due_date > today):
            continue
        if mode == 'Favoritas' and (not card.get('favorite')):
            continue
        if mode == 'Difíciles' and card.get('difficulty') != 'Difícil' and (safe_int(card.get('lapses', 0), 0) < 2):
            continue
        filtered.append((idx, card))
    self._flash_index_map = [idx for idx, _ in filtered]; self.flash_list.delete(0, tk.END)
    for idx, card in filtered:
        due = card.get('due', today_string()); flag = '⭐' if card.get('favorite') else ''; status = '📌' if parse_date_string(due, today) <= today else '⏳'; preview = card.get('q', '').strip().replace('\n', ' ')
        if len(preview) > 42:
            preview = preview[:39] + '...'
        self.flash_list.insert(tk.END, f"{status}{flag} {preview} · {card.get('difficulty', 'Normal')} · due {due}")
    due_count = sum((1 for card in cards if parse_date_string(card.get('due', card.get('next_review')), today) <= today)); mastered = sum((1 for card in cards if safe_int(card.get('interval', 0), 0) >= 14))
    if hasattr(self, 'flash_stats_label'):
        self.flash_stats_label.config(text=f'Total: {len(cards)} · Para hoy: {due_count} · Dominadas: {mastered} · Filtro: {mode}')
    elif hasattr(self, 'flash_summary_label'):
        self.flash_summary_label.config(text=f'Total: {len(cards)} · Para hoy: {due_count} · Dominadas: {mastered} · Filtro: {mode}')

def _ms_v5_delete_flashcard(self):
    subject = self.selected_subject(); sel = self.flash_list.curselection()
    if not subject or not sel:
        messagebox.showerror('Flashcards', 'Selecciona una flashcard.'); return
    cards = self.subject_data(subject).get('flashcards', []); idx = self._flash_index_map[sel[0]] if hasattr(self, '_flash_index_map') and sel[0] < len(self._flash_index_map) else sel[0]
    if idx < len(cards):
        del cards[idx]; self.save(); self.load_selected_subject()

def _ms_v5_edit_flashcard(self):
    subject = self.selected_subject(); sel = self.flash_list.curselection()
    if not subject or not sel:
        messagebox.showerror('Flashcards', 'Selecciona una flashcard.'); return
    cards = self.subject_data(subject).get('flashcards', []); idx = self._flash_index_map[sel[0]] if hasattr(self, '_flash_index_map') and sel[0] < len(self._flash_index_map) else sel[0]
    if idx >= len(cards):
        return
    card = cards[idx]; c = self.palette(); win = tk.Toplevel(self.root); win.title('Editar flashcard'); win.geometry('470x410'); win.configure(bg=c['bg']); tk.Label(win, text='Editar flashcard', bg=c['bg'], fg=c['primary'], font=('Arial', 15, 'bold')).pack(pady=10); q = tk.Text(win, height=4, wrap='word'); q.pack(fill='x', padx=18, pady=4); q.insert('1.0', card.get('q', '')); a = tk.Text(win, height=5, wrap='word'); a.pack(fill='x', padx=18, pady=4); a.insert('1.0', card.get('a', '')); meta = tk.Frame(win, bg=c['bg']); meta.pack(fill='x', padx=18, pady=4); difficulty = tk.StringVar(value=card.get('difficulty', 'Normal')); ttk.Combobox(meta, textvariable=difficulty, values=['Fácil', 'Normal', 'Difícil'], state='readonly', width=10).pack(side='left'); favorite = tk.BooleanVar(value=bool(card.get('favorite')))
    tk.Checkbutton(meta, text='Favorita', variable=favorite, bg=c['bg'], fg=c['text']).pack(side='left', padx=10); tags = tk.Entry(win); tags.pack(fill='x', padx=18, pady=4); tags.insert(0, card.get('tags', card.get('category', '')))

    def save_edit():
        nq = q.get('1.0', tk.END).strip(); na = a.get('1.0', tk.END).strip()
        if not nq or not na:
            messagebox.showerror('Flashcards', 'Pregunta y respuesta no pueden quedar vacías.'); return
        card.update({'q': nq, 'a': na, 'difficulty': difficulty.get(), 'favorite': favorite.get(), 'tags': tags.get().strip(), 'category': tags.get().strip().split(',')[0] or 'General'}); self.save(); self.load_selected_subject(); win.destroy()
    tk.Button(win, text='Guardar cambios', command=save_edit, bg=c['accent']).pack(fill='x', padx=18, pady=10)

def _ms_v5_auto_flashcards_from_notes(self):
    subject = self.selected_subject()
    if not subject:
        messagebox.showerror('Flashcards', 'Selecciona una materia.'); return
    notes = self.subject_notes_text.get('1.0', tk.END).strip()
    if not notes:
        messagebox.showinfo('Flashcards', "Escribe apuntes primero. Tip: usa líneas tipo 'Concepto: definición'."); return
    cards = self.subject_data(subject).setdefault('flashcards', []); made = 0
    for raw in notes.splitlines():
        line = raw.strip(' •-*\t')
        if len(line) < 8:
            continue
        sep = ':' if ':' in line else ' - ' if ' - ' in line else None
        if not sep:
            continue
        left, right = [part.strip() for part in line.split(sep, 1)]
        if 2 <= len(left) <= 70 and len(right) >= 3:
            cards.append({'q': f'¿Qué es {left}?', 'a': right, 'category': 'auto', 'difficulty': 'Normal', 'tags': 'auto', 'favorite': False, 'created_at': now_string(), 'due': today_string(), 'next_review': today_string(), 'interval': 0, 'ease': 2.5, 'reviews': 0, 'correct': 0, 'lapses': 0, 'last_review': '', 'stats': {'ok': 0, 'review': 0, 'seen': 0, 'last_review': ''}}); made += 1
    if not made:
        messagebox.showinfo('Flashcards', 'No encontré líneas claras. Usa formato: Concepto: definición'); return
    self.save(); self.load_selected_subject(); messagebox.showinfo('Flashcards', f'Creé {made} flashcards desde tus apuntes.')

def _ms_v5_practice_flashcards(self, only_due=False):
    subject = self.selected_subject()
    if not subject:
        messagebox.showerror('Flashcards', 'Selecciona una materia.'); return
    all_cards = self.subject_data(subject).get('flashcards', [])
    if not all_cards:
        messagebox.showinfo('Flashcards', 'No hay fichas para practicar.'); return
    today = date.today(); pairs = [(idx, card) for idx, card in enumerate(all_cards)]
    if only_due:
        pairs = [(idx, card) for idx, card in pairs if parse_date_string(card.get('due', card.get('next_review')), today) <= today]
        if not pairs:
            messagebox.showinfo('Flashcards', 'No tienes fichas pendientes hoy. Michi está orgulloso ✨'); return
    pairs.sort(key=lambda item: (parse_date_string(item[1].get('due', item[1].get('next_review')), today), -safe_int(item[1].get('lapses', 0), 0))); cards = [card for _, card in pairs]; c = self.palette(); win = tk.Toplevel(self.root); win.title(f'Repaso inteligente · {subject}'); win.geometry('640x560'); win.configure(bg=c['bg']); tk.Label(win, text=f'Repaso inteligente · {subject}', bg=c['bg'], fg=c['primary'], font=('Arial', 16, 'bold')).pack(pady=10); tk.Label(win, text='Responde mentalmente, voltea y califica. Michi agenda el próximo repaso automáticamente.', bg=c['bg'], fg=c['muted'], wraplength=580, justify='center').pack(); state = {'index': 0, 'front': True, 'reviewed': 0, 'session_correct': 0}; box = tk.Frame(win, bg='#fffdfd', highlightbackground=c['secondary'], highlightthickness=2)
    box.pack(fill='both', expand=True, padx=34, pady=16); side = tk.Label(box, text='Pregunta', bg='#fffdfd', fg=c['primary'], font=('Arial', 11, 'bold')); side.pack(pady=(20, 5)); text = tk.Label(box, text='', bg='#fffdfd', fg=c['text'], font=('Arial', 18, 'bold'), wraplength=520, justify='center'); text.pack(expand=True, pady=20); meta = tk.Label(box, text='', bg='#fffdfd', fg=c['muted'], font=('Arial', 10, 'italic'), wraplength=520); meta.pack(pady=(0, 18)); status = tk.Label(win, text='', bg=c['bg'], fg=c['text'], font=('Arial', 10, 'bold')); status.pack()

    def cur():
        return cards[state['index']]

    def render():
        card = cur(); front = state['front']; bg = '#fffdfd' if front else '#fff2f7'
        for w in (box, side, text, meta):
            w.configure(bg=bg)
        side.configure(text='Pregunta' if front else 'Respuesta'); text.configure(text=card.get('q', '') if front else card.get('a', '')); due = card.get('due', card.get('next_review', today_string())); meta.configure(text=f"Dificultad: {card.get('difficulty', 'Normal')} · intervalo: {card.get('interval', 0)}d · facilidad: {safe_float(card.get('ease', 2.5), 2.5):.1f} · due: {due}" + (f" · tags: {card.get('tags')}" if card.get('tags') else '')); status.configure(text=f"Ficha {state['index'] + 1}/{len(cards)} · sesión: {state['reviewed']} revisadas · {state['session_correct']} bien"); flip_btn.configure(text='Ver pregunta' if not front else 'Voltear')

    def flip(event=None):
        state['front'] = not state['front']; render()

    def move(step=1):
        state['index'] = (state['index'] + step) % len(cards); state['front'] = True; render()

    def grade(kind):
        card = cur(); old = safe_int(card.get('interval', 0), 0); ease = safe_float(card.get('ease', 2.5), 2.5)
        if kind == 'again':
            interval = 0; ease = max(1.3, ease - 0.25); card['lapses'] = safe_int(card.get('lapses', 0), 0) + 1; reward = (1, 2)
        elif kind == 'hard':
            interval = max(1, old if old else 1); ease = max(1.3, ease - 0.1); reward = (2, 3)
        elif kind == 'good':
            interval = 1 if old == 0 else max(2, round(old * ease)); card['correct'] = safe_int(card.get('correct', 0), 0) + 1; state['session_correct'] += 1; reward = (3, 6)
        else:
            interval = 3 if old == 0 else max(4, round(old * (ease + 0.35))); ease = min(3.2, ease + 0.15); card['correct'] = safe_int(card.get('correct', 0), 0) + 1; state['session_correct'] += 1; reward = (4, 7)
        if card.get('difficulty') == 'Difícil' and kind in ('again', 'hard'):
            interval = min(interval, 1)
        if card.get('difficulty') == 'Fácil' and kind in ('good', 'easy'):
            interval += 1
        card['interval'] = interval; card['ease'] = round(ease, 2); card['reviews'] = safe_int(card.get('reviews', 0), 0) + 1; card['last_review'] = today_string(); card['due'] = (date.today() + timedelta(days=interval)).isoformat(); card['next_review'] = card['due']; stats = card.setdefault('stats', {'ok': 0, 'review': 0, 'seen': 0, 'last_review': ''}); stats['seen'] = int(stats.get('seen', 0)) + 1; stats['last_review'] = now_string()
        if kind in ('good', 'easy'):
            stats['ok'] = int(stats.get('ok', 0)) + 1
        else:
            stats['review'] = int(stats.get('review', 0)) + 1
        state['reviewed'] += 1; self.add_rewards(fresas=reward[0], xp=reward[1], pet_xp=3); self.update_mission_progress('flashcards', 1); self.save(); self.load_selected_subject()
        if state['index'] == len(cards) - 1:
            messagebox.showinfo('Repaso', f"Sesión terminada: {state['reviewed']} revisadas, {state['session_correct']} bien. ¡Buen trabajo!"); win.destroy(); self.refresh_all(); return
        move(1)
    for w in (box, side, text, meta):
        w.bind('<Button-1>', flip)
    nav = tk.Frame(win, bg=c['bg']); nav.pack(fill='x', padx=20, pady=(8, 5)); tk.Button(nav, text='◀', command=lambda: move(-1), bg='#d7ecff').pack(side='left', fill='x', expand=True, padx=3); flip_btn = tk.Button(nav, text='Voltear', command=flip, bg=c['accent']); flip_btn.pack(side='left', fill='x', expand=True, padx=3); tk.Button(nav, text='▶', command=lambda: move(1), bg='#d6f5df').pack(side='left', fill='x', expand=True, padx=3); grades = tk.Frame(win, bg=c['bg']); grades.pack(fill='x', padx=20, pady=(0, 15)); tk.Button(grades, text='Olvidé', command=lambda: grade('again'), bg=c['danger']).pack(side='left', fill='x', expand=True, padx=3); tk.Button(grades, text='Difícil', command=lambda: grade('hard'), bg='#fff1b8').pack(side='left', fill='x', expand=True, padx=3)
    tk.Button(grades, text='Bien', command=lambda: grade('good'), bg='#cfe8ff').pack(side='left', fill='x', expand=True, padx=3); tk.Button(grades, text='Fácil', command=lambda: grade('easy'), bg='#d6f5df').pack(side='left', fill='x', expand=True, padx=3); render()

def _ms_v6_ensure_schema(self):
    _ms_v6_old_ensure_schema(self); self.user_data.setdefault('planner_events', []); self.user_data.setdefault('moods', []); self.user_data.setdefault('mood_stats', {'last_saved': '', 'total_saved': 0}); self.user_data.setdefault('mood_history_summary', {}); self.user_data.setdefault('calendar_settings', {'selected_date': today_string()}); self.user_data.setdefault('metrics', {}); self.user_data['metrics'].setdefault('calendar_events_created', 0); self.user_data['metrics'].setdefault('calendar_events_completed', 0)
    for ev in self.user_data.get('planner_events', []):
        ev.setdefault('date', today_string()); ev.setdefault('time', '16:00'); ev.setdefault('type', 'Estudio'); ev.setdefault('title', 'Evento'); ev.setdefault('subject', ''); ev.setdefault('notes', ''); ev.setdefault('done', False); ev.setdefault('created_at', now_string())
    for mood in self.user_data.get('moods', []):
        mood.setdefault('date', mood.get('created_at', now_string())); mood.setdefault('mood', '😊 Feliz'); mood.setdefault('note', ''); mood.setdefault('intensity', 7); mood.setdefault('energy', 6); mood.setdefault('tags', '')
    self.save()

def _ms_v6_month_start(self):
    current = getattr(self, 'calendar_current_month', None)
    if current is None:
        selected = self.user_data.get('calendar_settings', {}).get('selected_date', today_string())
        try:
            d = date.fromisoformat(str(selected)[:10])
        except Exception:
            d = date.today()
        self.calendar_current_month = date(d.year, d.month, 1)
    return self.calendar_current_month

def _ms_v6_set_selected_date(self, value):
    try:
        d = date.fromisoformat(str(value)[:10])
    except Exception:
        d = date.today()
    self.calendar_selected_date = d.isoformat(); self.user_data.setdefault('calendar_settings', {})['selected_date'] = self.calendar_selected_date
    if hasattr(self, 'plan_date_entry'):
        self.plan_date_entry.delete(0, tk.END); self.plan_date_entry.insert(0, self.calendar_selected_date)
    self.save(); self.refresh_planner_events('selected'); self.render_calendar_month()

def _ms_v6_events_for_day(self, day_text):
    return [e for e in self.user_data.get('planner_events', []) if str(e.get('date', ''))[:10] == day_text]

def _ms_v6_change_calendar_month(self, delta):
    current = self.month_start(); month = current.month + delta; year = current.year
    while month < 1:
        month += 12; year -= 1
    while month > 12:
        month -= 12; year += 1
    self.calendar_current_month = date(year, month, 1); self.render_calendar_month()

def _ms_v6_go_calendar_today(self):
    self.calendar_current_month = date.today().replace(day=1); self.set_selected_date(today_string())

def _ms_v6_add_planner_event(self):
    d = self.plan_date_entry.get().strip() if hasattr(self, 'plan_date_entry') else today_string(); t = self.plan_time_entry.get().strip() if hasattr(self, 'plan_time_entry') else '16:00'; title = self.plan_title_entry.get().strip() if hasattr(self, 'plan_title_entry') else ''; subject = self.plan_subject_entry.get().strip() if hasattr(self, 'plan_subject_entry') else ''; notes = self.plan_notes_text.get('1.0', tk.END).strip() if hasattr(self, 'plan_notes_text') else ''
    if not title:
        messagebox.showerror('Planificador', 'Escribe un título.'); return
    try:
        datetime.strptime(d, '%Y-%m-%d'); datetime.strptime(t, '%H:%M')
    except ValueError:
        messagebox.showerror('Planificador', 'Usa fecha YYYY-MM-DD y hora HH:MM.'); return
    ev = {'date': d, 'time': t, 'type': self.plan_type_var.get() if hasattr(self, 'plan_type_var') else 'Estudio', 'title': title, 'subject': subject, 'notes': notes, 'done': False, 'created_at': now_string()}; self.user_data.setdefault('planner_events', []).append(ev); self.user_data.setdefault('metrics', {})['calendar_events_created'] = self.user_data.setdefault('metrics', {}).get('calendar_events_created', 0) + 1
    if hasattr(self, 'plan_title_entry'):
        self.plan_title_entry.delete(0, tk.END)
    if hasattr(self, 'plan_notes_text'):
        self.plan_notes_text.delete('1.0', tk.END)
    self.set_selected_date(d); self.save(); self.refresh_all()

def _ms_v6_refresh_planner_events(self, mode='selected'):
    if not hasattr(self, 'planner_list'):
        return
    self.planner_list.delete(0, tk.END); selected = getattr(self, 'calendar_selected_date', self.user_data.get('calendar_settings', {}).get('selected_date', today_string())); events = list(enumerate(self.user_data.get('planner_events', [])))
    if mode == 'today':
        events = [(i, e) for i, e in events if str(e.get('date', ''))[:10] == today_string()]
    elif mode == 'pending':
        events = [(i, e) for i, e in events if not e.get('done')]
    elif mode == 'selected':
        events = [(i, e) for i, e in events if str(e.get('date', ''))[:10] == selected]
    events.sort(key=lambda item: (item[1].get('date', ''), item[1].get('time', ''))); self._planner_visible_indices_v6 = []
    if not events:
        self.planner_list.insert(tk.END, 'No hay eventos en esta vista.')
    for i, ev in events:
        self._planner_visible_indices_v6.append(i); status = '✅' if ev.get('done') else '⬜'; subject = f" · {ev.get('subject')}" if ev.get('subject') else ''; notes = f" · {ev.get('notes')[:28]}" if ev.get('notes') else ''; self.planner_list.insert(tk.END, f"{status} {ev.get('date')} {ev.get('time')} · [{ev.get('type')}] {ev.get('title')}{subject}{notes}")
    total = len(self.user_data.get('planner_events', [])); pending = len([e for e in self.user_data.get('planner_events', []) if not e.get('done')]); today_count = len(self.events_for_day(today_string()))
    if hasattr(self, 'planner_summary'):
        self.planner_summary.config(text=f'Total: {total} · Pendientes: {pending} · Hoy: {today_count} · Día seleccionado: {selected}')
    self.render_calendar_month()

def _ms_v6_planner_visible_to_index(self):
    sel = self.planner_list.curselection() if hasattr(self, 'planner_list') else ()
    if not sel:
        return None
    if hasattr(self, '_planner_visible_indices_v6') and sel[0] < len(self._planner_visible_indices_v6):
        return self._planner_visible_indices_v6[sel[0]]
    return None

def _ms_v6_complete_planner_event(self):
    idx = self._planner_visible_to_index()
    if idx is None:
        messagebox.showerror('Planificador', 'Selecciona un evento.'); return
    ev = self.user_data['planner_events'][idx]
    if ev.get('done'):
        messagebox.showinfo('Planificador', 'Ese evento ya está completado.'); return
    ev['done'] = True; ev['completed_at'] = now_string(); self.user_data.setdefault('metrics', {})['planner_events_completed'] = self.user_data.setdefault('metrics', {}).get('planner_events_completed', 0) + 1; self.user_data['metrics']['calendar_events_completed'] = self.user_data['metrics'].get('calendar_events_completed', 0) + 1
    try:
        self.update_mission_progress('planner', 1)
    except Exception:
        pass
    self.add_rewards(fresas=10, xp=15, pet_xp=8); self.save(); self.refresh_all(); self.render_calendar_month(); messagebox.showinfo('Planificador', 'Evento completado. +10 fresas y +15 XP.')

def _ms_v6_delete_planner_event(self):
    idx = self._planner_visible_to_index()
    if idx is None:
        messagebox.showerror('Planificador', 'Selecciona un evento.'); return
    if messagebox.askyesno('Planificador', '¿Eliminar este evento?'):
        del self.user_data['planner_events'][idx]; self.save(); self.refresh_all(); self.render_calendar_month()

def _ms_v6_save_mood(self):
    mood = self.quick_mood.get() if hasattr(self, 'quick_mood') else '😊 Feliz'; note = self.mood_note.get().strip() if hasattr(self, 'mood_note') else ''
    if note.startswith('¿Cómo te sientes') or note == 'Guardado ✨':
        note = ''
    tags = self.mood_tags_entry.get().strip() if hasattr(self, 'mood_tags_entry') else ''
    if tags.startswith('Tags:'):
        tags = ''
    intensity = safe_int(self.mood_intensity_var.get(), 7) if hasattr(self, 'mood_intensity_var') else 7; energy = safe_int(self.mood_energy_var.get(), 6) if hasattr(self, 'mood_energy_var') else 6; entry = {'date': now_string(), 'day': today_string(), 'mood': mood, 'note': note, 'intensity': intensity, 'energy': energy, 'tags': tags, 'recommendation': self.mood_recommendation({'mood': mood, 'energy': energy, 'intensity': intensity}) if hasattr(self, 'mood_recommendation') else 'Haz una tarea pequeña y toma un descanso suave.'}; self.user_data.setdefault('moods', []).append(entry); self.user_data.setdefault('profile', {})['last_mood'] = entry; self.user_data.setdefault('mood_stats', {})['last_saved'] = now_string(); self.user_data['mood_stats']['total_saved'] = len(self.user_data.get('moods', []))
    self.user_data.setdefault('metrics', {})['moods_registered'] = self.user_data.setdefault('metrics', {}).get('moods_registered', 0) + 1
    if self.user_data.get('pet'):
        self.user_data['pet']['happiness'] = clamp(self.user_data['pet'].get('happiness', 80) + 3)
    if hasattr(self, 'mood_note'):
        self.mood_note.delete(0, tk.END); self.mood_note.insert(0, 'Guardado ✨')
    if hasattr(self, 'mood_tags_entry'):
        self.mood_tags_entry.delete(0, tk.END); self.mood_tags_entry.insert(0, 'Tags: sueño, escuela, amigas, familia...')
    try:
        self.update_mission_progress('mood', 1)
    except Exception:
        pass
    self.add_rewards(fresas=2, xp=3, pet_xp=2); self.save(); self.refresh_all()

def _ms_v6_refresh_control_center(self):
    try:
        _ms_v6_old_refresh_control_center(self)
    except Exception:
        pass
    if hasattr(self, 'control_text'):
        events = self.user_data.get('planner_events', []); today_events = [e for e in events if str(e.get('date', ''))[:10] == today_string()]; pending = [e for e in events if not e.get('done')]; moods = self.user_data.get('moods', [])[-7:]; mood_line = moods[-1].get('mood', 'sin mood') if moods else 'sin mood'; self.control_text.insert(tk.END, f'\n\nCALENDARIO Y MOOD\nEventos hoy: {len(today_events)}\nEventos pendientes: {len(pending)}\nÚltimo mood guardado: {mood_line}\n')

def _ms_v7_ensure_schema(self):
    _ms_v7_old_ensure_schema(self); self.user_data.setdefault('room', {'wall_color': 'Rosa suave', 'floor_color': 'Madera clara', 'desk': 'Escritorio kawaii', 'bed': 'Cama nube', 'plant': True, 'lamp': True, 'poster': 'Michi Studio', 'decorations': ['📚', '🍓', '⭐']}); self.user_data.setdefault('planner_events', []); self.user_data.setdefault('moods', []); self.user_data.setdefault('study_links', {'tasks_to_planner': 0, 'pomodoros_from_events': 0, 'subject_sessions': {}}); self.user_data.setdefault('metrics', {}); self.user_data['metrics'].setdefault('room_customizations', 0); self.user_data['metrics'].setdefault('smart_reviews', 0)
    for task in self.user_data.get('tasks', []):
        task.setdefault('subject', ''); task.setdefault('due', '')
    for subject, data in self.user_data.get('subjects', {}).items():
        data.setdefault('study_minutes', 0); data.setdefault('pomodoros', 0)
        for card in data.get('flashcards', []):
            card.setdefault('favorite', False); card.setdefault('difficulty', 'Normal'); card.setdefault('next_review', today_string()); card.setdefault('stats', {'ok': 0, 'review': 0, 'seen': 0, 'last_review': ''})
    self.save()

def _ms_v7_build_main_ui(self):
    _ms_v7_old_build_main_ui(self)
    try:
        c = self.palette()
        if not hasattr(self, 'room_tab'):
            self.room_tab = tk.Frame(self.notebook, bg=c['bg']); self.notebook.add(self.room_tab, text='🏡 Habitación'); self.build_room_tab()
    except Exception:
        pass

def _ms_v7_refresh_all(self):
    try:
        _ms_v7_old_refresh_all(self)
    except Exception:
        pass
    try:
        if hasattr(self, 'week_frame'):
            self.render_week_view()
        if hasattr(self, 'room_canvas'):
            self.draw_room()
        if hasattr(self, 'mood_calendar_canvas'):
            self.draw_mood_calendar()
    except Exception:
        pass

def _ms_v7_build_home_tab(self):
    _ms_v7_old_build_home_tab(self)
    try:
        c = self.palette(); pro = self.card(self.home_tab, 'Mood y productividad Pro', '💗'); pro.pack(fill='x', padx=18, pady=(0, 10)); row = tk.Frame(pro, bg=c['card']); row.pack(fill='x'); tk.Button(row, text='📆 Calendario emocional', command=self.open_mood_calendar, bg='#ffd9e8').pack(side='left', fill='x', expand=True, padx=3); tk.Button(row, text='🧠 Plan según mood', command=self.generate_mood_study_plan, bg='#d6f5df').pack(side='left', fill='x', expand=True, padx=3); tk.Button(row, text='🔎 Buscar en todo', command=self.open_global_search, bg='#d7ecff').pack(side='left', fill='x', expand=True, padx=3); self.mood_productivity_label = tk.Label(pro, text=self.mood_productivity_summary(), bg=c['card'], fg=c['muted'], justify='left', wraplength=900); self.mood_productivity_label.pack(fill='x', pady=5)
    except Exception:
        pass

def _ms_v7_mood_productivity_summary(self):
    moods = self.user_data.get('moods', [])[-14:]; events = self.user_data.get('planner_events', []); done = len([e for e in events if e.get('done')]); pending = len([e for e in events if not e.get('done')])
    if not moods:
        return f'Aún no hay suficiente historial emocional. Eventos completados: {done}; pendientes: {pending}.'
    avg_energy = sum((safe_int(m.get('energy', 6), 6) for m in moods)) / max(1, len(moods)); avg_intensity = sum((safe_int(m.get('intensity', 7), 7) for m in moods)) / max(1, len(moods)); last = moods[-1]; suggestion = 'Haz un plan suave de 20 minutos.' if avg_energy < 5 else 'Puedes hacer una sesión profunda o flashcards.'; return f"Último mood: {last.get('mood')} · Energía promedio: {avg_energy:.1f}/10 · Intensidad promedio: {avg_intensity:.1f}/10 · Eventos ✅{done}/⬜{pending}. {suggestion}"

def _ms_v7_week_start(self):
    selected = getattr(self, 'calendar_selected_date', self.user_data.get('calendar_settings', {}).get('selected_date', today_string()))
    try:
        d = date.fromisoformat(str(selected)[:10])
    except Exception:
        d = date.today()
    return d - datetime.timedelta(days=d.weekday()) if False else date.fromordinal(d.toordinal() - d.weekday())

def _ms_v7_change_week(self, delta):
    current = self.week_start(); new = date.fromordinal(current.toordinal() + delta); self.set_selected_date(new.isoformat()); self.render_week_view()

def _ms_v7_go_week_today(self):
    self.set_selected_date(today_string()); self.render_week_view()

def _ms_v7_create_pomodoro_from_selected_event(self):
    idx = self._planner_visible_to_index() if hasattr(self, '_planner_visible_to_index') else None
    if idx is None:
        messagebox.showerror('Planner', 'Selecciona un evento del planificador.'); return
    ev = self.user_data.get('planner_events', [])[idx]; minutes = 25 if ev.get('type') != 'Repaso' else 20
    try:
        self.timer.reset(self.root, minutes, 'study')
        if hasattr(self, 'study_plan_text'):
            self.study_plan_text.insert(tk.END, f"\nPomodoro desde evento: {ev.get('title')} ({ev.get('subject', '')})")
    except Exception:
        pass
    self.user_data.setdefault('study_links', {})['pomodoros_from_events'] = self.user_data.setdefault('study_links', {}).get('pomodoros_from_events', 0) + 1; self.save(); self.refresh_all(); messagebox.showinfo('Pomodoro', f"Preparé un Pomodoro de {minutes} min para: {ev.get('title')}")

def _ms_v7_task_to_planner_window(self):
    tasks = [t for t in self.user_data.get('tasks', []) if not t.get('done')]
    if not tasks:
        messagebox.showinfo('Tareas', 'No tienes tareas pendientes para enviar al calendario.'); return
    c = self.palette(); win = tk.Toplevel(self.root); win.title('Enviar tarea al calendario'); win.geometry('520x360'); win.configure(bg=c['bg']); tk.Label(win, text='Enviar tarea al calendario', bg=c['bg'], fg=c['primary'], font=('Arial', 15, 'bold')).pack(pady=10); lb = tk.Listbox(win, height=8); lb.pack(fill='both', expand=True, padx=18, pady=6)
    for t in tasks:
        lb.insert(tk.END, f"[{t.get('priority', 'Normal')}] {t.get('text', '')}")
    row = tk.Frame(win, bg=c['bg']); row.pack(fill='x', padx=18, pady=4); tk.Label(row, text='Fecha', bg=c['bg'], fg=c['text']).pack(side='left'); date_entry = tk.Entry(row, width=12); date_entry.pack(side='left', padx=4); date_entry.insert(0, self.user_data.get('calendar_settings', {}).get('selected_date', today_string())); tk.Label(row, text='Hora', bg=c['bg'], fg=c['text']).pack(side='left'); time_entry = tk.Entry(row, width=7); time_entry.pack(side='left', padx=4); time_entry.insert(0, '16:00')

    def send():
        sel = lb.curselection()
        if not sel:
            messagebox.showerror('Tareas', 'Selecciona una tarea.'); return
        task = tasks[sel[0]]; d, tm = (date_entry.get().strip(), time_entry.get().strip())
        try:
            date.fromisoformat(d); datetime.strptime(tm, '%H:%M')
        except Exception:
            messagebox.showerror('Fecha', 'Usa YYYY-MM-DD y HH:MM.'); return
        self.user_data.setdefault('planner_events', []).append({'date': d, 'time': tm, 'type': 'Tarea', 'title': task.get('text', 'Tarea'), 'subject': task.get('subject', ''), 'notes': 'Creado desde To-do', 'done': False, 'created_at': now_string()}); self.user_data.setdefault('study_links', {})['tasks_to_planner'] = self.user_data.setdefault('study_links', {}).get('tasks_to_planner', 0) + 1; task['due'] = d; self.save(); self.refresh_all(); win.destroy()
    tk.Button(win, text='Enviar al calendario', command=send, bg=c['accent']).pack(fill='x', padx=18, pady=10)

def _ms_v7_auto_week_plan(self):
    subjects = list(self.user_data.get('subjects', {}).keys()); pending_tasks = [t for t in self.user_data.get('tasks', []) if not t.get('done')]; start = self.week_start(); created = 0
    for i, subject in enumerate(subjects[:5]):
        d = date.fromordinal(start.toordinal() + i).isoformat(); self.user_data.setdefault('planner_events', []).append({'date': d, 'time': '17:00', 'type': 'Estudio', 'title': f'Repasar {subject}', 'subject': subject, 'notes': 'Plan semanal automático', 'done': False, 'created_at': now_string()}); created += 1
    for i, task in enumerate(pending_tasks[:4]):
        d = date.fromordinal(start.toordinal() + i % 5).isoformat(); self.user_data.setdefault('planner_events', []).append({'date': d, 'time': '18:00', 'type': 'Tarea', 'title': task.get('text', 'Tarea'), 'subject': task.get('subject', ''), 'notes': 'Tarea colocada automáticamente', 'done': False, 'created_at': now_string()}); created += 1
    self.save(); self.refresh_all(); self.render_week_view(); messagebox.showinfo('Plan semanal', f'Creé {created} bloques en tu semana.')

def _ms_v7_room_color(self, value):
    return {'Rosa suave': '#ffe5ef', 'Lavanda': '#eee7ff', 'Menta': '#e2fff1', 'Cielo': '#e4f4ff', 'Crema': '#fff6df', 'Madera clara': '#e5c59e', 'Madera rosa': '#eac0c7', 'Alfombra nube': '#eef6ff', 'Pastel': '#f5e9ff'}.get(value, '#fff7fa')

def _ms_v7_open_mood_calendar(self):
    c = self.palette(); win = tk.Toplevel(self.root); win.title('Calendario emocional'); win.geometry('760x560'); win.configure(bg=c['bg']); tk.Label(win, text='Calendario emocional', bg=c['bg'], fg=c['primary'], font=('Arial', 18, 'bold')).pack(pady=10); self.mood_calendar_canvas = tk.Canvas(win, width=720, height=420, bg=c['card'], highlightthickness=0); self.mood_calendar_canvas.pack(padx=18, pady=8); self.mood_calendar_summary = tk.Label(win, text='', bg=c['bg'], fg=c['text'], justify='left', wraplength=700); self.mood_calendar_summary.pack(fill='x', padx=18); self.draw_mood_calendar()

def _ms_v7_draw_mood_calendar(self):
    if not hasattr(self, 'mood_calendar_canvas'):
        return
    c = self.palette(); canvas = self.mood_calendar_canvas; canvas.delete('all'); today = date.today(); start = today.replace(day=1); cal = _ms_v7_calendar.Calendar(firstweekday=0); moods_by_day = {}
    for m in self.user_data.get('moods', []):
        day = m.get('day') or str(m.get('date', ''))[:10]; moods_by_day.setdefault(day, []).append(m)
    headers = ['L', 'M', 'X', 'J', 'V', 'S', 'D']; cell_w, cell_h = (96, 58)
    for i, h in enumerate(headers):
        canvas.create_text(50 + i * cell_w, 25, text=h, fill=c['primary'], font=('Arial', 12, 'bold'))
    for r, week in enumerate(cal.monthdatescalendar(today.year, today.month)):
        for col, d in enumerate(week):
            x, y = (10 + col * cell_w, 45 + r * cell_h); day = d.isoformat(); items = moods_by_day.get(day, []); fill = c['soft'] if d.month != today.month else '#fffdfd'
            if items:
                avg_energy = sum((safe_int(m.get('energy', 6), 6) for m in items)) / len(items); fill = '#d6f5df' if avg_energy >= 7 else '#fff1b8' if avg_energy >= 4 else '#ffd9e8'
            canvas.create_rectangle(x, y, x + cell_w - 6, y + cell_h - 6, fill=fill, outline=c['secondary']); label = str(d.day)
            if items:
                label += '\n' + items[-1].get('mood', '').split()[0]
            canvas.create_text(x + cell_w / 2 - 3, y + cell_h / 2 - 3, text=label, font=('Arial', 10, 'bold'), fill=c['text'])
    recent = self.user_data.get('moods', [])[-30:]
    if hasattr(self, 'mood_calendar_summary'):
        if recent:
            avg_e = sum((safe_int(m.get('energy', 6), 6) for m in recent)) / len(recent); avg_i = sum((safe_int(m.get('intensity', 7), 7) for m in recent)) / len(recent); self.mood_calendar_summary.config(text=f'Últimos 30 registros: {len(recent)} · Energía media {avg_e:.1f}/10 · Intensidad media {avg_i:.1f}/10. Verde = energía alta, amarillo = media, rosa = baja.')
        else:
            self.mood_calendar_summary.config(text='Guarda moods para ver patrones emocionales.')

def _ms_v7_generate_mood_study_plan(self):
    moods = self.user_data.get('moods', []); last = moods[-1] if moods else {'mood': '😊 Feliz', 'energy': 6, 'intensity': 7}; energy = safe_int(last.get('energy', 6), 6); mood = last.get('mood', '😊 Feliz')
    if energy <= 3:
        plan = 'Plan suave: 10 min ordenar apuntes, 10 min flashcards fáciles, descanso largo.'
    elif energy <= 6:
        plan = 'Plan medio: 1 Pomodoro de 25 min, 5 flashcards y una tarea pequeña.'
    else:
        plan = 'Plan intenso: 2 Pomodoros, tarea difícil primero y repaso de fichas pendientes.'
    self.user_data['study_plan'] = f'Mood actual: {mood}\n{plan}'; self.save(); self.refresh_all(); messagebox.showinfo('Plan según mood', plan)

def _ms_v7_open_global_search(self):
    c = self.palette(); win = tk.Toplevel(self.root); win.title('Buscar en Michi Studio'); win.geometry('700x520'); win.configure(bg=c['bg']); tk.Label(win, text='Buscador interno', bg=c['bg'], fg=c['primary'], font=('Arial', 17, 'bold')).pack(pady=10); entry = tk.Entry(win); entry.pack(fill='x', padx=18, pady=4); results = tk.Listbox(win, height=20); results.pack(fill='both', expand=True, padx=18, pady=8)

    def search():
        q = entry.get().strip().lower(); results.delete(0, tk.END)
        if not q:
            return
        for t in self.user_data.get('tasks', []):
            if q in t.get('text', '').lower():
                results.insert(tk.END, f"✅ Tarea: {t.get('text')}")
        for sub, data in self.user_data.get('subjects', {}).items():
            if q in sub.lower() or q in data.get('notes', '').lower():
                results.insert(tk.END, f'📚 Materia/apunte: {sub}')
            for card in data.get('flashcards', []):
                if q in card.get('q', '').lower() or q in card.get('a', '').lower():
                    results.insert(tk.END, f"🃏 Flashcard {sub}: {card.get('q')[:55]}")
        for ev in self.user_data.get('planner_events', []):
            hay = ' '.join((str(ev.get(k, '')) for k in ['title', 'subject', 'notes', 'type'])).lower()
            if q in hay:
                results.insert(tk.END, f"📅 Evento: {ev.get('date')} {ev.get('time')} · {ev.get('title')}")
        for item in self.user_data.get('library', []):
            hay = ' '.join((str(item.get(k, '')) for k in ['title', 'author', 'notes', 'type'])).lower()
            if q in hay:
                results.insert(tk.END, f"📖 Biblioteca: {item.get('title')}")
        if results.size() == 0:
            results.insert(tk.END, 'No encontré resultados.')
    tk.Button(win, text='Buscar', command=search, bg=c['accent']).pack(fill='x', padx=18, pady=4); entry.bind('<Return>', lambda e: search())

def _ms_v7_get_current_subject_cards(self):
    subject = self.selected_subject() if hasattr(self, 'selected_subject') else None
    if not subject:
        return (None, [])
    return (subject, self.subject_data(subject).get('flashcards', []))

def _ms_v7_study_weak_flashcards(self):
    subject, cards = self.get_current_subject_cards()
    if not subject or not cards:
        messagebox.showinfo('Flashcards', 'Selecciona una materia con flashcards.'); return
    weak = [c for c in cards if c.get('favorite') or safe_int(c.get('stats', {}).get('review', 0), 0) >= safe_int(c.get('stats', {}).get('ok', 0), 0) or c.get('difficulty') == 'Difícil']
    if not weak:
        weak = cards[:]
    self._forced_flashcards_v7 = weak; self.user_data.setdefault('metrics', {})['smart_reviews'] = self.user_data.setdefault('metrics', {}).get('smart_reviews', 0) + 1; self.practice_flashcards()

def _ms_v7_flashcard_exam_mode(self):
    subject, cards = self.get_current_subject_cards()
    if not subject or len(cards) < 3:
        messagebox.showinfo('Modo examen', 'Necesitas al menos 3 flashcards.'); return
    c = self.palette(); win = tk.Toplevel(self.root); win.title('Modo examen'); win.geometry('650x520'); win.configure(bg=c['bg']); tk.Label(win, text=f'Modo examen · {subject}', bg=c['bg'], fg=c['primary'], font=('Arial', 17, 'bold')).pack(pady=10); questions = random.sample(cards, min(10, len(cards))) if 'random' in globals() else cards[:10]; state = {'i': 0, 'score': 0}; q_label = tk.Label(win, text='', bg=c['bg'], fg=c['text'], font=('Arial', 15, 'bold'), wraplength=580); q_label.pack(padx=20, pady=14); answer = tk.Text(win, height=5, wrap='word'); answer.pack(fill='x', padx=20, pady=6); feedback = tk.Label(win, text='', bg=c['bg'], fg=c['muted'], wraplength=580, justify='left'); feedback.pack(padx=20, pady=6)

    def render():
        if state['i'] >= len(questions):
            self.add_rewards(fresas=state['score'] * 2 + 5, xp=state['score'] * 5 + 10, pet_xp=state['score'] * 2); self.save(); self.refresh_all(); q_label.config(text=f"Examen terminado: {state['score']}/{len(questions)}"); answer.destroy(); btn.config(text='Cerrar', command=win.destroy); return
        answer.delete('1.0', tk.END); feedback.config(text=''); q_label.config(text=f"{state['i'] + 1}. {questions[state['i']].get('q', '')}")

    def check():
        card = questions[state['i']]; expected = card.get('a', ''); user = answer.get('1.0', tk.END).strip().lower(); words = [w for w in expected.lower().split() if len(w) > 3]; hit = sum((1 for w in words if w in user))
        if user and (hit >= max(1, len(words) // 3) or user in expected.lower()):
            state['score'] += 1; card.setdefault('stats', {})['ok'] = safe_int(card.setdefault('stats', {}).get('ok', 0), 0) + 1; feedback.config(text='Correcto o muy cerca ✅')
        else:
            card.setdefault('stats', {})['review'] = safe_int(card.setdefault('stats', {}).get('review', 0), 0) + 1; feedback.config(text=f'Repasar 🔁 Respuesta esperada: {expected}')
        state['i'] += 1; self.save(); win.after(900, render)
    btn = tk.Button(win, text='Comprobar', command=check, bg=c['accent']); btn.pack(fill='x', padx=20, pady=10); render()

def _ms_v7_finish_timer(self, mode):
    selected_subject = ''
    try:
        idx = self._planner_visible_to_index() if hasattr(self, '_planner_visible_to_index') else None
        if idx is not None:
            selected_subject = self.user_data.get('planner_events', [])[idx].get('subject', '')
    except Exception:
        selected_subject = ''
    _ms_v7_old_finish_timer(self, mode)
    if mode == 'study' and selected_subject and (selected_subject in self.user_data.get('subjects', {})):
        mins = self.user_data.get('pomodoro', {}).get('study_minutes', 25); data = self.user_data['subjects'][selected_subject]; data['study_minutes'] = safe_int(data.get('study_minutes', 0), 0) + mins; data['pomodoros'] = safe_int(data.get('pomodoros', 0), 0) + 1; self.user_data.setdefault('study_links', {}).setdefault('subject_sessions', {})[selected_subject] = data['pomodoros']; self.save()

def _ms_v8_ensure_schema(self):
    _ms_v8_old_ensure_schema(self); self.user_data.setdefault('dashboard', {'mode': 'cozy', 'show_focus_suggestion': True}); self.user_data.setdefault('room', {}); room = self.user_data['room']; room.setdefault('objects', {'cama': {'x': 62, 'y': 238, 'icon': '🛏', 'label': 'Cama fresa'}, 'escritorio': {'x': 260, 'y': 232, 'icon': '📚', 'label': 'Escritorio'}, 'lampara': {'x': 312, 'y': 112, 'icon': '💡', 'label': 'Lámpara'}, 'alfombra': {'x': 175, 'y': 285, 'icon': '🟣', 'label': 'Alfombra'}, 'poster': {'x': 86, 'y': 90, 'icon': '🌸', 'label': 'Póster'}}); room.setdefault('unlocked_furniture', ['cama', 'escritorio', 'lampara', 'alfombra', 'poster']); room.setdefault('selected_object', ''); self.user_data.setdefault('theme_packs', {'active': 'fresa', 'unlocked': ['fresa', 'lavanda', 'menta', 'noche']})
    self.user_data.setdefault('study_stats', {'total_minutes': 0, 'by_subject': {}, 'sessions': []}); self.user_data.setdefault('global_search_history', []); self.user_data.setdefault('planner_settings', {'view': 'month', 'drag_hint_seen': False}); self.user_data.setdefault('michi_sprites', {'enabled': True, 'state': 'idle', 'last_reaction': ''})
    for subject, data in self.user_data.get('subjects', {}).items():
        data.setdefault('study_minutes', 0); data.setdefault('pomodoros', 0); data.setdefault('weak_topics', [])
        for card in data.get('flashcards', []):
            stats = card.setdefault('stats', {}); stats.setdefault('ease', 2.5); stats.setdefault('interval', 0); stats.setdefault('repetitions', 0); stats.setdefault('due', today_string()); stats.setdefault('lapses', 0); card.setdefault('mode', 'normal')
    self.save()

def _ms_v8_dashboard_summary(self):
    tasks = self.user_data.get('tasks', []); pending = [t for t in tasks if not t.get('done')]; events = self.user_data.get('planner_events', []); today_events = [e for e in events if str(e.get('date', ''))[:10] == today_string()]; moods = self.user_data.get('moods', []); flash_due = 0
    for data in self.user_data.get('subjects', {}).values():
        for card in data.get('flashcards', []):
            if str(card.get('stats', {}).get('due', today_string()))[:10] <= today_string():
                flash_due += 1
    next_event = 'Sin eventos hoy'
    if today_events:
        ev = sorted(today_events, key=lambda e: e.get('time', ''))[0]; next_event = f"{ev.get('time', '')} · {ev.get('title', '')}"
    last_mood = moods[-1].get('mood', 'Sin mood') if moods else 'Sin mood'; return (pending, today_events, flash_due, next_event, last_mood)

def _ms_v8_smart_next_action(self):
    moods = self.user_data.get('moods', []); energy = safe_int(moods[-1].get('energy', 6), 6) if moods else 6; pending = [t for t in self.user_data.get('tasks', []) if not t.get('done')]; due_cards = []
    for subj, data in self.user_data.get('subjects', {}).items():
        for card in data.get('flashcards', []):
            if str(card.get('stats', {}).get('due', today_string()))[:10] <= today_string():
                due_cards.append((subj, card))
    if energy <= 4:
        return 'Plan suave: 10 min de repaso + una tarea fácil'
    if due_cards:
        return f'Repasar {len(due_cards)} flashcards vencidas'
    if pending:
        return f"Completar: {pending[0].get('text', 'tarea')}"
    return 'Pomodoro libre de 25 min'

def _ms_v8_start_focus_from_dashboard(self):
    moods = self.user_data.get('moods', []); energy = safe_int(moods[-1].get('energy', 6), 6) if moods else 6; minutes = 15 if energy <= 4 else 25
    try:
        self.timer.reset(self.root, minutes, 'study'); self.notebook.select(self.study_tab)
    except Exception:
        pass
    messagebox.showinfo('Modo enfoque', f'Preparé un Pomodoro de {minutes} minutos según tu energía actual.')

def _ms_v8_open_today_overview(self):
    c = self.palette(); win = tk.Toplevel(self.root); win.title('Hoy en Michi Studio'); win.geometry('620x520'); win.configure(bg=c['bg']); tk.Label(win, text='Resumen de hoy', bg=c['bg'], fg=c['primary'], font=('Arial', 17, 'bold')).pack(pady=10); box = tk.Text(win, wrap='word', height=22); box.pack(fill='both', expand=True, padx=18, pady=8); events = [e for e in self.user_data.get('planner_events', []) if str(e.get('date', ''))[:10] == today_string()]; tasks = [t for t in self.user_data.get('tasks', []) if not t.get('done')]; moods = self.user_data.get('moods', []); lines = ['EVENTOS DE HOY']; lines += [f"- {e.get('time', '')} {e.get('title', '')} ({e.get('type', '')})" for e in events] or ['- Sin eventos']; lines += ['', 'TAREAS PENDIENTES']
    lines += [f"- [{t.get('priority', 'Normal')}] {t.get('text', '')}" for t in tasks[:8]] or ['- Sin tareas pendientes']; lines += ['', 'MOOD']; lines += [f"- {moods[-1].get('mood')} · energía {moods[-1].get('energy', '?')}/10" if moods else '- Sin mood registrado']; lines += ['', 'RECOMENDACIÓN', f'- {self.smart_next_action()}']; box.insert('1.0', '\n'.join(lines)); box.config(state='disabled')

def _ms_v8_shop_items(self):
    items = list(_ms_v8_old_shop_items(self))
    extra = [{'name': 'Cama luna', 'icon': '🛏', 'slot': 'furniture', 'price': 120, 'rarity': 'raro', 'collection': 'Habitación cozy', 'effect': 'Mueble para la habitación', 'furniture_key': 'cama', 'room_icon': '🛏', 'label': 'Cama luna'}, {'name': 'Escritorio pro', 'icon': '🧑\u200d💻', 'slot': 'furniture', 'price': 140, 'rarity': 'épico', 'collection': 'Estudio', 'effect': 'Mueble para estudiar', 'furniture_key': 'escritorio', 'room_icon': '🧑\u200d💻', 'label': 'Escritorio pro'}, {'name': 'Lámpara estrella', 'icon': '🌟', 'slot': 'furniture', 'price': 95, 'rarity': 'raro', 'collection': 'Habitación cozy', 'effect': 'Ilumina la habitación', 'furniture_key': 'lampara', 'room_icon': '🌟', 'label': 'Lámpara estrella'}, {'name': 'Alfombra fresa', 'icon': '🍓', 'slot': 'furniture', 'price': 90, 'rarity': 'común', 'collection': 'Fresa', 'effect': 'Alfombra decorativa', 'furniture_key': 'alfombra', 'room_icon': '🍓', 'label': 'Alfombra fresa'}, {'name': 'Póster biblioteca', 'icon': '📚', 'slot': 'furniture', 'price': 75, 'rarity': 'común', 'collection': 'Estudio', 'effect': 'Póster para motivarte', 'furniture_key': 'poster', 'room_icon': '📚', 'label': 'Póster biblioteca'}, {'name': 'Tema pixel pastel', 'icon': '🎮', 'slot': 'theme_pack', 'price': 160, 'rarity': 'legendario', 'collection': 'Temas', 'effect': 'Desbloquea tema pixel pastel', 'theme': 'pixel'}, {'name': 'Tema bosque', 'icon': '🌲', 'slot': 'theme_pack', 'price': 135, 'rarity': 'épico', 'collection': 'Temas', 'effect': 'Desbloquea tema bosque', 'theme': 'bosque'}]
    names = {i.get('name') for i in items}; items.extend([i for i in extra if i.get('name') not in names]); return items

def _ms_v8_use_inventory_item(self):
    sel = self.inventory_list.curselection() if hasattr(self, 'inventory_list') else ()
    if sel and getattr(self, '_inventory_index_map', None) and (not self.inventory_list.get(sel[0]).startswith('Tu inventario')):
        item = self._inventory_index_map[sel[0]]; slot = item.get('slot')
        if slot == 'furniture':
            key = item.get('furniture_key', item.get('name', 'mueble').lower()); room = self.user_data.setdefault('room', {}); objects = room.setdefault('objects', {}); objects[key] = {'x': 180, 'y': 210, 'icon': item.get('room_icon', item.get('icon', '🪑')), 'label': item.get('label', item.get('name', 'Mueble'))}; unlocked = room.setdefault('unlocked_furniture', [])
            if key not in unlocked:
                unlocked.append(key)
            self.save(); self.refresh_all(); messagebox.showinfo('Habitación', f"Coloqué {item.get('name')} en la habitación."); return
        if slot == 'theme_pack':
            packs = self.user_data.setdefault('theme_packs', {'active': 'fresa', 'unlocked': ['fresa']}); theme = item.get('theme', 'fresa')
            if theme not in packs.setdefault('unlocked', []):
                packs['unlocked'].append(theme)
            packs['active'] = theme; self.save(); self.refresh_all(); messagebox.showinfo('Tema', f'Tema desbloqueado: {theme}'); return
    _ms_v8_old_use_inventory_item(self)

def _ms_v8_selected_event_index(self):
    try:
        idx = self._planner_visible_to_index() if hasattr(self, '_planner_visible_to_index') else None
        if idx is not None and idx < len(self.user_data.get('planner_events', [])):
            return idx
    except Exception:
        pass
    return None

def _ms_v8_move_selected_event_days(self, days):
    idx = self.selected_event_index()
    if idx is None:
        messagebox.showerror('Agenda', 'Selecciona un evento.'); return
    ev = self.user_data['planner_events'][idx]
    try:
        d = date.fromisoformat(str(ev.get('date', today_string()))[:10])
    except Exception:
        d = date.today()
    ev['date'] = (d + timedelta(days=days)).isoformat(); self.save(); self.refresh_all()

def _ms_v8_duplicate_selected_event_weekly(self):
    idx = self.selected_event_index()
    if idx is None:
        messagebox.showerror('Agenda', 'Selecciona un evento.'); return
    base = dict(self.user_data['planner_events'][idx])
    try:
        start = date.fromisoformat(str(base.get('date', today_string()))[:10])
    except Exception:
        start = date.today()
    for n in range(1, 4):
        ev = dict(base); ev['date'] = (start + timedelta(days=7 * n)).isoformat(); ev['done'] = False; ev['title'] = base.get('title', '') + ' (repetido)'; self.user_data.setdefault('planner_events', []).append(ev)
    self.save(); self.refresh_all(); messagebox.showinfo('Agenda', 'Duplicado semanal por 3 semanas.')

def _ms_v8_event_to_task(self):
    idx = self.selected_event_index()
    if idx is None:
        messagebox.showerror('Agenda', 'Selecciona un evento.'); return
    ev = self.user_data['planner_events'][idx]; self.user_data.setdefault('tasks', []).append({'text': f"{ev.get('title', 'Evento')} ({ev.get('date', '')})", 'priority': 'Alta' if ev.get('type') in ['Examen', 'Entrega'] else 'Normal', 'done': False, 'created_at': now_string(), 'subject': ev.get('subject', '')}); self.save(); self.refresh_all(); messagebox.showinfo('Agenda', 'Evento convertido en tarea.')

def _ms_v8_due_cards(self):
    due = []; today = today_string()
    for subj, data in self.user_data.get('subjects', {}).items():
        for card in data.get('flashcards', []):
            stats = card.setdefault('stats', {}); stats.setdefault('due', today)
            if str(stats.get('due', today))[:10] <= today:
                due.append((subj, card))
    return due

def _ms_v8_apply_anki_rating(self, card, rating):
    stats = card.setdefault('stats', {}); ease = float(stats.get('ease', 2.5) or 2.5); reps = safe_int(stats.get('repetitions', 0), 0); interval = safe_int(stats.get('interval', 0), 0)
    if rating <= 1:
        reps = 0; interval = 1; ease = max(1.3, ease - 0.25); stats['lapses'] = safe_int(stats.get('lapses', 0), 0) + 1
    elif rating == 2:
        reps = max(1, reps); interval = max(1, interval); ease = max(1.3, ease - 0.1)
    elif rating == 3:
        reps += 1; interval = 1 if reps == 1 else 3 if reps == 2 else max(4, int(interval * ease))
    else:
        reps += 1; ease += 0.12; interval = 2 if reps == 1 else 5 if reps == 2 else max(6, int(interval * ease * 1.25))
    stats['ease'] = round(ease, 2); stats['repetitions'] = reps; stats['interval'] = interval; stats['due'] = (date.today() + timedelta(days=interval)).isoformat(); stats['last_review'] = now_string(); stats['seen'] = safe_int(stats.get('seen', 0), 0) + 1
    if rating >= 3:
        stats['ok'] = safe_int(stats.get('ok', 0), 0) + 1
    else:
        stats['review'] = safe_int(stats.get('review', 0), 0) + 1

def _ms_v8_anki_review_today(self):
    cards = self.due_cards()
    if not cards:
        messagebox.showinfo('Anki', 'No hay tarjetas vencidas para hoy. ¡Buen trabajo!'); return
    c = self.palette(); win = tk.Toplevel(self.root); win.title('Anki Michi · Repaso de hoy'); win.geometry('650x560'); win.configure(bg=c['bg']); tk.Label(win, text='Repaso espaciado de hoy', bg=c['bg'], fg=c['primary'], font=('Arial', 17, 'bold')).pack(pady=10); random.shuffle(cards); state = {'i': 0, 'front': True, 'done': 0}; info = tk.Label(win, text='', bg=c['bg'], fg=c['muted'], font=('Arial', 10, 'bold')); info.pack(); frame = tk.Frame(win, bg='#fffdfd', highlightbackground=c['secondary'], highlightthickness=2); frame.pack(fill='both', expand=True, padx=35, pady=18); side = tk.Label(frame, text='Pregunta', bg='#fffdfd', fg=c['primary'], font=('Arial', 11, 'bold')); side.pack(pady=(18, 4)); textw = tk.Label(frame, text='', bg='#fffdfd', fg=c['text'], font=('Arial', 18, 'bold'), wraplength=500, justify='center')
    textw.pack(expand=True, padx=18, pady=14); hint = tk.Label(frame, text='', bg='#fffdfd', fg=c['muted'], font=('Arial', 10, 'italic')); hint.pack(pady=(0, 14))

    def current():
        return cards[state['i']]

    def render():
        if state['i'] >= len(cards):
            textw.config(text=f"Sesión lista ✨\nRepasaste {state['done']} tarjetas."); side.config(text='Fin'); hint.config(text='Michi está orgulloso de ti.'); return
        subj, card = current(); front = state['front']; bg = '#fffdfd' if front else '#fff2f7'
        for w in (frame, side, textw, hint):
            w.config(bg=bg)
        side.config(text='Pregunta' if front else 'Respuesta'); textw.config(text=card.get('q', '') if front else card.get('a', '')); st = card.get('stats', {}); info.config(text=f"{state['i'] + 1}/{len(cards)} · {subj} · intervalo {st.get('interval', 0)}d · facilidad {st.get('ease', 2.5)}"); hint.config(text='Voltea y califica tu memoria.' if front else 'Elige qué tan bien la recordaste.')

    def flip():
        state.update(front=not state['front']); render()

    def rate(r):
        if state['i'] >= len(cards):
            return
        subj, card = current(); self.apply_anki_rating(card, r); state['i'] += 1; state['front'] = True; state['done'] += 1; self.add_rewards(fresas=1 + r, xp=2 + r * 2, pet_xp=1 + r); self.save(); self.refresh_all(); render()
    for w in (frame, side, textw, hint):
        w.bind('<Button-1>', lambda e: flip())
    row = tk.Frame(win, bg=c['bg']); row.pack(fill='x', padx=20, pady=8); tk.Button(row, text='Voltear', command=flip, bg=c['accent']).pack(side='left', fill='x', expand=True, padx=3)
    for label, r, bg in [('Olvidé', 1, '#ffd0d0'), ('Difícil', 2, '#fff1b8'), ('Bien', 3, '#d6f5df'), ('Fácil', 4, '#d7ecff')]:
        tk.Button(row, text=label, command=lambda x=r: rate(x), bg=bg).pack(side='left', fill='x', expand=True, padx=3)
    render()

def _ms_v8_flashcard_write_mode(self):
    subject = self.selected_subject() if hasattr(self, 'selected_subject') else None
    if not subject:
        messagebox.showerror('Flashcards', 'Selecciona una materia.'); return
    cards = self.subject_data(subject).get('flashcards', [])
    if not cards:
        messagebox.showinfo('Flashcards', 'No hay tarjetas.'); return
    c = self.palette(); win = tk.Toplevel(self.root); win.title('Escribir respuesta'); win.geometry('640x520'); win.configure(bg=c['bg']); tk.Label(win, text=f'Modo escribir · {subject}', bg=c['bg'], fg=c['primary'], font=('Arial', 16, 'bold')).pack(pady=10); random.shuffle(cards); state = {'i': 0, 'score': 0}; q = tk.Label(win, text='', bg=c['bg'], fg=c['text'], font=('Arial', 15, 'bold'), wraplength=560); q.pack(padx=20, pady=12); ans = tk.Text(win, height=5, wrap='word'); ans.pack(fill='x', padx=20, pady=6); fb = tk.Label(win, text='', bg=c['bg'], fg=c['muted'], wraplength=560, justify='left'); fb.pack(padx=20, pady=6)

    def render():
        if state['i'] >= min(10, len(cards)):
            q.config(text=f"Terminado: {state['score']}/{min(10, len(cards))}"); ans.destroy(); btn.config(text='Cerrar', command=win.destroy); self.save(); self.refresh_all(); return
        ans.delete('1.0', tk.END); fb.config(text=''); q.config(text=cards[state['i']].get('q', ''))

    def check():
        card = cards[state['i']]; expected = card.get('a', '').lower(); user = ans.get('1.0', tk.END).strip().lower(); keywords = [w.strip('.,;:()') for w in expected.split() if len(w) > 3]; hit = sum((1 for w in keywords if w in user)); ok = user and (hit >= max(1, len(keywords) // 3) or user in expected); self.apply_anki_rating(card, 3 if ok else 1)
        if ok:
            state['score'] += 1; fb.config(text='Correcto o muy cerca ✅')
        else:
            fb.config(text=f"Repasar 🔁 Respuesta: {card.get('a', '')}")
        state['i'] += 1; win.after(900, render)
    btn = tk.Button(win, text='Comprobar', command=check, bg=c['accent']); btn.pack(fill='x', padx=20, pady=10); render()

def _ms_v8_create_flashcards_from_notes(self):
    subject = self.selected_subject() if hasattr(self, 'selected_subject') else None
    if not subject:
        messagebox.showerror('Flashcards', 'Selecciona una materia.'); return
    notes = self.subject_data(subject).get('notes', '')
    if not notes.strip():
        messagebox.showinfo('Flashcards', 'No hay apuntes para convertir.'); return
    added = 0; cards = self.subject_data(subject).setdefault('flashcards', [])
    for line in notes.splitlines():
        line = line.strip()
        if ':' in line and len(line) > 10:
            q, a = line.split(':', 1)
            if len(q.strip()) > 2 and len(a.strip()) > 3:
                cards.append({'q': q.strip(), 'a': a.strip(), 'category': 'Desde apuntes', 'difficulty': 'Normal', 'favorite': False, 'stats': {'ease': 2.5, 'interval': 0, 'repetitions': 0, 'due': today_string(), 'ok': 0, 'review': 0, 'seen': 0}}); added += 1
    self.save(); self.refresh_all(); messagebox.showinfo('Flashcards', f'Creé {added} flashcards desde apuntes.')

def _ms_v8_refresh_control_center(self):
    _ms_v8_old_refresh_control_center(self)
    try:
        stats = self.user_data.get('study_stats', {}); by = stats.get('by_subject', {}); extra = '\n\nESTADÍSTICAS VISUALES PRO\n'; extra += f"Minutos totales estudiados: {stats.get('total_minutes', 0)}\n"
        for subj, mins in sorted(by.items(), key=lambda x: x[1], reverse=True)[:6]:
            bars = '█' * max(1, min(20, mins // 10 if isinstance(mins, int) else 1)); extra += f'{subj}: {bars} {mins} min\n'
        due = len(self.due_cards()) if hasattr(self, 'due_cards') else 0; extra += f'Flashcards vencidas hoy: {due}\n'; self.control_text.insert(tk.END, extra)
    except Exception:
        pass

def _ms_v8_finish_timer(self, mode):
    _ms_v7_finish_timer(self, mode) if '_ms_v7_finish_timer' in globals() else None
    if mode == 'study':
        mins = safe_int(self.user_data.get('pomodoro', {}).get('study_minutes', 25), 25); stats = self.user_data.setdefault('study_stats', {'total_minutes': 0, 'by_subject': {}, 'sessions': []}); stats['total_minutes'] = safe_int(stats.get('total_minutes', 0), 0) + mins; subject = 'General'
        try:
            idx = self.selected_event_index() if hasattr(self, 'selected_event_index') else None
            if idx is not None:
                subject = self.user_data.get('planner_events', [])[idx].get('subject') or 'General'
        except Exception:
            pass
        stats.setdefault('by_subject', {})[subject] = safe_int(stats.setdefault('by_subject', {}).get(subject, 0), 0) + mins; stats.setdefault('sessions', []).append({'date': now_string(), 'minutes': mins, 'subject': subject}); stats['sessions'] = stats['sessions'][-200:]; self.save()

def _ms_v9_build_library_tab(self):
    c = self.palette()
    for widget in self.library_tab.winfo_children():
        widget.destroy()
    main = tk.Frame(self.library_tab, bg=c['bg']); main.pack(fill='both', expand=True, padx=10, pady=10); main.grid_columnconfigure(0, weight=1, uniform='library_cols'); main.grid_columnconfigure(1, weight=1, uniform='library_cols'); main.grid_rowconfigure(0, weight=1); left = tk.Frame(main, bg=c['bg']); left.grid(row=0, column=0, sticky='nsew', padx=(0, 8)); right = tk.Frame(main, bg=c['bg']); right.grid(row=0, column=1, sticky='nsew', padx=(8, 0)); lib = self.card(left, 'Biblioteca personal', '📖'); lib.pack(fill='both', expand=True, pady=6); lib_body = self.card_content(lib); list_wrap, self.library_list = self.v9_scrollbox(lib_body, height=14); list_wrap.pack(fill='both', expand=True, pady=(0, 8)); self.library_list.bind('<<ListboxSelect>>', lambda e: self.preview_library_item()); btns = tk.Frame(lib_body, bg=c['card'])
    btns.pack(fill='x'); self.v9_button(btns, 'Agregar recurso', self.add_library_item, c['accent'], side='left', fill='x', expand=True, padx=3, ipady=7); self.v9_button(btns, 'Adjuntar archivo', self.add_library_file, '#cfe8ff', side='left', fill='x', expand=True, padx=3, ipady=7); self.v9_button(btns, 'Eliminar', self.delete_library_item, c['danger'], side='left', fill='x', expand=True, padx=3, ipady=7); detail = self.card(right, 'Detalle del recurso', '🔖'); detail.pack(fill='both', expand=True, pady=6); detail_body = self.card_content(detail); detail_wrap, self.library_detail = self.v9_textbox(detail_body, height=13); detail_wrap.pack(fill='both', expand=True, pady=(0, 8)); detail_btns = tk.Frame(detail_body, bg=c['card']); detail_btns.pack(fill='x')
    self.v9_button(detail_btns, 'Abrir recurso', self.open_library_item, '#e4d5ff', side='left', fill='x', expand=True, padx=3, ipady=7); self.v9_button(detail_btns, 'Marcar terminado', self.toggle_library_done, '#d7f4dc', side='left', fill='x', expand=True, padx=3, ipady=7); self.v9_button(detail_btns, 'Guardar notas', self.save_library_notes, c['accent'], side='left', fill='x', expand=True, padx=3, ipady=7); self.refresh_library()

def _ms_v9_style_buttons_deep(self, widget):
    c = self.palette()
    for child in widget.winfo_children():
        if isinstance(child, tk.Button):
            try:
                child.configure(relief='flat', bd=0, fg=c['text'], activebackground=c['secondary'], font=self.app_font(10, 'bold'), cursor='hand2')
            except Exception:
                pass
        self.v9_style_buttons_deep(child)

def _ms_v10_scrollbox(self, parent, height=6):
    c = self.palette(); wrap = tk.Frame(parent, bg=c['card']); box = tk.Listbox(wrap, height=height, relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], font=self.app_font(10)); box.pack(fill='both', expand=True); return (wrap, box)

def _ms_v10_textbox(self, parent, height=5):
    c = self.palette(); wrap = tk.Frame(parent, bg=c['card']); text = tk.Text(wrap, height=height, wrap='word', relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary'], font=self.app_font(10), padx=8, pady=6); text.pack(fill='both', expand=True); return (wrap, text)

def _ms_v10_build_subjects_tab(self):
    c = self.palette()
    for widget in self.subjects_tab.winfo_children():
        widget.destroy()
    main = tk.Frame(self.subjects_tab, bg=c['bg']); main.pack(fill='both', expand=True, padx=10, pady=10); main.grid_columnconfigure(0, weight=1, uniform='subjects_cols'); main.grid_columnconfigure(1, weight=1, uniform='subjects_cols'); main.grid_rowconfigure(0, weight=1); left = tk.Frame(main, bg=c['bg']); left.grid(row=0, column=0, sticky='nsew', padx=(0, 8)); right = tk.Frame(main, bg=c['bg']); right.grid(row=0, column=1, sticky='nsew', padx=(8, 0)); subjects = self.card(left, 'Ingresa tus materias', '📚'); subjects.pack(fill='both', expand=True, pady=6); subjects_body = self.card_content(subjects); form = tk.Frame(subjects_body, bg=c['card']); form.pack(fill='x', pady=(0, 8))
    self.subject_entry = tk.Entry(form, font=self.app_font(11), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary']); self.subject_entry.pack(side='left', fill='x', expand=True, padx=(0, 6), ipady=7); self.v9_button(form, 'Agregar', self.add_subject, c['accent'], side='left', ipady=7); self.subject_list = tk.Listbox(subjects_body, height=6, relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], font=self.app_font(10)); self.subject_list.pack(fill='both', expand=True, pady=(0, 8)); self.subject_list.bind('<<ListboxSelect>>', lambda e: self.load_selected_subject()); self.v9_button(subjects_body, 'Eliminar materia', self.delete_subject, c['danger'], fill='x', pady=(0, 2), ipady=7); notes = self.card(left, 'Apuntes y archivos', '📝')
    notes.pack(fill='both', expand=True, pady=6); notes_body = self.card_content(notes); self.notes_title = tk.Label(notes_body, text='Selecciona o crea una materia', bg=c['card'], fg=c['text'], font=self.app_font(11, 'bold')); self.notes_title.pack(anchor='w', pady=(0, 6)); self.subject_notes_text = tk.Text(notes_body, wrap='word', height=5, font=self.app_font(10), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary'], padx=10, pady=8); self.subject_notes_text.pack(fill='both', expand=True, pady=(0, 8)); btns = tk.Frame(notes_body, bg=c['card']); btns.pack(fill='x', pady=(0, 8)); self.v9_button(btns, 'Guardar apuntes', self.save_subject_notes, c['accent'], side='left', fill='x', expand=True, padx=(0, 4), ipady=7)
    self.v9_button(btns, 'Subir archivo', self.add_subject_file, '#cfe8ff', side='left', fill='x', expand=True, padx=(4, 0), ipady=7); self.subject_files_list = tk.Listbox(notes_body, height=3, relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], font=self.app_font(10)); self.subject_files_list.pack(fill='x', pady=(0, 8)); file_btns = tk.Frame(notes_body, bg=c['card']); file_btns.pack(fill='x'); self.v9_button(file_btns, 'Abrir archivo', self.open_subject_file, '#e4d5ff', side='left', fill='x', expand=True, padx=(0, 4), ipady=7); self.v9_button(file_btns, 'Quitar archivo', self.delete_subject_file, c['danger'], side='left', fill='x', expand=True, padx=(4, 0), ipady=7); grade_card = self.card(right, 'Calificaciones', '🧮'); grade_card.pack(fill='both', expand=True, pady=6); grade_body = self.card_content(grade_card)
    self.grade_title = tk.Label(grade_body, text='Selecciona una materia para ver sus calificaciones', bg=c['card'], fg=c['text'], font=self.app_font(11, 'bold')); self.grade_title.pack(anchor='w', pady=(0, 6)); self.subjects_summary_label = tk.Label(grade_body, text='', bg=c['soft'], fg=c['muted'], font=self.app_font(9, 'bold'), justify='left', wraplength=440, padx=10, pady=6); self.subjects_summary_label.pack(fill='x', pady=(0, 8)); gform = tk.Frame(grade_body, bg=c['card']); gform.pack(fill='x', pady=(0, 8))
    for col, weight in enumerate([2, 1, 1, 0]):
        gform.grid_columnconfigure(col, weight=weight)
    self.grade_name_entry = tk.Entry(gform, font=self.app_font(10), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary']); self.grade_name_entry.grid(row=0, column=0, sticky='ew', padx=(0, 5), ipady=7); self.grade_name_entry.insert(0, 'Actividad'); self.grade_value_entry = tk.Entry(gform, font=self.app_font(10), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary'], justify='center'); self.grade_value_entry.grid(row=0, column=1, sticky='ew', padx=5, ipady=7); self.grade_value_entry.insert(0, '5.0'); self.grade_weight_entry = tk.Entry(gform, font=self.app_font(10), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary'], justify='center')
    self.grade_weight_entry.grid(row=0, column=2, sticky='ew', padx=5, ipady=7); self.grade_weight_entry.insert(0, '%'); self.v9_button(gform, 'Agregar', self.add_grade, c['accent']).grid(row=0, column=3, sticky='ns', padx=(5, 0), ipady=7); self.grade_list = ttk.Treeview(grade_body, columns=('name', 'value', 'weight'), show='headings', height=5); self.grade_list.heading('name', text='Actividad'); self.grade_list.heading('value', text='Nota'); self.grade_list.heading('weight', text='%'); self.grade_list.column('name', width=170, anchor='w'); self.grade_list.column('value', width=70, anchor='center'); self.grade_list.column('weight', width=70, anchor='center'); self.grade_list.pack(fill='both', expand=True, pady=(0, 6)); self.v9_button(grade_body, 'Eliminar nota', self.delete_grade, c['danger'], fill='x', pady=4, ipady=7)
    self.grade_average = tk.Label(grade_body, text='', bg=c['card'], fg=c['primary'], font=self.app_font(11, 'bold')); self.grade_average.pack(anchor='center', pady=4); flash = self.card(right, 'Flashcards pro con repaso', '🃏'); flash.pack(fill='both', expand=True, pady=6); flash_body = self.card_content(flash); flash_form = tk.Frame(flash_body, bg=c['card']); flash_form.pack(fill='x', pady=(0, 8)); flash_form.grid_columnconfigure(0, weight=1); flash_form.grid_columnconfigure(1, weight=1); self.flash_q_entry = tk.Entry(flash_form, font=self.app_font(10), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary']); self.flash_q_entry.grid(row=0, column=0, sticky='ew', padx=(0, 4), ipady=7); self.flash_q_entry.insert(0, 'Pregunta')
    self.flash_a_entry = tk.Entry(flash_form, font=self.app_font(10), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary']); self.flash_a_entry.grid(row=0, column=1, sticky='ew', padx=4, ipady=7); self.flash_a_entry.insert(0, 'Respuesta'); self.v9_button(flash_form, 'Agregar', self.add_flashcard, c['accent']).grid(row=0, column=2, sticky='ns', padx=(4, 0), ipady=7); flash_meta = tk.Frame(flash_body, bg=c['card']); flash_meta.pack(fill='x', pady=(0, 8)); flash_meta.grid_columnconfigure(1, weight=1); ttk.Combobox(flash_meta, textvariable=self.flash_difficulty_var, values=['Fácil', 'Normal', 'Difícil'], state='readonly', width=9).grid(row=0, column=0, sticky='ns', padx=(0, 4))
    self.flash_tags_entry = tk.Entry(flash_meta, font=self.app_font(10), relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary']); self.flash_tags_entry.grid(row=0, column=1, sticky='ew', padx=4, ipady=7); self.flash_tags_entry.insert(0, 'Categoría o tags'); ttk.Combobox(flash_meta, textvariable=self.flash_filter_var, values=['Todas', 'Para hoy', 'Favoritas', 'Difíciles'], state='readonly', width=10).grid(row=0, column=2, sticky='ns', padx=4); self.v9_button(flash_meta, 'Filtrar', self.load_selected_subject, '#fff1b8').grid(row=0, column=3, sticky='ns', padx=(4, 0), ipady=7); self.flash_stats_label = tk.Label(flash_body, text='', bg=c['card'], fg=c['muted'], justify='left'); self.flash_stats_label.pack(anchor='w', pady=2)
    self.flash_list = tk.Listbox(flash_body, height=5, relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], font=self.app_font(10)); self.flash_list.pack(fill='both', expand=True, pady=(0, 8)); self.flash_list.bind('<Double-Button-1>', lambda e: self.edit_flashcard()); fbtns = tk.Frame(flash_body, bg=c['card']); fbtns.pack(fill='x')
    for col in range(4):
        fbtns.grid_columnconfigure(col, weight=1, uniform='flash_buttons_clean')
    self.v9_button(fbtns, 'Practicar', self.practice_flashcards, '#cfe8ff').grid(row=0, column=0, sticky='ew', padx=(0, 4), ipady=7); self.v9_button(fbtns, 'Hoy', lambda: self.practice_flashcards(only_due=True), '#d6f5df').grid(row=0, column=1, sticky='ew', padx=4, ipady=7); self.v9_button(fbtns, 'Editar', self.edit_flashcard, '#fff1b8').grid(row=0, column=2, sticky='ew', padx=4, ipady=7); self.v9_button(fbtns, 'Eliminar', self.delete_flashcard, c['danger']).grid(row=0, column=3, sticky='ew', padx=(4, 0), ipady=7); quick = tk.Frame(flash_body, bg=c['card']); quick.pack(fill='x', pady=(6, 0))
    for col in range(2):
        quick.grid_columnconfigure(col, weight=1, uniform='flash_quick_clean')
    self.v9_button(quick, 'Importar lote', self.bulk_add_flashcards, '#ead7ff').grid(row=0, column=0, sticky='ew', padx=(0, 4), ipady=6); self.v9_button(quick, 'Crear desde apuntes', self.create_flashcards_from_notes, '#d7ecff').grid(row=0, column=1, sticky='ew', padx=(4, 0), ipady=6); self.refresh_subjects()

def _ms_v12_draw_mood_chart(self, moods):
    if not hasattr(self, 'mood_canvas'):
        return
    c = self.palette(); canvas = self.mood_canvas; canvas.delete('all'); width = max(150, canvas.winfo_width() or 190); height = max(36, canvas.winfo_height() or 42); canvas.create_rectangle(3, 3, width - 3, height - 3, fill=c['soft'], outline=c['secondary'])
    if not moods:
        canvas.create_text(width // 2, height // 2, text='Sin datos', fill=c['muted'], font=self.app_font(8, 'bold')); return
    values = [self.mood_score(m) for m in moods[-7:]]; maxv = max(10, max(values)); step = (width - 22) / max(1, len(values) - 1); points = []
    for i, val in enumerate(values):
        x = 11 + i * step; y = height - 9 - val / maxv * (height - 18); points.append((x, y))
    for i in range(1, len(points)):
        canvas.create_line(points[i - 1][0], points[i - 1][1], points[i][0], points[i][1], fill=c['primary'], width=2)
    for x, y in points:
        canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill=c['primary'], outline='')

def _ms_v12_set_shop_selection(self, index):
    self._selected_shop_index = index
    if hasattr(self, 'shop_list'):
        try:
            self.shop_list.selection_clear(0, tk.END); self.shop_list.selection_set(index)
        except Exception:
            pass
    self.preview_shop_item()
    try:
        self.refresh_shop_cards()
    except Exception:
        pass

def _ms_v12_buy_shop_item(self):
    if not getattr(self, '_shop_index_map', None):
        messagebox.showerror('Tienda', 'No hay items para comprar.'); return
    index = getattr(self, '_selected_shop_index', 0)
    if index >= len(self._shop_index_map):
        index = 0
    item = self._shop_index_map[index]
    if self.user_data['currency']['fresas'] < item['price']:
        messagebox.showerror('Tienda', f"Necesitas {item['price']} fresas."); return
    self.user_data['currency']['fresas'] -= item['price']
    if item['slot'].startswith('consumable'):
        self.apply_consumable(item)
    else:
        inventory_item = {k: v for k, v in item.items() if k != 'price'}; inventory_item['bought_at'] = now_string(); self.user_data['inventory'].append(inventory_item)
    self.user_data['shop_history'].append({'date': now_string(), 'item': item['name'], 'price': item['price']}); self.add_achievement(f"Compraste {item['name']}"); self.save(); self.refresh_all(); messagebox.showinfo('Tienda', f"Compraste: {item.get('icon', '🎁')} {item.get('name', 'Item')}")

def _ms_v12_center_cat_canvas(self, canvas, item=None):
    c = self.palette(); canvas.delete('all'); w = max(240, canvas.winfo_width() or 260); h = max(220, canvas.winfo_height() or 250); canvas.create_rectangle(8, 8, w - 8, h - 8, fill=c['card'], outline=c['secondary'], width=2); canvas.create_oval(w // 2 - 48, h // 2 - 42, w // 2 + 48, h // 2 + 54, fill='#fff7fb', outline=c['secondary'], width=2); canvas.create_oval(w // 2 - 32, h // 2 - 92, w // 2 + 32, h // 2 - 30, fill='#fff7fb', outline=c['secondary'], width=2); canvas.create_polygon(w // 2 - 30, h // 2 - 78, w // 2 - 48, h // 2 - 116, w // 2 - 10, h // 2 - 92, fill='#fff7fb', outline=c['secondary']); canvas.create_polygon(w // 2 + 30, h // 2 - 78, w // 2 + 48, h // 2 - 116, w // 2 + 10, h // 2 - 92, fill='#fff7fb', outline=c['secondary']); canvas.create_oval(w // 2 - 18, h // 2 - 62, w // 2 - 10, h // 2 - 54, fill=c['text'], outline='')
    canvas.create_oval(w // 2 + 10, h // 2 - 62, w // 2 + 18, h // 2 - 54, fill=c['text'], outline=''); canvas.create_text(w // 2, h // 2 - 45, text='♡', fill=c['primary'], font=self.app_font(12, 'bold'))
    if item:
        canvas.create_oval(w // 2 + 34, h // 2 - 115, w // 2 + 86, h // 2 - 63, fill=c['soft'], outline=c['secondary'], width=2); canvas.create_text(w // 2 + 60, h // 2 - 90, text=item.get('icon', '🎁'), font=(self.app_font_name(), 24))

def _ms_v13_refresh_moods(self):
    moods = self.user_data.get('moods', [])[-7:]
    if not hasattr(self, 'mood_summary'):
        return
    self.mood_label.config(text=f'Mood actual: {self.quick_mood.get()}')
    if hasattr(self, 'mood_canvas'):
        self.mood_canvas.grid_remove()
    if not moods:
        self.mood_summary.config(text='Sin registros aún. Guarda tu mood para ver tendencia.'); return
    scores = [self.mood_score(m) for m in moods]; energy_values = [safe_int(m.get('energy', 6), 6) for m in moods]; avg = sum(scores) / max(1, len(scores)); energy_avg = sum(energy_values) / max(1, len(energy_values)); trend = 'estable'
    if len(scores) >= 2 and scores[-1] > scores[0] + 0.5:
        trend = 'subiendo'
    elif len(scores) >= 2 and scores[-1] < scores[0] - 0.5:
        trend = 'bajando'
    last = moods[-1]; self.mood_summary.config(text=f"Promedio: {avg:.1f}/10 · Energía: {energy_avg:.1f}/10 · Tendencia {trend}\nÚltimo mood: {last.get('mood', '')}")

def _ms_v13_build_home_tab(self):
    base_home = globals().get('_ms_v7_old_build_home_tab') or globals().get('_ms_v8_old_build_home_tab')
    if base_home:
        base_home(self)
    else:
        _ms_v8_old_build_home_tab(self)
    try:
        if hasattr(self, 'mood_canvas'):
            self.mood_canvas.grid_remove()
        if hasattr(self, 'mood_summary'):
            self.mood_summary.grid_configure(row=0, column=0, columnspan=2, sticky='ew', padx=0); self.mood_summary.configure(wraplength=460, font=self.app_font(9))
        if hasattr(self, 'mood_label'):
            self.mood_label.configure(font=self.app_font(10, 'bold'))
    except Exception:
        pass

def _ms_v14_preview_shop_item(self):
    if not getattr(self, '_shop_index_map', None):
        return
    index = getattr(self, '_selected_shop_index', 0)
    if index >= len(self._shop_index_map):
        index = 0
    item = self._shop_index_map[index]
    if hasattr(self, 'shop_description'):
        self.shop_description.config(text=f"{item.get('icon', '🎁')} {item.get('name', 'Item')} · {item.get('price', 0)} fresas\n{item.get('effect', '')}")
    if hasattr(self, 'shop_preview_canvas'):
        self.shop_preview_canvas.configure(width=230, height=280); self.draw_cat(self.shop_preview_canvas, preview_item=item)

def _ms_v15_build_planner_tab(self):
    c = self.palette()
    for widget in self.planner_tab.winfo_children():
        widget.destroy()
    main = tk.Frame(self.planner_tab, bg=c['bg']); main.pack(fill='both', expand=True, padx=10, pady=8); main.grid_columnconfigure(0, weight=1, uniform='planner_cols'); main.grid_columnconfigure(1, weight=1, uniform='planner_cols'); main.grid_rowconfigure(0, weight=1); left = tk.Frame(main, bg=c['bg']); left.grid(row=0, column=0, sticky='nsew', padx=(0, 8)); right = tk.Frame(main, bg=c['bg']); right.grid(row=0, column=1, sticky='nsew', padx=(8, 0)); cal_card = self.card(left, 'Calendario mensual', '📅'); cal_card.pack(fill='both', expand=True, pady=4); cal_body = self.card_content(cal_card)
    for child in cal_body.winfo_children():
        if getattr(child, 'michi_card_title', False):
            child.pack_configure(pady=(0, 4))
    nav = tk.Frame(cal_body, bg=c['card']); nav.pack(fill='x', pady=(0, 4)); self.v9_button(nav, '◀', lambda: self.change_calendar_month(-1), '#d7ecff', side='left', padx=(0, 4), ipady=5); self.calendar_month_label = tk.Label(nav, text='', bg=c['card'], fg=c['primary'], font=self.app_font(11, 'bold')); self.calendar_month_label.pack(side='left', fill='x', expand=True); self.v9_button(nav, 'Hoy', self.go_calendar_today, '#fff1b8', side='right', padx=(4, 0), ipady=5); self.v9_button(nav, '▶', lambda: self.change_calendar_month(1), '#d6f5df', side='right', padx=4, ipady=5); self.calendar_grid_frame = tk.Frame(cal_body, bg=c['card']); self.calendar_grid_frame.pack(fill='both', expand=True, pady=(0, 0)); event_card = self.card(right, 'Agregar al planificador', '➕'); event_card.pack(fill='x', pady=4); event_body = self.card_content(event_card)
    for child in event_body.winfo_children():
        if getattr(child, 'michi_card_title', False):
            child.pack_configure(pady=(0, 6))
    form = tk.Frame(event_body, bg=c['card']); form.pack(fill='x')
    for col in range(4):
        form.grid_columnconfigure(col, weight=1, uniform='planner_form')
    tk.Label(form, text='Fecha', bg=c['card'], fg=c['text'], font=self.app_font(9, 'bold')).grid(row=0, column=0, sticky='w', padx=(0, 4)); tk.Label(form, text='Hora', bg=c['card'], fg=c['text'], font=self.app_font(9, 'bold')).grid(row=0, column=1, sticky='w', padx=4); tk.Label(form, text='Tipo', bg=c['card'], fg=c['text'], font=self.app_font(9, 'bold')).grid(row=0, column=2, sticky='w', padx=4); tk.Label(form, text='Título', bg=c['card'], fg=c['text'], font=self.app_font(9, 'bold')).grid(row=2, column=0, sticky='w', padx=(0, 4), pady=(5, 0)); tk.Label(form, text='Materia', bg=c['card'], fg=c['text'], font=self.app_font(9, 'bold')).grid(row=2, column=2, sticky='w', padx=4, pady=(5, 0))
    self.plan_date_entry = tk.Entry(form, relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary'], font=self.app_font(10), justify='center'); self.plan_date_entry.grid(row=1, column=0, sticky='ew', padx=(0, 4), ipady=6); self.plan_date_entry.insert(0, getattr(self, 'calendar_selected_date', self.user_data.get('calendar_settings', {}).get('selected_date', today_string()))); self.plan_time_entry = tk.Entry(form, relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary'], font=self.app_font(10), justify='center'); self.plan_time_entry.grid(row=1, column=1, sticky='ew', padx=4, ipady=6); self.plan_time_entry.insert(0, '16:00'); self.plan_type_var = tk.StringVar(value='Estudio')
    ttk.Combobox(form, textvariable=self.plan_type_var, values=['Estudio', 'Tarea', 'Examen', 'Entrega', 'Descanso', 'Repaso', 'Proyecto'], state='readonly', width=9).grid(row=1, column=2, columnspan=2, sticky='ew', padx=(4, 0)); self.plan_title_entry = tk.Entry(form, relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary'], font=self.app_font(10)); self.plan_title_entry.grid(row=3, column=0, columnspan=2, sticky='ew', padx=(0, 4), ipady=6); self.plan_subject_entry = tk.Entry(form, relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary'], font=self.app_font(10)); self.plan_subject_entry.grid(row=3, column=2, columnspan=2, sticky='ew', padx=(4, 0), ipady=6)
    tk.Label(event_body, text='Notas', bg=c['card'], fg=c['text'], font=self.app_font(9, 'bold')).pack(anchor='w', pady=(6, 2)); self.plan_notes_text = tk.Text(event_body, height=2, wrap='word', relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary'], font=self.app_font(10), padx=8, pady=5); self.plan_notes_text.pack(fill='x', pady=(0, 7)); self.v9_button(event_body, 'Agregar evento', self.add_planner_event, c['accent'], fill='x', ipady=7); list_card = self.card(right, 'Eventos del día seleccionado', '🗓'); list_card.pack(fill='both', expand=True, pady=4); list_body = self.card_content(list_card)
    for child in list_body.winfo_children():
        if getattr(child, 'michi_card_title', False):
            child.pack_configure(pady=(0, 6))
    filters = tk.Frame(list_body, bg=c['card']); filters.pack(fill='x', pady=(0, 6))
    for col in range(4):
        filters.grid_columnconfigure(col, weight=1, uniform='planner_filters')
    self.v9_button(filters, 'Día', lambda: self.refresh_planner_events('selected'), '#d7ecff').grid(row=0, column=0, sticky='ew', padx=(0, 3), ipady=6); self.v9_button(filters, 'Hoy', lambda: self.refresh_planner_events('today'), '#fff1b8').grid(row=0, column=1, sticky='ew', padx=3, ipady=6); self.v9_button(filters, 'Pendientes', lambda: self.refresh_planner_events('pending'), '#ead7ff').grid(row=0, column=2, sticky='ew', padx=3, ipady=6); self.v9_button(filters, 'Todos', lambda: self.refresh_planner_events('all'), '#d6f5df').grid(row=0, column=3, sticky='ew', padx=(3, 0), ipady=6); self.planner_list = tk.Listbox(list_body, height=8, relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], font=self.app_font(10)); self.planner_list.pack(fill='both', expand=True, pady=(0, 7)); actions = tk.Frame(list_body, bg=c['card'])
    actions.pack(fill='x'); self.v9_button(actions, 'Completar', self.complete_planner_event, c['accent'], side='left', fill='x', expand=True, padx=(0, 4), ipady=7); self.v9_button(actions, 'Eliminar', self.delete_planner_event, c['danger'], side='left', fill='x', expand=True, padx=(4, 0), ipady=7); self.planner_summary = tk.Label(list_body, text='', bg=c['card'], fg=c['muted'], justify='left', wraplength=430, font=self.app_font(9)); self.planner_summary.pack(fill='x', pady=(5, 0)); week_card = self.card(self.planner_tab, 'Vista semanal conectada', '📆'); week_card.pack(fill='x', padx=18, pady=(0, 8)); week_body = self.card_content(week_card)
    for child in week_body.winfo_children():
        if getattr(child, 'michi_card_title', False):
            child.pack_configure(pady=(0, 5))
    nav_week = tk.Frame(week_body, bg=c['card']); nav_week.pack(fill='x'); self.v9_button(nav_week, '◀ Semana', lambda: self.change_week(-7), '#d7ecff', side='left', padx=(0, 4), ipady=5); self.week_label = tk.Label(nav_week, text='', bg=c['card'], fg=c['primary'], font=self.app_font(10, 'bold')); self.week_label.pack(side='left', fill='x', expand=True); self.v9_button(nav_week, 'Hoy', self.go_week_today, '#fff1b8', side='right', padx=(4, 0), ipady=5); self.v9_button(nav_week, 'Semana ▶', lambda: self.change_week(7), '#d6f5df', side='right', padx=4, ipady=5); self.week_frame = tk.Frame(week_body, bg=c['card']); self.week_frame.pack(fill='x', pady=(5, 0)); self.render_calendar_month(); self.refresh_planner_events('selected')
    if hasattr(self, 'render_week_view'):
        self.render_week_view()

def _ms_v15_render_week_view(self):
    if not hasattr(self, 'week_frame'):
        return
    c = self.palette()
    for w in self.week_frame.winfo_children():
        w.destroy()
    start = self.week_start(); end = date.fromordinal(start.toordinal() + 6); self.week_label.config(text=f'{start.isoformat()} → {end.isoformat()}')
    for col in range(7):
        d = date.fromordinal(start.toordinal() + col); day_events = [e for e in self.user_data.get('planner_events', []) if str(e.get('date', ''))[:10] == d.isoformat()]; frame = tk.Frame(self.week_frame, bg=c['soft'], highlightbackground=c['secondary'], highlightthickness=1, padx=4, pady=4); frame.grid(row=0, column=col, sticky='nsew', padx=2, pady=2); self.week_frame.grid_columnconfigure(col, weight=1, uniform='week_cols_v15'); tk.Label(frame, text=d.strftime('%a\n%d/%m'), bg=c['soft'], fg=c['primary'], font=self.app_font(8, 'bold')).pack(fill='x')
        if not day_events:
            tk.Label(frame, text='Libre', bg=c['soft'], fg=c['muted'], font=self.app_font(8)).pack(pady=4)
        for ev in sorted(day_events, key=lambda e: e.get('time', ''))[:2]:
            status = '✓' if ev.get('done') else '□'; color = {'Examen': '#ffd0d0', 'Entrega': '#ffe0b8', 'Estudio': '#d6f5df', 'Tarea': '#d7ecff'}.get(ev.get('type'), '#fffdfd'); title = str(ev.get('title', ''))[:14]; b = tk.Button(frame, text=f"{status} {ev.get('time', '')}\n{title}", bg=color, fg=c['text'], relief='flat', bd=0, wraplength=72, command=lambda v=ev.get('date'): self.set_selected_date(v), font=self.app_font(8, 'bold'), cursor='hand2'); b.pack(fill='x', pady=1)
        if len(day_events) > 2:
            tk.Label(frame, text=f'+{len(day_events) - 2}', bg=c['soft'], fg=c['muted'], font=self.app_font(8)).pack()

def _ms_v16_next_goal_text(self):
    rules = self.achievement_rules()
    for name, ok, desc in rules:
        if not ok:
            return f'Siguiente meta: {name}\n{desc}'
    return 'Siguiente meta: mantener racha\nYa desbloqueaste todos los logros base. Sigue completando misiones diarias.'

def _ms_v16_build_achievements_tab(self):
    c = self.palette()
    for widget in self.achievements_tab.winfo_children():
        widget.destroy()
    main = tk.Frame(self.achievements_tab, bg=c['bg']); main.pack(fill='both', expand=True, padx=10, pady=8); main.grid_columnconfigure(0, weight=3); main.grid_columnconfigure(1, weight=2); main.grid_rowconfigure(0, weight=1); left = tk.Frame(main, bg=c['bg']); left.grid(row=0, column=0, sticky='nsew', padx=(0, 8)); right = tk.Frame(main, bg=c['bg']); right.grid(row=0, column=1, sticky='nsew', padx=(8, 0)); missions_card = self.card(left, 'Misiones diarias', '🎯'); missions_card.pack(fill='x', pady=4); missions_body = self.card_content(missions_card)
    for child in missions_body.winfo_children():
        if getattr(child, 'michi_card_title', False):
            child.pack_configure(pady=(0, 5))
    self.achievements_missions_frame = tk.Frame(missions_body, bg=c['card']); self.achievements_missions_frame.pack(fill='x'); goals_card = self.card(left, 'Logros desbloqueables', '🏆'); goals_card.pack(fill='both', expand=True, pady=4); goals_body = self.card_content(goals_card)
    for child in goals_body.winfo_children():
        if getattr(child, 'michi_card_title', False):
            child.pack_configure(pady=(0, 5))
    self.achievement_cards_frame = tk.Frame(goals_body, bg=c['card']); self.achievement_cards_frame.pack(fill='both', expand=True); self.achievement_list = tk.Listbox(goals_body, height=1); self.achievement_list.pack_forget(); summary_card = self.card(right, 'Resumen de progreso', '⭐'); summary_card.pack(fill='x', pady=4); summary_body = self.card_content(summary_card)
    for child in summary_body.winfo_children():
        if getattr(child, 'michi_card_title', False):
            child.pack_configure(pady=(0, 5))
    self.achievement_stats_frame = tk.Frame(summary_body, bg=c['card']); self.achievement_stats_frame.pack(fill='x'); self.achievement_summary = tk.Text(summary_body, height=5, wrap='word', relief='flat', bd=0, bg=c['soft'], fg=c['text'], font=self.app_font(9), padx=8, pady=6); self.achievement_summary.pack(fill='x', pady=(8, 0)); next_card = self.card(right, 'Próxima meta', '✨'); next_card.pack(fill='both', expand=True, pady=4); next_body = self.card_content(next_card)
    for child in next_body.winfo_children():
        if getattr(child, 'michi_card_title', False):
            child.pack_configure(pady=(0, 5))
    self.next_goal_label = tk.Label(next_body, text='', bg=c['soft'], fg=c['text'], justify='left', wraplength=340, padx=10, pady=10, font=self.app_font(10, 'bold')); self.next_goal_label.pack(fill='x', pady=(0, 8)); self.achievement_tip_label = tk.Label(next_body, text='Tip: completa una tarea, un pomodoro o una flashcard para mover misiones y logros al mismo tiempo.', bg=c['card'], fg=c['muted'], justify='left', wraplength=340, font=self.app_font(9)); self.achievement_tip_label.pack(fill='x'); self.v9_button(next_body, 'Actualizar progreso', self.refresh_achievements, c['accent'], fill='x', pady=(10, 0), ipady=7); self.refresh_achievements()

def _ms_v16_refresh_achievements(self):
    if not hasattr(self, 'achievement_cards_frame'):
        return
    c = self.palette(); rules = self.achievement_rules(); unlocked = len([1 for _, ok, _ in rules if ok]); total = max(1, len(rules))
    if hasattr(self, 'achievement_list'):
        self.achievement_list.delete(0, tk.END)
    for widget in self.achievements_missions_frame.winfo_children():
        widget.destroy()
    missions = self.get_daily_missions() if hasattr(self, 'get_daily_missions') else []
    for i, m in enumerate(missions[:4]):
        goal = max(1, safe_int(m.get('goal', 1), 1)); progress = min(goal, safe_int(m.get('progress', 0), 0)); done = m.get('done'); row = tk.Frame(self.achievements_missions_frame, bg=c['soft'], padx=8, pady=6, highlightbackground=c['secondary'], highlightthickness=1); row.grid(row=i // 2, column=i % 2, sticky='ew', padx=4, pady=4); self.achievements_missions_frame.grid_columnconfigure(i % 2, weight=1, uniform='mission_cols'); tk.Label(row, text=('✓ ' if done else '□ ') + m.get('title', 'Misión'), bg=c['soft'], fg=c['primary'], font=self.app_font(9, 'bold'), anchor='w').pack(fill='x'); tk.Label(row, text=f"{progress}/{goal} · +{m.get('reward_fresas', 0)} fresas +{m.get('reward_xp', 0)} XP", bg=c['soft'], fg=c['text'], font=self.app_font(8), anchor='w').pack(fill='x'); bar = tk.Canvas(row, height=8, bg=c['soft'], highlightthickness=0)
        bar.pack(fill='x', pady=(4, 0)); bar.update_idletasks(); w = max(80, bar.winfo_width()); bar.create_rectangle(0, 1, w, 7, fill=c['card'], outline=''); bar.create_rectangle(0, 1, int(w * progress / goal), 7, fill=c['primary'], outline='')
    for widget in self.achievement_cards_frame.winfo_children():
        widget.destroy()
    for i, (name, ok, desc) in enumerate(rules):
        bg = '#fff7fb' if ok else c['soft']; tile = tk.Frame(self.achievement_cards_frame, bg=bg, padx=8, pady=7, highlightbackground=c['secondary'], highlightthickness=1); tile.grid(row=i // 2, column=i % 2, sticky='nsew', padx=4, pady=4); self.achievement_cards_frame.grid_columnconfigure(i % 2, weight=1, uniform='ach_cols'); icon = '🏅' if ok else '🔒'; tk.Label(tile, text=f'{icon} {name}', bg=bg, fg=c['primary'], font=self.app_font(9, 'bold'), anchor='w', wraplength=220, justify='left').pack(fill='x'); tk.Label(tile, text=desc, bg=bg, fg=c['muted'], font=self.app_font(8), anchor='w', wraplength=220, justify='left').pack(fill='x', pady=(2, 0))
        if hasattr(self, 'achievement_list'):
            status = '✅' if ok else '🔒'; self.achievement_list.insert(tk.END, f'{status} {name} · {desc}')
    for widget in self.achievement_stats_frame.winfo_children():
        widget.destroy()
    cur = self.user_data.get('currency', {}); pet = self.user_data.get('pet', {}); stats = [('Logros', f'{unlocked}/{total}'), ('Nivel app', str(cur.get('level', 1))), ('XP', f"{cur.get('xp', 0)}/100"), ('Fresas', str(cur.get('fresas', 0))), ('Michi nivel', str(pet.get('level', 1))), ('Felicidad', f"{pet.get('happiness', 0)}%")]
    for i, (label, value) in enumerate(stats):
        box = tk.Frame(self.achievement_stats_frame, bg=c['soft'], padx=8, pady=6, highlightbackground=c['secondary'], highlightthickness=1); box.grid(row=i // 2, column=i % 2, sticky='ew', padx=4, pady=4); self.achievement_stats_frame.grid_columnconfigure(i % 2, weight=1, uniform='stats_cols'); tk.Label(box, text=label, bg=c['soft'], fg=c['muted'], font=self.app_font(8, 'bold')).pack(anchor='w'); tk.Label(box, text=value, bg=c['soft'], fg=c['primary'], font=self.app_font(12, 'bold')).pack(anchor='w')
    text = f'Progreso general: {int(unlocked / total * 100)}% de logros base.\nMisiones visibles arriba para que no tengas que abrir otra ventana.\nUsa esta pestaña como tablero de recompensa y siguiente paso.'; self.achievement_summary.delete('1.0', tk.END); self.achievement_summary.insert('1.0', text)
    if hasattr(self, 'next_goal_label'):
        self.next_goal_label.config(text=self.v16_next_goal_text())

def _ms_v17_ensure_room_data(self):
    room = self.user_data.setdefault('room', {}); room.setdefault('wall_color', room.get('wall', 'Rosa suave')); room.setdefault('floor_color', room.get('floor', 'Madera clara')); room.setdefault('desk', 'Escritorio kawaii'); room.setdefault('bed', 'Cama nube'); room.setdefault('plant', True); room.setdefault('lamp', True); room.setdefault('poster', 'Michi Studio'); room.setdefault('decorations', ['📚', '🍓', '⭐']); room.setdefault('selected_object', ''); room.setdefault('objects', {'cama': {'x': 70, 'y': 240, 'icon': '🛏', 'label': 'Cama'}, 'escritorio': {'x': 285, 'y': 238, 'icon': '📚', 'label': 'Escritorio'}, 'lampara': {'x': 335, 'y': 118, 'icon': '💡', 'label': 'Lámpara'}, 'alfombra': {'x': 200, 'y': 285, 'icon': '🍓', 'label': 'Alfombra'}, 'poster': {'x': 95, 'y': 92, 'icon': '🌸', 'label': 'Póster'}})

def _ms_v17_build_main_ui(self):
    _ms_v17_old_build_main_ui(self)
    try:
        c = self.palette()
        if not hasattr(self, 'room_tab') or not self.room_tab.winfo_exists():
            self.room_tab = tk.Frame(self.notebook, bg=c['bg'])
        tabs = [str(self.notebook.tab(i, 'text')) for i in range(self.notebook.index('end'))]
        if not any(('Habit' in t for t in tabs)):
            insert_at = min(5, self.notebook.index('end')); self.notebook.insert(insert_at, self.room_tab, text='🏡 Habitación')
        if not self.room_tab.winfo_children():
            self.build_room_tab()
    except Exception:
        pass

def _ms_v17_build_room_tab(self):
    c = self.palette(); self.v17_ensure_room_data()
    for widget in self.room_tab.winfo_children():
        widget.destroy()
    main = tk.Frame(self.room_tab, bg=c['bg']); main.pack(fill='both', expand=True, padx=10, pady=10); main.grid_columnconfigure(0, weight=3); main.grid_columnconfigure(1, weight=2); main.grid_rowconfigure(0, weight=1); left = tk.Frame(main, bg=c['bg']); left.grid(row=0, column=0, sticky='nsew', padx=(0, 8)); right = tk.Frame(main, bg=c['bg']); right.grid(row=0, column=1, sticky='nsew', padx=(8, 0)); room_card = self.card(left, 'Habitación del michi', '🏡'); room_card.pack(fill='both', expand=True, pady=4); room_body = self.card_content(room_card)
    for child in room_body.winfo_children():
        if getattr(child, 'michi_card_title', False):
            child.pack_configure(pady=(0, 6))
    self.room_canvas = tk.Canvas(room_body, width=520, height=360, bg=c['card'], highlightthickness=0); self.room_canvas.pack(fill='both', expand=True); self.room_canvas.bind('<Button-1>', self.select_room_object); controls = self.card(right, 'Personalización', '🎨'); controls.pack(fill='x', pady=4); controls_body = self.card_content(controls)
    for child in controls_body.winfo_children():
        if getattr(child, 'michi_card_title', False):
            child.pack_configure(pady=(0, 6))
    room = self.user_data.setdefault('room', {}); tk.Label(controls_body, text='Pared', bg=c['card'], fg=c['text'], font=self.app_font(9, 'bold')).pack(anchor='w'); self.room_wall_var = tk.StringVar(value=room.get('wall_color', 'Rosa suave')); ttk.Combobox(controls_body, textvariable=self.room_wall_var, values=['Rosa suave', 'Lavanda', 'Menta', 'Azul cielo', 'Vainilla', 'Blanco'], state='readonly').pack(fill='x', pady=(2, 6)); tk.Label(controls_body, text='Piso', bg=c['card'], fg=c['text'], font=self.app_font(9, 'bold')).pack(anchor='w'); self.room_floor_var = tk.StringVar(value=room.get('floor_color', 'Madera clara')); ttk.Combobox(controls_body, textvariable=self.room_floor_var, values=['Madera clara', 'Rosa suave', 'Lavanda', 'Menta', 'Azul cielo', 'Vainilla'], state='readonly').pack(fill='x', pady=(2, 6))
    tk.Label(controls_body, text='Póster', bg=c['card'], fg=c['text'], font=self.app_font(9, 'bold')).pack(anchor='w'); self.room_poster_var = tk.StringVar(value=room.get('poster', 'Michi Studio')); ttk.Combobox(controls_body, textvariable=self.room_poster_var, values=['Michi Studio', 'Study mode', 'Fresas', 'Estrellas', 'Biblioteca'], state='readonly').pack(fill='x', pady=(2, 8)); row = tk.Frame(controls_body, bg=c['card']); row.pack(fill='x'); self.v9_button(row, 'Guardar', self.save_room, c['accent'], side='left', fill='x', expand=True, padx=(0, 4), ipady=7); self.v9_button(row, 'Aleatorio', self.randomize_room, '#fff1b8', side='left', fill='x', expand=True, padx=(4, 0), ipady=7); move = self.card(right, 'Mover objetos', '🧸'); move.pack(fill='x', pady=4); move_body = self.card_content(move)
    for child in move_body.winfo_children():
        if getattr(child, 'michi_card_title', False):
            child.pack_configure(pady=(0, 6))
    tk.Label(move_body, text='Haz clic en un objeto y muévelo sin que se salga del cuarto.', bg=c['card'], fg=c['muted'], wraplength=340, justify='left', font=self.app_font(9)).pack(fill='x', pady=(0, 6)); arrows = tk.Frame(move_body, bg=c['card']); arrows.pack(fill='x')
    for col in range(3):
        arrows.grid_columnconfigure(col, weight=1, uniform='room_arrows')
    self.v9_button(arrows, '↑', lambda: self.move_room_object(0, -12), '#d7ecff').grid(row=0, column=1, sticky='ew', padx=3, pady=2, ipady=6); self.v9_button(arrows, '←', lambda: self.move_room_object(-12, 0), '#d7ecff').grid(row=1, column=0, sticky='ew', padx=3, pady=2, ipady=6); self.v9_button(arrows, 'Centro', lambda: self.move_room_object(0, 0, center=True), '#fff1b8').grid(row=1, column=1, sticky='ew', padx=3, pady=2, ipady=6); self.v9_button(arrows, '→', lambda: self.move_room_object(12, 0), '#d7ecff').grid(row=1, column=2, sticky='ew', padx=3, pady=2, ipady=6); self.v9_button(arrows, '↓', lambda: self.move_room_object(0, 12), '#d7ecff').grid(row=2, column=1, sticky='ew', padx=3, pady=2, ipady=6); status = self.card(right, 'Ambiente', '✨'); status.pack(fill='both', expand=True, pady=4); status_body = self.card_content(status)
    for child in status_body.winfo_children():
        if getattr(child, 'michi_card_title', False):
            child.pack_configure(pady=(0, 6))
    self.room_status_label = tk.Label(status_body, text='', bg=c['soft'], fg=c['text'], wraplength=340, justify='left', padx=10, pady=10, font=self.app_font(9, 'bold')); self.room_status_label.pack(fill='x'); self.draw_room()

def _ms_v17_save_room(self):
    self.v17_ensure_room_data(); room = self.user_data.setdefault('room', {})
    if hasattr(self, 'room_wall_var'):
        room['wall_color'] = self.room_wall_var.get()
    if hasattr(self, 'room_floor_var'):
        room['floor_color'] = self.room_floor_var.get()
    if hasattr(self, 'room_poster_var'):
        room['poster'] = self.room_poster_var.get()
    self.user_data.setdefault('metrics', {})['room_customizations'] = self.user_data.setdefault('metrics', {}).get('room_customizations', 0) + 1; self.save(); self.draw_room()

def _ms_v17_randomize_room(self):
    import random as _room_random; self.v17_ensure_room_data(); walls = ['Rosa suave', 'Lavanda', 'Menta', 'Azul cielo', 'Vainilla', 'Blanco']; floors = ['Madera clara', 'Rosa suave', 'Lavanda', 'Menta', 'Azul cielo', 'Vainilla']; posters = ['Michi Studio', 'Study mode', 'Fresas', 'Estrellas', 'Biblioteca']; room = self.user_data.setdefault('room', {}); room['wall_color'] = _room_random.choice(walls); room['floor_color'] = _room_random.choice(floors); room['poster'] = _room_random.choice(posters)
    for obj in room.get('objects', {}).values():
        obj['x'] = _room_random.randint(55, 365); obj['y'] = _room_random.randint(80, 285)
    if hasattr(self, 'room_wall_var'):
        self.room_wall_var.set(room['wall_color'])
    if hasattr(self, 'room_floor_var'):
        self.room_floor_var.set(room['floor_color'])
    if hasattr(self, 'room_poster_var'):
        self.room_poster_var.set(room['poster'])
    self.save_room()

def _ms_v17_refresh_all(self):
    _ms_v17_old_refresh_all(self)
    try:
        if hasattr(self, 'room_canvas'):
            self.draw_room()
    except Exception:
        pass

def _ms_v18_filter_shop_items(self):
    items = list(self.shop_items()); mode = self.shop_filter_var.get() if hasattr(self, 'shop_filter_var') else 'Todos'
    if mode == 'Menor precio':
        return sorted(items, key=lambda item: safe_int(item.get('price', 0), 0))
    if mode == 'Ropa':
        return [i for i in items if i.get('slot') in ('outfit', 'palette')]
    if mode == 'Accesorios':
        return [i for i in items if i.get('slot') == 'accessory']
    if mode == 'Muebles':
        return [i for i in items if i.get('slot') == 'furniture']
    if mode == 'Consumibles':
        return [i for i in items if str(i.get('slot', '')).startswith('consumable')]
    return items

def _ms_v18_refresh_shop(self):
    self._shop_index_map = self.v18_filter_shop_items()
    if not hasattr(self, '_selected_shop_index') or self._selected_shop_index >= len(self._shop_index_map):
        self._selected_shop_index = 0
    if hasattr(self, 'shop_list'):
        self.shop_list.delete(0, tk.END)
        for item in self._shop_index_map:
            self.shop_list.insert(tk.END, f"{item.get('icon', '🎁')} {item.get('name', 'Item')}")
        if self._shop_index_map:
            self.shop_list.selection_set(self._selected_shop_index)
    self.refresh_shop_cards()
    if self._shop_index_map:
        self.preview_shop_item()

def _ms_v18_set_inventory_selection(self, index):
    self._selected_inventory_index = index
    if hasattr(self, 'inventory_list'):
        self.inventory_list.selection_clear(0, tk.END); self.inventory_list.selection_set(index)
    self.preview_inventory_item(); self.refresh_inventory_cards()

def _ms_v18_refresh_inventory_cards(self):
    if not hasattr(self, 'inventory_cards_frame'):
        return
    c = self.palette()
    for widget in self.inventory_cards_frame.winfo_children():
        widget.destroy()
    items = getattr(self, '_inventory_index_map', [])
    if not items:
        tk.Label(self.inventory_cards_frame, text='Tu inventario está vacío.', bg=c['soft'], fg=c['muted'], padx=10, pady=10, font=self.app_font(10, 'bold')).pack(fill='x', padx=4, pady=4); return
    selected = getattr(self, '_selected_inventory_index', 0)
    for i, item in enumerate(items):
        is_selected = i == selected; bg = c['card'] if is_selected else c['soft']; tile = tk.Frame(self.inventory_cards_frame, bg=bg, padx=8, pady=7, highlightbackground=c['primary'] if is_selected else c['secondary'], highlightthickness=2 if is_selected else 1); tile.grid(row=i // 2, column=i % 2, sticky='nsew', padx=4, pady=4); self.inventory_cards_frame.grid_columnconfigure(i % 2, weight=1, uniform='inventory_cards')
        for text, font_size in [(item.get('icon', '🎁'), 20), (item.get('name', 'Item'), 9), (item.get('slot', 'extra'), 8)]:
            label = tk.Label(tile, text=text, bg=bg, fg=c['primary'] if font_size == 20 else c['text'], font=self.app_font(font_size, 'bold') if font_size != 8 else self.app_font(font_size), wraplength=120, justify='center'); label.pack(fill='x'); label.bind('<Button-1>', lambda e, idx=i: self.v18_set_inventory_selection(idx))
        tile.bind('<Button-1>', lambda e, idx=i: self.v18_set_inventory_selection(idx))
        if is_selected:
            row = tk.Frame(tile, bg=bg); row.pack(fill='x', pady=(5, 0)); self.v9_button(row, 'Usar', self.use_inventory_item, c['accent'], side='left', fill='x', expand=True, padx=(0, 2), ipady=4); self.v9_button(row, 'Eliminar', self.delete_inventory_item, c['danger'], side='left', fill='x', expand=True, padx=(2, 0), ipady=4)

def _ms_v18_refresh_inventory(self):
    self._inventory_index_map = list(self.user_data.get('inventory', []))
    if not hasattr(self, '_selected_inventory_index') or self._selected_inventory_index >= len(self._inventory_index_map):
        self._selected_inventory_index = 0
    if hasattr(self, 'inventory_list'):
        self.inventory_list.delete(0, tk.END)
        if not self._inventory_index_map:
            self.inventory_list.insert(tk.END, 'Tu inventario está vacío.')
        for item in self._inventory_index_map:
            self.inventory_list.insert(tk.END, f"{item.get('icon', '🎁')} {item.get('name', 'Item')}")
        if self._inventory_index_map:
            self.inventory_list.selection_set(self._selected_inventory_index)
    self.refresh_inventory_cards(); self.preview_inventory_item()

def _ms_v18_preview_inventory_item(self):
    item = None; items = getattr(self, '_inventory_index_map', []); index = getattr(self, '_selected_inventory_index', 0)
    if items and index < len(items):
        item = items[index]
    if hasattr(self, 'inventory_preview_canvas'):
        self.inventory_preview_canvas.configure(width=230, height=280); self.draw_cat(self.inventory_preview_canvas, preview_item=item)

def _ms_v18_build_shop_tab(self):
    c = self.palette()
    for widget in self.shop_tab.winfo_children():
        widget.destroy()
    main = tk.Frame(self.shop_tab, bg=c['bg']); main.pack(fill='both', expand=True, padx=10, pady=10); main.grid_columnconfigure(0, weight=3); main.grid_columnconfigure(1, weight=2); main.grid_rowconfigure(0, weight=1); left = tk.Frame(main, bg=c['bg']); left.grid(row=0, column=0, sticky='nsew', padx=(0, 8)); right = tk.Frame(main, bg=c['bg']); right.grid(row=0, column=1, sticky='nsew', padx=(8, 0)); shop = self.card(left, 'Tienda de looks y ayudas', '🛍'); shop.pack(fill='both', expand=True, pady=6); shop_body = self.card_content(shop); filter_row = tk.Frame(shop_body, bg=c['card']); filter_row.pack(fill='x', pady=(0, 8)); tk.Label(filter_row, text='Filtrar', bg=c['card'], fg=c['primary'], font=self.app_font(9, 'bold')).pack(side='left', padx=(0, 6))
    self.shop_filter_var = tk.StringVar(value=getattr(self, 'shop_filter_var', tk.StringVar(value='Todos')).get() if hasattr(self, 'shop_filter_var') else 'Todos'); filter_box = ttk.Combobox(filter_row, textvariable=self.shop_filter_var, values=['Todos', 'Menor precio', 'Ropa', 'Accesorios', 'Muebles', 'Consumibles'], state='readonly', width=14); filter_box.pack(side='left', fill='x', expand=True); filter_box.bind('<<ComboboxSelected>>', lambda e: self.refresh_shop()); scroll_outer, self.shop_cards_frame = self.v13_make_scroll_area(shop_body); scroll_outer.pack(fill='both', expand=True, pady=(0, 8)); self.shop_description = tk.Label(shop_body, text='', bg=c['card'], fg=c['muted'], wraplength=560, justify='left', font=self.app_font(9)); self.shop_description.pack(fill='x', pady=(0, 4)); preview_holder = tk.Frame(shop_body, bg=c['card'])
    preview_holder.pack(fill='x', pady=(2, 0)); self.shop_preview_canvas = tk.Canvas(preview_holder, width=230, height=280, bg=c['card'], highlightthickness=0); self.shop_preview_canvas.pack(anchor='center'); self.shop_list = tk.Listbox(shop_body, height=1); self.shop_list.pack_forget(); inv = self.card(right, 'Inventario y equipamiento', '🎒'); inv.pack(fill='both', expand=True, pady=6); inv_body = self.card_content(inv); inv_scroll, self.inventory_cards_frame = self.v13_make_scroll_area(inv_body); inv_scroll.pack(fill='both', expand=True, pady=(0, 8)); self.inventory_list = tk.Listbox(inv_body, height=1); self.inventory_list.pack_forget(); preview = tk.Frame(inv_body, bg=c['card']); preview.pack(fill='x'); self.inventory_preview_canvas = tk.Canvas(preview, width=230, height=280, bg=c['card'], highlightthickness=0)
    self.inventory_preview_canvas.pack(anchor='center'); self.refresh_shop(); self.refresh_inventory()

def _ms_v18_motivation_text(self):
    phrases = ['Hoy no tienes que hacerlo perfecto, solo avanzar un poquito.', 'Tu progreso también cuenta cuando vas lento.', 'Una tarea pequeña terminada vale más que diez perfectas imaginadas.', 'Respira, ordena una cosa y sigue. Michi te acompaña.', 'Cada check es una fresita para tu yo del futuro.', 'Si te cuesta empezar, hazlo por cinco minutos. Después decides.']
    try:
        idx = datetime.now().minute % len(phrases)
    except Exception:
        idx = 0
    return phrases[idx]

def _ms_v18_refresh_achievements(self):
    _ms_v18_prev_refresh_achievements(self)
    if hasattr(self, 'achievement_summary'):
        self.achievement_summary.delete('1.0', tk.END); self.achievement_summary.insert('1.0', self.v18_motivation_text())

def _ms_v18_refresh_shop_cards(self):
    if not hasattr(self, 'shop_cards_frame'):
        return
    c = self.palette()
    for widget in self.shop_cards_frame.winfo_children():
        widget.destroy()
    self._shop_index_map = getattr(self, '_shop_index_map', self.v18_filter_shop_items()); selected = getattr(self, '_selected_shop_index', 0)
    for i, item in enumerate(self._shop_index_map):
        is_selected = i == selected; bg = c['card'] if is_selected else c['soft']; tile = tk.Frame(self.shop_cards_frame, bg=bg, padx=8, pady=7, highlightbackground=c['primary'] if is_selected else c['secondary'], highlightthickness=2 if is_selected else 1); tile.grid(row=i // 3, column=i % 3, sticky='nsew', padx=4, pady=4); tile.bind('<Button-1>', lambda e, idx=i: self.set_shop_selection(idx))
        for text, font_size, fg in [(item.get('icon', '🎁'), 22, c['primary']), (item.get('name', 'Item'), 9, c['text']), (f"{item.get('price', 0)} fresas", 9, c['primary'])]:
            label = tk.Label(tile, text=text, bg=bg, fg=fg, font=self.app_font(font_size, 'bold'), wraplength=120, justify='center'); label.pack(fill='x'); label.bind('<Button-1>', lambda e, idx=i: self.set_shop_selection(idx))
        if is_selected:
            self.v9_button(tile, 'Comprar', self.buy_shop_item, c['accent'], fill='x', pady=(6, 0), ipady=5)
    for col in range(3):
        self.shop_cards_frame.grid_columnconfigure(col, weight=1, uniform='shop_item_cards_v18')

def _ms_v19_make_scroll_area(self, parent):
    c = self.palette(); outer = tk.Frame(parent, bg=c['card']); canvas = tk.Canvas(outer, bg=c['card'], highlightthickness=0, height=255); scrollbar = tk.Scrollbar(outer, orient='vertical', bg=c['bg'], troughcolor=c['bg'], activebackground=c['secondary'], relief='flat', bd=0, width=12); inner = tk.Frame(canvas, bg=c['card']); window_id = canvas.create_window((0, 0), window=inner, anchor='nw'); canvas.configure(yscrollcommand=scrollbar.set); scrollbar.configure(command=canvas.yview); canvas.pack(side='left', fill='both', expand=True); scrollbar.pack(side='right', fill='y')

    def sync_scroll(event=None):
        canvas.configure(scrollregion=canvas.bbox('all')); canvas.itemconfigure(window_id, width=canvas.winfo_width())

    def wheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units'); return 'break'
    inner.bind('<Configure>', sync_scroll); canvas.bind('<Configure>', sync_scroll); canvas.bind('<MouseWheel>', wheel); inner.bind('<MouseWheel>', wheel); return (outer, inner)

def _ms_v20_build_main_ui(self):
    _ms_v20_old_build_main_ui(self)
    try:
        header = self.root.winfo_children()[0]
        for child in list(header.winfo_children()):
            if isinstance(child, tk.Button) and child.cget('text') in {'Exportar', 'Modo nocturno', 'Misiones', 'Backup', 'Pro'}:
                child.destroy()
        self.v20_apply_theme_to_widgets()
    except Exception:
        pass

def _ms_v20_render_calendar_month(self):
    if not hasattr(self, 'calendar_grid_frame'):
        return
    c = self.palette()
    for widget in self.calendar_grid_frame.winfo_children():
        widget.destroy()
    month_start = self.month_start(); self.calendar_month_label.config(text=month_start.strftime('%B %Y')); selected = getattr(self, 'calendar_selected_date', self.user_data.get('calendar_settings', {}).get('selected_date', today_string())); today = today_string(); grid_bg = c['secondary']; self.calendar_grid_frame.configure(bg=grid_bg); headers = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']
    for col, htxt in enumerate(headers):
        self.calendar_grid_frame.grid_columnconfigure(col, weight=1, uniform='cal_cols_v20'); tk.Label(self.calendar_grid_frame, text=htxt, bg=c['secondary'], fg=c['primary'], font=self.app_font(8, 'bold')).grid(row=0, column=col, sticky='nsew', padx=1, pady=1)
    cal = _ms_v6_calendar.Calendar(firstweekday=0)
    for r, week in enumerate(cal.monthdatescalendar(month_start.year, month_start.month), start=1):
        self.calendar_grid_frame.grid_rowconfigure(r, weight=1, minsize=38)
        for col, d in enumerate(week):
            day_text = d.isoformat(); events = self.events_for_day(day_text); done = len([e for e in events if e.get('done')]); label = str(d.day) + (f'\n{done}/{len(events)}' if events else ''); bg = c['card'] if d.month == month_start.month else c['soft']
            if day_text == selected:
                bg = c['secondary']
            elif day_text == today:
                bg = c['accent']
            tk.Button(self.calendar_grid_frame, text=label, bg=bg, fg=c['text'], relief='flat', bd=0, command=lambda v=day_text: self.set_selected_date(v), height=2, wraplength=58, font=self.app_font(8, 'bold'), cursor='hand2').grid(row=r, column=col, sticky='nsew', padx=1, pady=1)

def _ms_v21_color_luminance(hex_color):
    try:
        value = str(hex_color).lstrip('#'); r, g, b = (int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16)); return (0.299 * r + 0.587 * g + 0.114 * b) / 255
    except Exception:
        return 0.8

def _ms_v21_button(self, parent, text, command=None, bg=None, **pack):
    c = self.palette(); bg = bg or c['accent']; fg = '#2f2630' if _ms_v21_color_luminance(bg) > 0.55 else '#fff7fb'; btn = tk.Button(parent, text=text, command=command, bg=bg, fg=fg, relief='flat', bd=0, activebackground=c['secondary'], activeforeground=c['text'], font=self.app_font(10, 'bold'), cursor='hand2', padx=8, pady=0)
    if pack:
        btn.pack(**pack)
    return btn

def _ms_v21_rebuild_keep_tab(self):
    current = ''
    try:
        current = self.notebook.tab(self.notebook.select(), 'text')
    except Exception:
        pass
    self.build_main_ui()
    if current and hasattr(self, 'notebook'):
        try:
            for i in range(self.notebook.index('end')):
                if self.notebook.tab(i, 'text') == current:
                    self.notebook.select(i); break
        except Exception:
            pass

def _ms_v21_apply_app_font(self):
    self.user_data['profile']['app_font'] = self.font_var.get(); self.save(); self.v21_rebuild_keep_tab()

def _ms_v21_apply_theme_variant(self):
    self.user_data['profile']['theme_variant'] = self.theme_variant.get(); self.save(); self.v21_rebuild_keep_tab()

def _ms_v21_toggle_dark_mode(self):
    profile = self.user_data['profile']; profile['theme_mode'] = 'dark' if profile.get('theme_mode', 'light') == 'light' else 'light'; self.save(); self.v21_rebuild_keep_tab()

def _ms_v21_choose_primary_color(self):
    color = colorchooser.askcolor(title='Color principal')
    if color and color[1]:
        self.user_data['profile']['custom_primary'] = color[1]; self.user_data['profile']['theme_variant'] = 'custom'; self.save(); self.v21_rebuild_keep_tab()

def _ms_v21_choose_bg_color(self):
    color = colorchooser.askcolor(title='Color de fondo')
    if color and color[1]:
        self.user_data['profile']['custom_bg'] = color[1]; self.user_data['profile']['theme_variant'] = 'custom'; self.save(); self.v21_rebuild_keep_tab()

def _ms_v21_style_planner_fonts(self):
    if not hasattr(self, 'planner_tab'):
        return

    def walk(w):
        try:
            if isinstance(w, (tk.Label, tk.Button, tk.Entry, tk.Text, tk.Listbox)):
                current = str(w.cget('font')).lower(); w.configure(font=self.app_font(9, 'bold') if 'bold' in current else self.app_font(10))
        except Exception:
            pass
        for child in w.winfo_children():
            walk(child)
    walk(self.planner_tab)

def _ms_v21_build_planner_tab(self):
    _ms_v21_prev_build_planner_tab(self); self.v21_style_planner_fonts(); self.v20_apply_theme_to_widgets(self.planner_tab)

def _ms_v21_build_settings_tab(self):
    c = self.palette()
    for widget in self.settings_tab.winfo_children():
        widget.destroy()
    main = tk.Frame(self.settings_tab, bg=c['bg']); main.pack(fill='both', expand=True, padx=10, pady=10); main.grid_columnconfigure(0, weight=1, uniform='settings_cols'); main.grid_columnconfigure(1, weight=1, uniform='settings_cols'); left = tk.Frame(main, bg=c['bg']); left.grid(row=0, column=0, sticky='nsew', padx=(0, 8)); right = tk.Frame(main, bg=c['bg']); right.grid(row=0, column=1, sticky='nsew', padx=(8, 0)); themes = self.card(left, 'Temas personalizables', '🎨'); themes.pack(fill='x', pady=4); tb = self.card_content(themes); self.theme_variant = tk.StringVar(value=self.user_data['profile'].get('theme_variant', 'strawberry')); tk.Label(tb, text='Tema', bg=c['card'], fg=c['primary'], font=self.app_font(9, 'bold')).pack(anchor='w')
    ttk.Combobox(tb, textvariable=self.theme_variant, values=['strawberry', 'lavender', 'mint', 'custom'], state='readonly').pack(fill='x', pady=(2, 7)); tk.Label(tb, text='Tipografía', bg=c['card'], fg=c['primary'], font=self.app_font(9, 'bold')).pack(anchor='w'); self.font_var = tk.StringVar(value=self.user_data['profile'].get('app_font', 'Segoe UI')); ttk.Combobox(tb, textvariable=self.font_var, values=APP_FONTS, state='readonly').pack(fill='x', pady=(2, 8)); grid = tk.Frame(tb, bg=c['card']); grid.pack(fill='x')
    for col in range(2):
        grid.grid_columnconfigure(col, weight=1, uniform='theme_buttons')
    self.v9_button(grid, 'Aplicar tipografía', self.apply_app_font, '#ffd9e8').grid(row=0, column=0, sticky='ew', padx=(0, 4), pady=3, ipady=7); self.v9_button(grid, 'Aplicar tema', self.apply_theme_variant, c['accent']).grid(row=0, column=1, sticky='ew', padx=(4, 0), pady=3, ipady=7); self.v9_button(grid, 'Color principal', self.choose_primary_color, '#cfe8ff').grid(row=1, column=0, sticky='ew', padx=(0, 4), pady=3, ipady=7); self.v9_button(grid, 'Color de fondo', self.choose_bg_color, '#e4d5ff').grid(row=1, column=1, sticky='ew', padx=(4, 0), pady=3, ipady=7); self.v9_button(tb, 'Alternar claro / nocturno', self.toggle_dark_mode, '#fff1b8', fill='x', pady=(5, 0), ipady=7); media = self.card(left, 'Conexiones y accesos', '🎧'); media.pack(fill='x', pady=4); mb = self.card_content(media)
    for label, attr, value in [('Spotify URL', 'spotify_entry', self.user_data['profile'].get('spotify_url', 'https://open.spotify.com')), ('YouTube URL', 'youtube_entry', self.user_data['profile'].get('youtube_url', 'https://www.youtube.com'))]:
        tk.Label(mb, text=label, bg=c['card'], fg=c['primary'], font=self.app_font(9, 'bold')).pack(anchor='w'); entry = tk.Entry(mb, relief='flat', bd=0, highlightthickness=1, highlightbackground=c['secondary'], highlightcolor=c['primary'], font=self.app_font(10)); entry.pack(fill='x', pady=(2, 7), ipady=7); entry.insert(0, value); setattr(self, attr, entry)
    self.v9_button(mb, 'Guardar enlaces', self.save_media_links, c['accent'], fill='x', ipady=7); tools = self.card(right, 'Herramientas y optimización', '🧰'); tools.pack(fill='x', pady=4); body = self.card_content(tools); rows = [('Optimizar datos', self.optimize_user_data, c['accent']), ('Backup rápido', self.create_quick_backup, '#cfe8ff'), ('Importar backup', self.import_backup, '#e4d5ff'), ('Misiones', self.open_daily_missions_window, '#d6f5df'), ('Exportar datos', self.export_user_data, '#ead7ff'), ('Panel Pro', self.open_pro_dashboard, '#fff1b8')]
    for i, (text, cmd, bg) in enumerate(rows):
        if i % 2 == 0:
            row = tk.Frame(body, bg=c['card']); row.pack(fill='x'); row.grid_columnconfigure(0, weight=1, uniform='tools'); row.grid_columnconfigure(1, weight=1, uniform='tools')
        self.v9_button(row, text, cmd, bg).grid(row=0, column=i % 2, sticky='ew', padx=(0, 4) if i % 2 == 0 else (4, 0), pady=3, ipady=7)
    pro = self.card(right, 'Inicio Pro y centro de control', '🎛'); pro.pack(fill='both', expand=True, pady=4); pb = self.card_content(pro); self.pro_home_var = tk.BooleanVar(value=self.user_data['settings'].get('pro_home', True)); self.animations_var = tk.BooleanVar(value=self.user_data['settings'].get('animations', True)); self.auto_opt_var = tk.BooleanVar(value=self.user_data['settings'].get('auto_optimize', True)); checks = tk.Frame(pb, bg=c['card']); checks.pack(fill='x', pady=(0, 7))
    for text, var in [('Inicio Pro', self.pro_home_var), ('Animaciones', self.animations_var), ('Auto optimización', self.auto_opt_var)]:
        tk.Checkbutton(checks, text=text, variable=var, bg=c['card'], fg=c['text'], activebackground=c['card'], activeforeground=c['text'], selectcolor=c['soft'], command=self.save_settings_toggles, font=self.app_font(9, 'bold')).pack(side='left', expand=True, fill='x')
    mode = self.user_data.get('profile', {}).get('theme_mode', 'light'); text_bg = c['soft'] if mode == 'dark' else '#ffffff'; self.control_text = tk.Text(pb, height=10, wrap='word', relief='flat', bd=0, bg=text_bg, fg=c['text'], insertbackground=c['text'], highlightthickness=1, highlightbackground=c['secondary'], font=self.app_font(9), padx=8, pady=8); self.control_text.pack(fill='both', expand=True, pady=(0, 7)); self.v9_button(pb, 'Actualizar centro de control', self.refresh_control_center, c['accent'], fill='x', ipady=7); self.refresh_control_center(); self.v20_apply_theme_to_widgets(self.settings_tab)

def _ms_v22_refresh_achievements(self):
    _ms_v20_old_refresh_achievements(self)
    if hasattr(self, 'achievement_summary'):
        c = self.palette(); self.achievement_summary.configure(state='normal', height=4, font=('Georgia', 15, 'italic'), relief='flat', bd=0, wrap='word', bg=c['soft'] if self.user_data.get('profile', {}).get('theme_mode', 'light') == 'dark' else '#ffffff', fg=c['primary']); self.achievement_summary.delete('1.0', tk.END); self.achievement_summary.tag_configure('center', justify='center'); self.achievement_summary.insert('1.0', self.v18_motivation_text(), 'center'); self.achievement_summary.configure(state='disabled')

def _ms_v22_draw_bed(self, canvas, x, y, c, selected=False):
    canvas.create_rectangle(x - 68, y - 28, x + 70, y + 40, fill='#f8d8e6', outline=c['secondary'], width=3); canvas.create_rectangle(x - 58, y - 52, x + 8, y - 20, fill='#fff7fb', outline=c['secondary'], width=2); canvas.create_rectangle(x - 10, y - 46, x + 58, y + 20, fill='#ffd4e4', outline=''); canvas.create_arc(x + 28, y - 18, x + 80, y + 34, start=270, extent=180, fill='#f8d8e6', outline=c['secondary'], width=2)

def _ms_v22_draw_desk(self, canvas, x, y, c, selected=False):
    canvas.create_rectangle(x - 70, y - 22, x + 70, y + 0, fill='#c99568', outline=c['secondary'], width=3); canvas.create_line(x - 50, y, x - 60, y + 62, fill='#8b5e3c', width=5); canvas.create_line(x + 50, y, x + 60, y + 62, fill='#8b5e3c', width=5); canvas.create_rectangle(x - 24, y - 64, x + 42, y - 24, fill=c['soft'], outline=c['secondary'], width=3); canvas.create_rectangle(x - 36, y - 18, x - 10, y - 6, fill='#fff1b8', outline=c['secondary'], width=1); canvas.create_text(x + 9, y - 44, text='✦', fill=c['primary'], font=('Segoe UI', 18, 'bold'))

def _ms_v22_draw_lamp(self, canvas, x, y, c, selected=False):
    canvas.create_line(x, y - 34, x, y + 48, fill=c['secondary'], width=6); canvas.create_polygon(x - 36, y - 34, x + 36, y - 34, x + 20, y - 80, x - 20, y - 80, fill='#fff1b8', outline=c['secondary'], width=2); canvas.create_oval(x - 28, y + 42, x + 28, y + 58, fill=c['soft'], outline=c['secondary'], width=2)

def _ms_v22_draw_rug(self, canvas, x, y, c, selected=False):
    canvas.create_oval(x - 92, y - 30, x + 92, y + 36, fill='#ffd9e8', outline=c['secondary'], width=3); canvas.create_oval(x - 34, y - 16, x + 34, y + 18, fill='#ff7ba4', outline=''); canvas.create_text(x, y + 2, text='♡', fill='#fff7fb', font=('Georgia', 18, 'bold'))

def _ms_v22_draw_poster_obj(self, canvas, x, y, c, selected=False):
    canvas.create_rectangle(x - 48, y - 48, x + 48, y + 48, fill=c['card'], outline=c['secondary'], width=3); canvas.create_rectangle(x - 38, y - 38, x + 38, y + 38, fill=c['soft'], outline=''); canvas.create_text(x, y - 10, text='Michi', fill=c['primary'], font=('Segoe UI', 12, 'bold')); canvas.create_text(x, y + 14, text='Studio', fill=c['muted'], font=('Segoe UI', 10, 'bold'))

def _ms_v22_draw_michi_in_room(self, canvas, mx, my, c):
    pet = self.user_data.get('pet', {}); accessory = pet.get('accessory', 'Moño verde'); outfit = pet.get('outfit', 'Vestido fresa'); hood_color = pet.get('hood_color', 'Rojo fresa'); dress_color = pet.get('dress_color', 'Rojo fresa'); accessory_icons = {'Moño verde': '🎀', 'Moño rosa': '🎀', 'Corona': '👑', 'Lentes': '👓', 'Estrellita': '⭐', 'Libro mini': '📘', 'Ninguno': ''}; canvas.create_oval(mx - 96, my - 98, mx + 96, my + 88, fill=self.color_value(hood_color), outline=''); canvas.create_oval(mx - 80, my - 82, mx + 80, my + 72, fill=self.color_value(dress_color), outline=''); canvas.create_oval(mx - 64, my - 66, mx + 64, my + 58, fill=c['soft'], outline='')
    if getattr(self, 'michi_photo', None):
        canvas.create_image(mx, my - 4, image=self.michi_photo)
    else:
        canvas.create_text(mx, my - 4, text='🐱', font=('Arial', 90))
    canvas.create_rectangle(mx - 98, my + 92, mx + 98, my + 114, fill=c['card'], outline=c['secondary'], width=1); canvas.create_text(mx, my + 103, text=f"{pet.get('name', 'Michi')} · {outfit}", font=('Arial', 9, 'bold'), fill=c['text']); canvas.create_rectangle(mx - 98, my + 118, mx + 98, my + 140, fill=c['card'], outline=c['secondary'], width=1); acc_text = accessory if accessory != 'Ninguno' else 'Sin accesorio'; canvas.create_text(mx, my + 129, text=f"{accessory_icons.get(accessory, '')} {acc_text}".strip(), font=('Arial', 9), fill=c['text'])
    if accessory_icons.get(accessory):
        canvas.create_oval(mx + 62, my - 100, mx + 100, my - 62, fill=c['card'], outline=c['secondary'], width=2); canvas.create_text(mx + 81, my - 81, text=accessory_icons[accessory], font=('Arial', 16))

def _ms_v24_style_ttk(self):
    _ms_v24_prev_style_ttk(self); c = self.palette(); style = ttk.Style(); style.configure('TNotebook.Tab', background=c['soft'], foreground=c['text'], padding=[22, 13], font=self.app_font(12, 'bold'), borderwidth=0); style.map('TNotebook.Tab', background=[('selected', c['primary'])], foreground=[('selected', 'white')]); style.configure('TCombobox', padding=6, font=self.app_font(10)); style.configure('Treeview', font=self.app_font(10), rowheight=28, background=c['card'], fieldbackground=c['card'], foreground=c['text']); style.configure('Treeview.Heading', font=self.app_font(10, 'bold'), background=c['soft'], foreground=c['text'], padding=6)

def _ms_v24_apply_theme_to_widgets(self, widget=None):
    c = self.palette(); mode = self.user_data.get('profile', {}).get('theme_mode', 'light') if self.user_data else 'light'; widget = widget or self.root
    try:
        if widget is getattr(self, 'timer_label', None):
            widget.configure(font=('Consolas', 68, 'bold'), fg=c['primary']); return
        if getattr(widget, 'michi_card_title', False):
            widget.configure(font=self.app_font(16, 'bold'), fg=c['primary'], bg=c['card']); return
        if isinstance(widget, tk.Button) and widget.cget('text') in {'😊', '🤩', '😌', '😴', '😤', '🥺', '😔'}:
            widget.configure(font=('Segoe UI Emoji', 22), width=3, fg=c['text'], bg=c['soft'], activebackground=c['secondary']); return
        if isinstance(widget, tk.Entry):
            bg = c['soft'] if mode == 'dark' else '#ffffff'; widget.configure(bg=bg, fg=c['text'], insertbackground=c['text'], highlightbackground=c['secondary'], highlightcolor=c['primary'])
        elif isinstance(widget, tk.Text):
            bg = c['soft'] if mode == 'dark' else '#ffffff'; widget.configure(bg=bg, fg=c['text'], insertbackground=c['text'], highlightbackground=c['secondary'], highlightcolor=c['primary'])
        elif isinstance(widget, tk.Listbox):
            bg = c['soft'] if mode == 'dark' else '#ffffff'; widget.configure(bg=bg, fg=c['text'], selectbackground=c['secondary'], selectforeground=c['text'], highlightbackground=c['secondary'])
        elif isinstance(widget, tk.Button):
            bg = widget.cget('bg'); fg = '#2f2630' if _ms_v21_color_luminance(bg) > 0.55 else '#fff7fb'; widget.configure(fg=fg, activeforeground=c['text'], font=self.app_font(10, 'bold'))
        elif isinstance(widget, tk.Checkbutton):
            widget.configure(bg=c['card'], fg=c['text'], activebackground=c['card'], activeforeground=c['text'], selectcolor=c['soft'], font=self.app_font(9, 'bold'))
    except Exception:
        pass
    for child in widget.winfo_children():
        self.v20_apply_theme_to_widgets(child)

def _ms_v24_build_study_tab(self):
    _ms_v24_prev_build_study_tab(self)
    try:
        c = self.palette(); self.timer_label.configure(font=('Consolas', 68, 'bold'), fg=c['primary'])
    except Exception:
        pass

def _ms_v24_build_home_tab(self):
    _ms_v24_prev_build_home_tab(self)
    try:
        self.v23_fix_mood_tracker()
    except Exception:
        pass

def _ms_v23_fix_mood_tracker(self):
    if not hasattr(self, 'mood_label'):
        return
    c = self.palette(); mood_emojis = {'😊', '🤩', '😌', '😴', '😤', '🥺', '😔'}

    def walk(widget):
        for child in widget.winfo_children():
            try:
                if isinstance(child, tk.Button) and child.cget('text') in mood_emojis:
                    child.configure(width=3, font=('Segoe UI Emoji', 20), bg=c['soft'], fg=c['text'], activebackground=c['secondary'], activeforeground=c['text'], relief='flat', bd=0)
                elif isinstance(child, tk.Scale):
                    child.configure(bg=c['card'], fg=c['text'], troughcolor=c['soft'], activebackground=c['primary'], highlightthickness=0, font=self.app_font(8, 'bold'))
                elif isinstance(child, tk.Label) and child.cget('text') in {'Intensidad', 'Energía', 'Energia'}:
                    child.configure(bg=c['card'], fg=c['text'], font=self.app_font(9, 'bold'))
            except Exception:
                pass
            walk(child)
    try:
        card = self.mood_label.master; walk(card)
    except Exception:
        pass

def _ms_v23_build_home_tab(self):
    _ms_v23_prev_build_home_tab(self); self.v23_fix_mood_tracker()

def _ms_v25_style_ttk(self):
    _ms_v25_prev_style_ttk(self); c = self.palette(); style = ttk.Style(); style.configure('TNotebook.Tab', background=c['soft'], foreground=c['text'], padding=[14, 7], font=self.app_font(10, 'bold'), borderwidth=0); style.map('TNotebook.Tab', background=[('selected', c['primary'])], foreground=[('selected', 'white')])

def _ms_v25_build_main_ui(self):
    _ms_v25_prev_build_main_ui(self); c = self.palette()
    try:
        header = self.notebook.master.winfo_children()[0]; header.configure(height=76); header.pack_propagate(False)
        for child in header.winfo_children():
            if isinstance(child, tk.Label) and 'Michi Studio' in str(child.cget('text')):
                child.configure(font=(self.app_font_name(), 25, 'bold')); child.pack_configure(padx=24, pady=12)
            elif child is getattr(self, 'header_status', None):
                child.configure(font=(self.app_font_name(), 12, 'bold'), wraplength=520, justify='right'); child.pack_configure(padx=14)
            elif isinstance(child, tk.Button):
                child.configure(relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2'); child.pack_configure(padx=5, ipady=4)
        self.notebook.pack_configure(padx=10, pady=8)
    except Exception:
        pass

def _ms_v25_room_default_positions(self, w, h):
    return {'cama': (120, int(h * 0.76)), 'escritorio': (w - 150, int(h * 0.68)), 'lampara': (w - 72, int(h * 0.38)), 'alfombra': (int(w * 0.52), int(h * 0.83)), 'poster': (115, int(h * 0.31))}

def _ms_v26_style_flashcard_window(self):
    c = self.palette(); wins = [w for w in self.root.winfo_children() if isinstance(w, tk.Toplevel) and 'Repaso inteligente' in str(w.title())]
    if not wins:
        return
    win = wins[-1]

    def walk(widget):
        for child in widget.winfo_children():
            try:
                if isinstance(child, tk.Button):
                    bg = child.cget('bg'); fg = '#2f2630' if _ms_v21_color_luminance(bg) > 0.55 else '#fff7fb'; child.configure(fg=fg, relief='flat', bd=0, activebackground=c['secondary'], activeforeground=c['text'], font=self.app_font(10, 'bold'), cursor='hand2', padx=8, pady=4); child.pack_configure(ipady=7, padx=4)
            except Exception:
                pass
            walk(child)
    walk(win)

def _ms_v26_practice_flashcards(self, only_due=False):
    _ms_v26_prev_practice_flashcards(self, only_due=only_due)
    try:
        self.root.after(80, self.v26_style_flashcard_window)
    except Exception:
        pass

def _ms_v27_select_subject_for_flash_quiz(self, subject):
    subjects = sorted(self.user_data.get('subjects', {}).keys())
    if subject not in subjects:
        return False
    try:
        self._subject_order = subjects; index = subjects.index(subject)
        if hasattr(self, 'subject_list'):
            self.subject_list.selection_clear(0, tk.END); self.subject_list.selection_set(index); self.subject_list.see(index)
        self.load_selected_subject()
    except Exception:
        pass
    return True

def _ms_v27_open_flash_quiz_subject_picker(self):
    c = self.palette(); available = [subject for subject, data in sorted(self.user_data.get('subjects', {}).items()) if len(data.get('flashcards', [])) >= 2]
    if not available:
        messagebox.showinfo('Flash Quiz', 'Necesitas una materia con al menos 2 flashcards para jugar.'); return
    win = tk.Toplevel(self.root); win.title('Elegir materia para Flash Quiz'); win.geometry('390x360'); win.configure(bg=c['bg']); win.resizable(False, False); tk.Label(win, text='Flash Quiz', bg=c['bg'], fg=c['primary'], font=self.app_font(17, 'bold')).pack(pady=(14, 4)); tk.Label(win, text='Elige una materia para jugar con sus flashcards.', bg=c['bg'], fg=c['muted'], font=self.app_font(10, 'bold'), wraplength=330, justify='center').pack(pady=(0, 10)); box_frame = tk.Frame(win, bg=c['card'], padx=10, pady=10, highlightbackground=c['secondary'], highlightthickness=1); box_frame.pack(fill='both', expand=True, padx=20, pady=(0, 12)); listbox = tk.Listbox(box_frame, relief='flat', bd=0, highlightthickness=0, bg=c['soft'], fg=c['text'], selectbackground=c['primary'], selectforeground='white', font=self.app_font(10, 'bold'), activestyle='none')
    listbox.pack(fill='both', expand=True)
    for subject in available:
        total = len(self.user_data['subjects'][subject].get('flashcards', [])); listbox.insert(tk.END, f'{subject}  ·  {total} fichas')
    listbox.selection_set(0)

    def start_selected(event=None):
        sel = listbox.curselection()
        if not sel:
            return
        subject = available[sel[0]]; win.destroy(); self.v27_select_subject_for_flash_quiz(subject); _ms_v27_prev_practice_flashcards_quiz(self)
    listbox.bind('<Double-Button-1>', start_selected); row = tk.Frame(win, bg=c['bg']); row.pack(fill='x', padx=20, pady=(0, 16)); self.v9_button(row, 'Jugar', start_selected, c['accent'], side='left', fill='x', expand=True, padx=(0, 5), ipady=7); self.v9_button(row, 'Cancelar', win.destroy, '#fff1b8', side='left', fill='x', expand=True, padx=(5, 0), ipady=7)

def _ms_v27_practice_flashcards_quiz(self):
    if self.selected_subject():
        _ms_v27_prev_practice_flashcards_quiz(self); return
    self.v27_open_flash_quiz_subject_picker()

def _ms_v28_build_main_ui(self):
    _ms_v28_prev_build_main_ui(self); c = self.palette()
    try:
        header = self.notebook.master.winfo_children()[0]; title_label = None; status_label = getattr(self, 'header_status', None); salir_btn = None; export_btn = None; mode_btn = None
        for child in header.winfo_children():
            text = str(child.cget('text')) if hasattr(child, 'cget') else ''
            if isinstance(child, tk.Label) and 'Michi Studio' in text:
                title_label = child
            elif child is status_label:
                status_label = child
            elif isinstance(child, tk.Button) and text == 'Salir':
                salir_btn = child
            elif isinstance(child, tk.Button) and text == 'Exportar':
                export_btn = child
            elif isinstance(child, tk.Button) and 'Modo' in text:
                mode_btn = child
        for child in header.winfo_children():
            child.pack_forget()
        if title_label:
            title_label.configure(font=(self.app_font_name(), 25, 'bold'), bg=c['primary'], fg='white'); title_label.pack(side='left', padx=24, pady=12)
        for btn in (salir_btn, status_label, export_btn, mode_btn):
            if not btn:
                continue
            if isinstance(btn, tk.Button):
                btn.configure(relief='flat', bd=0, font=self.app_font(10, 'bold'), cursor='hand2', bg='white'); btn.pack(side='right', padx=(4, 10) if btn is salir_btn else 4, ipady=4)
            else:
                btn.configure(font=(self.app_font_name(), 12, 'bold'), bg=c['primary'], fg='white', wraplength=560, justify='right'); btn.pack(side='right', padx=10)
    except Exception:
        pass

def _ms_v28_is_edge_white(pixel):
    try:
        if isinstance(pixel, str):
            pixel = pixel.strip('{}').split()
        r, g, b = [int(v) for v in pixel[:3]]; return r >= 245 and g >= 245 and (b >= 245)
    except Exception:
        return False

def _ms_v28_get_transparent_michi_photo(self):
    self.ensure_michi_assets()
    if not getattr(self, 'michi_photo', None):
        return None
    if getattr(self, 'michi_room_transparent_photo', None) is not None:
        return self.michi_room_transparent_photo
    try:
        src = self.michi_photo; img = tk.PhotoImage(width=src.width(), height=src.height()); img.tk.call(img, 'copy', src); w, h = (img.width(), img.height()); seen = set(); stack = [(x, 0) for x in range(w)] + [(x, h - 1) for x in range(w)] + [(0, y) for y in range(h)] + [(w - 1, y) for y in range(h)]
        while stack:
            x, y = stack.pop()
            if (x, y) in seen or x < 0 or y < 0 or (x >= w) or (y >= h):
                continue
            seen.add((x, y))
            if not _ms_v28_is_edge_white(img.get(x, y)):
                continue
            try:
                img.transparency_set(x, y, True)
            except Exception:
                pass
            stack.extend(((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))
        self.michi_room_transparent_photo = img; return img
    except Exception:
        self.michi_room_transparent_photo = self.michi_photo; return self.michi_photo

def _ms_v28_draw_shop_michi_in_room(self, canvas, mx, my, c):
    photo = self.v28_get_transparent_michi_photo()
    if photo:
        canvas.create_image(mx, my, image=photo, anchor='center')
    else:
        canvas.create_text(mx, my, text='Michi', font=self.app_font(34, 'bold'), fill=c['primary'])

def _ms_v29_hex_to_rgb(color):
    color = str(color or '#ffffff').strip()
    if not color.startswith('#') or len(color) < 7:
        return (255, 255, 255)
    try:
        return tuple((int(color[i:i + 2], 16) for i in (1, 3, 5)))
    except Exception:
        return (255, 255, 255)

def _ms_v29_rgb_to_hex(rgb):
    return '#%02x%02x%02x' % tuple((max(0, min(255, int(v))) for v in rgb))

def _ms_v29_mix(c1, c2, amount=0.5):
    r1, g1, b1 = _ms_v29_hex_to_rgb(c1); r2, g2, b2 = _ms_v29_hex_to_rgb(c2); a = max(0.0, min(1.0, float(amount))); return _ms_v29_rgb_to_hex((r1 + (r2 - r1) * a, g1 + (g2 - g1) * a, b1 + (b2 - b1) * a))

def _ms_v30_room_drawers():
    """Devuelve los dibujadores de muebles una sola vez para no recrear el diccionario en cada frame."""; global _MS_V30_ROOM_DRAWERS
    if _MS_V30_ROOM_DRAWERS is None:
        _MS_V30_ROOM_DRAWERS = {'cama': globals().get('_ms_v22_draw_bed'), 'escritorio': globals().get('_ms_v22_draw_desk'), 'lampara': globals().get('_ms_v22_draw_lamp'), 'alfombra': globals().get('_ms_v22_draw_rug'), 'poster': globals().get('_ms_v22_draw_poster_obj')}
    return _MS_V30_ROOM_DRAWERS

def _ms_v29_canvas_size(canvas, fallback_w=240, fallback_h=280):
    try:
        w = int(canvas.winfo_width() or canvas.cget('width') or fallback_w); h = int(canvas.winfo_height() or canvas.cget('height') or fallback_h)
    except Exception:
        w, h = (fallback_w, fallback_h)
    return (max(120, w), max(140, h))

def _ms_v29_round_rect(canvas, x1, y1, x2, y2, r=18, **kw):
    r = max(2, min(r, abs(x2 - x1) // 2, abs(y2 - y1) // 2)); canvas.create_arc(x1, y1, x1 + 2 * r, y1 + 2 * r, start=90, extent=90, style='pieslice', **kw); canvas.create_arc(x2 - 2 * r, y1, x2, y1 + 2 * r, start=0, extent=90, style='pieslice', **kw); canvas.create_arc(x2 - 2 * r, y2 - 2 * r, x2, y2, start=270, extent=90, style='pieslice', **kw); canvas.create_arc(x1, y2 - 2 * r, x1 + 2 * r, y2, start=180, extent=90, style='pieslice', **kw); canvas.create_rectangle(x1 + r, y1, x2 - r, y2, **kw); canvas.create_rectangle(x1, y1 + r, x2, y2 - r, **kw)

def _ms_v29_draw_sparkles(canvas, w, h, c, phase=0):
    colors = ['#ffffff', c.get('secondary', '#ffd6e8'), c.get('accent', '#ffcf6b')]; points = [(0.14, 0.15, 7), (0.8, 0.18, 6), (0.22, 0.42, 5), (0.86, 0.46, 5), (0.13, 0.72, 4), (0.76, 0.78, 6)]
    for i, (px, py, size) in enumerate(points):
        pulse = 1 + (phase + i) % 3 * 0.12; x, y, s = (int(w * px), int(h * py), int(size * pulse)); fill = colors[i % len(colors)]; canvas.create_line(x - s, y, x + s, y, fill=fill, width=2); canvas.create_line(x, y - s, x, y + s, fill=fill, width=2); canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill=fill, outline='')

def _ms_v29_pet_pose(self):
    phase = int(getattr(self, '_pet_anim_phase', 0)); blink = phase % 9 == 0; bob = int(math.sin(phase / 2.0) * 5); tail = math.sin(phase / 1.4); paw = math.sin(phase / 1.7); return (phase, blink, bob, tail, paw)

def _ms_v29_draw_vector_michi(self, canvas, cx, cy, scale, c, pet, studying=False, accessory='Moño verde', outfit='Vestido fresa', hood_color='Rojo fresa', dress_color='Rojo fresa'):
    phase, blink, bob, tail, paw = _ms_v29_pet_pose(self); cx = int(cx); cy = int(cy + bob); s = float(scale); fur = '#fff7ef'; line = '#5b4638'; hood = self.color_value(hood_color); dress = self.color_value(dress_color); hood_dark = _ms_v29_mix(hood, '#000000', 0.12); dress_dark = _ms_v29_mix(dress, '#000000', 0.1); cheek = '#ffb8c7'; canvas.create_oval(cx - 62 * s, cy + 86 * s, cx + 62 * s, cy + 104 * s, fill=_ms_v29_mix(c.get('muted', '#999999'), '#ffffff', 0.65), outline=''); t = tail * 16 * s; canvas.create_arc(cx + 38 * s, cy + 6 * s + t * 0.25, cx + 108 * s, cy + 88 * s - t * 0.25, start=260, extent=220, style='arc', outline=hood_dark, width=max(8, int(11 * s))); canvas.create_arc(cx + 43 * s, cy + 11 * s + t * 0.25, cx + 100 * s, cy + 78 * s - t * 0.25, start=260, extent=220, style='arc', outline=hood, width=max(5, int(7 * s)))
    canvas.create_oval(cx - 55 * s, cy + 16 * s, cx + 55 * s, cy + 100 * s, fill=dress, outline=hood_dark, width=max(1, int(2 * s))); canvas.create_arc(cx - 54 * s, cy + 34 * s, cx + 54 * s, cy + 118 * s, start=200, extent=140, style='arc', outline=dress_dark, width=max(2, int(3 * s))); canvas.create_oval(cx - 43 * s, cy + 26 * s + paw * 3 * s, cx - 13 * s, cy + 63 * s + paw * 3 * s, fill=fur, outline=line, width=max(1, int(2 * s))); canvas.create_oval(cx + 13 * s, cy + 26 * s - paw * 3 * s, cx + 43 * s, cy + 63 * s - paw * 3 * s, fill=fur, outline=line, width=max(1, int(2 * s))); canvas.create_oval(cx - 42 * s, cy + 84 * s, cx - 8 * s, cy + 110 * s, fill=fur, outline=line, width=max(1, int(2 * s))); canvas.create_oval(cx + 8 * s, cy + 84 * s, cx + 42 * s, cy + 110 * s, fill=fur, outline=line, width=max(1, int(2 * s)))
    if 'sueter' in outfit.lower() or 'pijama' in outfit.lower():
        canvas.create_line(cx - 36 * s, cy + 50 * s, cx + 36 * s, cy + 50 * s, fill=_ms_v29_mix(dress, '#ffffff', 0.35), width=max(2, int(3 * s))); canvas.create_line(cx - 30 * s, cy + 67 * s, cx + 30 * s, cy + 67 * s, fill=_ms_v29_mix(dress, '#ffffff', 0.35), width=max(2, int(3 * s)))
    else:
        canvas.create_polygon(cx - 42 * s, cy + 48 * s, cx + 42 * s, cy + 48 * s, cx + 30 * s, cy + 94 * s, cx - 30 * s, cy + 94 * s, fill=_ms_v29_mix(dress, '#ffffff', 0.18), outline=dress_dark, width=max(1, int(2 * s)))
    canvas.create_polygon(cx - 54 * s, cy - 45 * s, cx - 30 * s, cy - 94 * s, cx - 12 * s, cy - 38 * s, fill=hood, outline=hood_dark, width=max(1, int(2 * s))); canvas.create_polygon(cx + 54 * s, cy - 45 * s, cx + 30 * s, cy - 94 * s, cx + 12 * s, cy - 38 * s, fill=hood, outline=hood_dark, width=max(1, int(2 * s))); canvas.create_polygon(cx - 42 * s, cy - 49 * s, cx - 30 * s, cy - 78 * s, cx - 20 * s, cy - 45 * s, fill='#ffd5de', outline=''); canvas.create_polygon(cx + 42 * s, cy - 49 * s, cx + 30 * s, cy - 78 * s, cx + 20 * s, cy - 45 * s, fill='#ffd5de', outline=''); canvas.create_oval(cx - 62 * s, cy - 64 * s, cx + 62 * s, cy + 42 * s, fill=hood, outline=hood_dark, width=max(1, int(2 * s))); canvas.create_oval(cx - 48 * s, cy - 50 * s, cx + 48 * s, cy + 34 * s, fill=fur, outline=line, width=max(1, int(2 * s)))
    canvas.create_oval(cx - 22 * s, cy - 22 * s, cx - 10 * s, cy - 10 * s, fill=cheek, outline=''); canvas.create_oval(cx + 10 * s, cy - 22 * s, cx + 22 * s, cy - 10 * s, fill=cheek, outline='')
    if blink:
        canvas.create_line(cx - 28 * s, cy - 34 * s, cx - 12 * s, cy - 34 * s, fill=line, width=max(2, int(3 * s))); canvas.create_line(cx + 12 * s, cy - 34 * s, cx + 28 * s, cy - 34 * s, fill=line, width=max(2, int(3 * s)))
    else:
        canvas.create_oval(cx - 30 * s, cy - 42 * s, cx - 14 * s, cy - 25 * s, fill=line, outline=''); canvas.create_oval(cx + 14 * s, cy - 42 * s, cx + 30 * s, cy - 25 * s, fill=line, outline=''); canvas.create_oval(cx - 24 * s, cy - 38 * s, cx - 20 * s, cy - 34 * s, fill='white', outline=''); canvas.create_oval(cx + 20 * s, cy - 38 * s, cx + 24 * s, cy - 34 * s, fill='white', outline='')
    canvas.create_polygon(cx - 5 * s, cy - 23 * s, cx + 5 * s, cy - 23 * s, cx, cy - 15 * s, fill='#e08391', outline=line); canvas.create_arc(cx - 12 * s, cy - 16 * s, cx, cy - 2 * s, start=300, extent=110, style='arc', outline=line, width=max(1, int(2 * s))); canvas.create_arc(cx, cy - 16 * s, cx + 12 * s, cy - 2 * s, start=130, extent=110, style='arc', outline=line, width=max(1, int(2 * s)))
    for side in (-1, 1):
        canvas.create_line(cx + side * 12 * s, cy - 20 * s, cx + side * 38 * s, cy - 27 * s, fill=line, width=max(1, int(2 * s))); canvas.create_line(cx + side * 12 * s, cy - 15 * s, cx + side * 40 * s, cy - 15 * s, fill=line, width=max(1, int(2 * s))); canvas.create_line(cx + side * 12 * s, cy - 10 * s, cx + side * 38 * s, cy - 4 * s, fill=line, width=max(1, int(2 * s)))
    acc_icons = {'Moño verde': ('🎀', '#76c893'), 'Moño rosa': ('🎀', '#ff8fba'), 'Corona': ('👑', '#ffd166'), 'Lentes': ('👓', '#39445a'), 'Estrellita': ('⭐', '#ffd166'), 'Libro mini': ('📘', '#6fb7ff'), 'Ninguno': ('', '')}; icon, color = acc_icons.get(accessory, ('', ''))
    if accessory == 'Lentes':
        canvas.create_oval(cx - 34 * s, cy - 41 * s, cx - 10 * s, cy - 19 * s, outline=color, width=max(2, int(3 * s))); canvas.create_oval(cx + 10 * s, cy - 41 * s, cx + 34 * s, cy - 19 * s, outline=color, width=max(2, int(3 * s))); canvas.create_line(cx - 10 * s, cy - 30 * s, cx + 10 * s, cy - 30 * s, fill=color, width=max(2, int(3 * s)))
    elif icon:
        canvas.create_text(cx + 43 * s, cy - 72 * s, text=icon, font=(self.app_font_name(), max(12, int(20 * s))), fill=color or c.get('primary'))
    if studying:
        _ms_v29_round_rect(canvas, cx - 74 * s, cy + 64 * s, cx + 74 * s, cy + 94 * s, r=int(10 * s), fill='#c79262', outline='#8b5a3c'); canvas.create_text(cx, cy + 79 * s, text='📚 estudiando', font=self.app_font(max(8, int(10 * s)), 'bold'), fill='#4c2f20'); canvas.create_text(cx + 60 * s, cy + 35 * s, text='✏️', font=(self.app_font_name(), max(12, int(18 * s))))

def _ms_v29_draw_cat(self, canvas, pet=None, studying=False, preview_item=None):
    if canvas is None:
        return
    canvas.delete('all')
    if pet is None:
        pet = self.user_data.get('pet', {})
    c = self.palette(); w, h = _ms_v29_canvas_size(canvas, 230, 270); phase = int(getattr(self, '_pet_anim_phase', 0)); accessory = pet.get('accessory', 'Moño verde'); outfit = pet.get('outfit', 'Vestido fresa'); hood_color = pet.get('hood_color', 'Rojo fresa'); dress_color = pet.get('dress_color', 'Rojo fresa')
    if preview_item:
        slot = preview_item.get('slot')
        if slot == 'accessory':
            accessory = preview_item.get('name', accessory)
        elif slot == 'outfit':
            outfit = preview_item.get('name', outfit); dress_color = preview_item.get('dress_color', dress_color)
        elif slot == 'palette':
            hood_color = preview_item.get('hood_color', hood_color); dress_color = preview_item.get('dress_color', dress_color)
    bg1 = _ms_v29_mix(c.get('card', '#ffffff'), self.color_value(hood_color), 0.08); bg2 = _ms_v29_mix(c.get('card', '#ffffff'), self.color_value(dress_color), 0.12)
    for i in range(18):
        y1 = int(h * i / 18); y2 = int(h * (i + 1) / 18); canvas.create_rectangle(0, y1, w, y2, fill=_ms_v29_mix(bg1, bg2, i / 17), outline='')
    _ms_v29_draw_sparkles(canvas, w, h, c, phase); canvas.create_oval(w * 0.1, h * 0.72, w * 0.9, h * 0.98, fill=_ms_v29_mix(c.get('soft', '#f7f0ff'), '#ffffff', 0.2), outline=''); scale = min(w / 250, h / 285); self.v29_draw_vector_michi(canvas, w * 0.5, h * 0.47, scale, c, pet, studying, accessory, outfit, hood_color, dress_color); name = pet.get('name', 'Michi'); label = f'{name} · {outfit}'; acc_text = accessory if accessory != 'Ninguno' else 'sin accesorio'; _ms_v29_round_rect(canvas, 14, h - 48, w - 14, h - 26, r=10, fill='#ffffff', outline=c.get('secondary', '#ffd6e8')); canvas.create_text(w // 2, h - 37, text=label[:32], font=self.app_font(9, 'bold'), fill=c.get('text', '#302730')); _ms_v29_round_rect(canvas, 14, h - 23, w - 14, h - 4, r=9, fill=_ms_v29_mix(c.get('soft', '#f7f0ff'), '#ffffff', 0.25), outline='')
    canvas.create_text(w // 2, h - 14, text=acc_text[:28], font=self.app_font(8), fill=c.get('muted', '#6f6270'))

def _ms_v29_draw_window(canvas, x, y, w, h, c):
    _ms_v29_round_rect(canvas, x, y, x + w, y + h, r=12, fill='#bfe7ff', outline='#ffffff'); canvas.create_rectangle(x + 8, y + 8, x + w - 8, y + h - 8, fill='#9fd3ff', outline=''); canvas.create_oval(x + w - 50, y + 12, x + w - 24, y + 38, fill='#fff2a8', outline=''); canvas.create_polygon(x + 8, y + h - 8, x + 60, y + h - 58, x + 112, y + h - 8, fill='#85c6b2', outline=''); canvas.create_polygon(x + 70, y + h - 8, x + 145, y + h - 75, x + w - 8, y + h - 8, fill='#75bca8', outline=''); canvas.create_line(x + w / 2, y + 8, x + w / 2, y + h - 8, fill='white', width=3); canvas.create_line(x + 8, y + h / 2, x + w - 8, y + h / 2, fill='white', width=3)

def _ms_v29_draw_room_cat(self, canvas, mx, my, c, scale=0.72):
    pet = self.user_data.get('pet', {}); self.v29_draw_vector_michi(canvas, mx, my, scale, c, pet, studying=getattr(self, 'timer', None) is not None and self.timer.running and (self.timer.mode == 'study'), accessory=pet.get('accessory', 'Moño verde'), outfit=pet.get('outfit', 'Vestido fresa'), hood_color=pet.get('hood_color', 'Rojo fresa'), dress_color=pet.get('dress_color', 'Rojo fresa'))

def _ms_v29_update_room_michi(self, room, w, h):
    phase = int(getattr(self, '_pet_anim_phase', 0)); mx = float(room.get('michi_x', w * 0.52)); my = float(room.get('michi_y', h * 0.6)); tx = float(room.get('michi_target_x', w * 0.52)); ty = float(room.get('michi_target_y', h * 0.62)); selected = room.get('selected_object'); obj = room.get('objects', {}).get(selected) if selected else None
    if obj:
        tx = safe_int(obj.get('x', tx), tx) + 46 * math.sin(phase / 5.0); ty = safe_int(obj.get('y', ty), ty) - 50
    elif phase % 18 == 0:
        tx = random.randint(int(w * 0.34), int(w * 0.72)); ty = random.randint(int(h * 0.53), int(h * 0.76))
    mx += (tx - mx) * 0.12; my += (ty - my) * 0.12; mx = max(95, min(w - 95, mx)); my = max(int(h * 0.4), min(h - 86, my)); room['michi_x'], room['michi_y'] = (mx, my); room['michi_target_x'], room['michi_target_y'] = (tx, ty); return (int(mx), int(my))

def _ms_v29_draw_room(self):
    if not hasattr(self, 'room_canvas'):
        return
    self.v17_ensure_room_data(); c = self.palette(); room = self.user_data.setdefault('room', {}); canvas = self.room_canvas; canvas.delete('all'); w, h = _ms_v29_canvas_size(canvas, 720, 470); split = int(h * 0.58); wall = self.room_color(room.get('wall_color', 'Rosa suave')); floor = self.room_color(room.get('floor_color', 'Madera clara'))
    for i in range(24):
        y1 = int(split * i / 24); y2 = int(split * (i + 1) / 24); canvas.create_rectangle(0, y1, w, y2, fill=_ms_v29_mix(wall, '#ffffff', 0.1 + i * 0.01), outline='')
    for x in range(0, w, 54):
        canvas.create_rectangle(x, 0, x + 28, split, fill=_ms_v29_mix(wall, '#ffffff', 0.16), outline='')
    canvas.create_rectangle(0, split, w, h, fill=floor, outline='')
    for y in range(split + 12, h, 34):
        canvas.create_line(0, y, w, y, fill=_ms_v29_mix(floor, '#000000', 0.08), width=1)
    for x in range(-40, w, 96):
        canvas.create_line(x, split, x + 86, h, fill=_ms_v29_mix(floor, '#000000', 0.06), width=1)
    canvas.create_line(0, split, w, split, fill=_ms_v29_mix(c.get('secondary', '#ffd6e8'), '#000000', 0.08), width=5); _ms_v29_draw_window(canvas, int(w * 0.68), 38, int(w * 0.22), int(h * 0.23), c); _ms_v29_round_rect(canvas, 18, 28, 210, 94, r=18, fill='#ffffff', outline=c.get('secondary', '#ffd6e8')); canvas.create_text(114, 50, text='✨ Habitación de Michi', fill=c.get('primary', '#d85b8a'), font=self.app_font(11, 'bold')); canvas.create_text(114, 73, text=room.get('poster', 'Michi Studio'), fill=c.get('muted', '#6f6270'), font=self.app_font(10, 'bold'), width=165); last = None
    for i in range(11):
        x = int(w * (0.07 + i * 0.065)); y = int(102 + math.sin(i / 1.5) * 13)
        if last:
            canvas.create_line(last[0], last[1], x, y, fill=_ms_v29_mix(c.get('secondary', '#ffd6e8'), '#000000', 0.15), width=2)
        bulb = '#fff4a8' if (i + int(getattr(self, '_pet_anim_phase', 0))) % 2 else '#ffd1e8'; canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=bulb, outline='white'); last = (x, y)
    px, py = (int(w * 0.92), split - 4); canvas.create_rectangle(px - 18, py - 34, px + 18, py, fill='#d99a72', outline='#ad6f53'); canvas.create_oval(px - 48, py - 96, px - 8, py - 52, fill='#77bf8f', outline=''); canvas.create_oval(px + 8, py - 104, px + 48, py - 54, fill='#66b582', outline=''); canvas.create_oval(px - 22, py - 128, px + 22, py - 72, fill='#86c99a', outline=''); defaults = self.v25_room_default_positions(w, h) if hasattr(self, 'v25_room_default_positions') else {}; objects = room.setdefault('objects', {})
    for key, pos in defaults.items():
        if key in objects and (not objects[key].get('moved_by_user')):
            objects[key]['x'], objects[key]['y'] = pos
    drawers = _ms_v30_room_drawers()
    for key, obj in sorted(objects.items(), key=lambda kv: safe_int(kv[1].get('y', 0), 0)):
        default_x, default_y = defaults.get(key, (int(w * 0.42), int(h * 0.7))); x = max(78, min(w - 78, safe_int(obj.get('x', default_x), default_x))); y = max(100, min(h - 78, safe_int(obj.get('y', default_y), default_y))); obj['x'], obj['y'] = (x, y); selected = room.get('selected_object') == key
        if selected:
            canvas.create_oval(x - 92, y - 78, x + 92, y + 88, outline=c.get('primary', '#d85b8a'), width=3, fill=_ms_v29_mix(c.get('card', '#ffffff'), c.get('primary', '#d85b8a'), 0.05)); canvas.create_text(x, y - 84, text='seleccionado', font=self.app_font(8, 'bold'), fill=c.get('primary', '#d85b8a'))
        drawer = drawers.get(key)
        if drawer:
            drawer(self, canvas, x, y, c, selected)
        else:
            _ms_v29_round_rect(canvas, x - 48, y - 48, x + 48, y + 48, r=18, fill=c.get('soft', '#f7f0ff'), outline=c.get('secondary', '#ffd6e8')); canvas.create_text(x, y, text=obj.get('icon', '🪑'), font=(self.app_font_name(), 28))
        canvas.create_text(x, y + 75, text=obj.get('label', key)[:16], font=self.app_font(8, 'bold'), fill=c.get('text', '#302730'))
    mx, my = self.v29_update_room_michi(room, w, h); self.v29_draw_room_cat(canvas, mx, my, c, scale=min(0.7, max(0.54, w / 980)))
    if hasattr(self, 'room_status_label'):
        selected = room.get('selected_object') or 'ningún objeto'; self.room_status_label.config(text=f'Objeto seleccionado: {selected}\nMichi camina suavemente por la habitación y se acerca al mueble seleccionado. Usa las flechas para decorar.')

def _ms_v29_move_room_object(self, dx, dy, center=False):
    self.v17_ensure_room_data(); room = self.user_data.setdefault('room', {}); key = room.get('selected_object')
    if not key or key not in room.get('objects', {}):
        messagebox.showinfo('Habitación', 'Selecciona primero un objeto del cuarto.'); return
    canvas = getattr(self, 'room_canvas', None); w, h = _ms_v29_canvas_size(canvas, 720, 470) if canvas else (720, 470); obj = room['objects'][key]; step = 18 if abs(dx) + abs(dy) <= 12 else 24
    if center:
        obj['x'], obj['y'] = (int(w * 0.52), int(h * 0.74))
    else:
        obj['x'] = max(78, min(w - 78, safe_int(obj.get('x', w // 2), w // 2) + (step if dx > 0 else -step if dx < 0 else 0))); obj['y'] = max(100, min(h - 78, safe_int(obj.get('y', h // 2), h // 2) + (step if dy > 0 else -step if dy < 0 else 0)))
    obj['moved_by_user'] = True; room['michi_target_x'] = obj['x']; room['michi_target_y'] = obj['y'] - 50; self.save(); self.draw_room()

def _ms_v29_select_room_object(self, event):
    self.v17_ensure_room_data(); room = self.user_data.setdefault('room', {}); best = ''; bestd = 10 ** 9
    for key, obj in room.get('objects', {}).items():
        dx = safe_int(obj.get('x', 0), 0) - event.x; dy = safe_int(obj.get('y', 0), 0) - event.y; d = dx * dx + dy * dy
        if d < bestd and d <= 9200:
            best = key; bestd = d
    room['selected_object'] = best
    if best:
        obj = room['objects'][best]; room['michi_target_x'] = obj.get('x', event.x); room['michi_target_y'] = obj.get('y', event.y) - 50
    self.save(); self.draw_room()

def _ms_v29_animate_pet(self):
    if not self.user_data:
        return
    self._pet_anim_phase = int(getattr(self, '_pet_anim_phase', 0)) + 1; animations = self.user_data.get('settings', {}).get('animations', True)
    if animations:
        phrases = ['Tu michi cree en ti 🐾', 'Un pasito pequeño también cuenta ✨', 'Respira, ordena y sigue con calma 🍓', 'Tu habitación se ve cada vez más linda 🛋️', 'Modo foco: Michi te acompaña 📚']
        if getattr(self, 'pet_speech', None) is not None and self._pet_anim_phase % 6 == 0:
            try:
                self.pet_speech.config(text=random.choice(phrases))
            except Exception:
                pass
    try:
        self.refresh_pet()
    except Exception:
        pass
    if animations and hasattr(self, 'room_canvas'):
        try:
            self.draw_room()
        except Exception:
            pass
    delay = 650 if animations else 3200; self.pet_animation_id = self.root.after(delay, self.animate_pet)

def _ms_v31_format_clock(seconds):
    seconds = max(0, int(seconds)); minutes, secs = divmod(seconds, 60); return f'{minutes:02d}:{secs:02d}'

def _ms_v31_pomodoro_mode_name(mode):
    return {'study': 'Estudio', 'break': 'Descanso corto', 'long_break': 'Descanso largo'}.get(mode, 'Pomodoro')

def _ms_v31_update_pomodoro_progress(self):
    if not hasattr(self, 'pomo_progress_canvas'):
        return
    c = self.palette(); total = max(1, int(getattr(self.timer, 'total_seconds', self.timer.seconds_left or 1))); left = max(0, int(getattr(self.timer, 'seconds_left', 0))); elapsed = max(0, total - left); percent = max(0, min(100, round(elapsed / total * 100))); mode_name = _ms_v31_pomodoro_mode_name(getattr(self.timer, 'mode', 'study'))
    try:
        self.pomo_mode_value.config(text=mode_name, fg=c['primary'], bg=c['soft']); self.pomo_percent_value.config(text=f'{percent}%', fg=c['primary'], bg=c['soft']); self.pomo_elapsed_value.config(text=_ms_v31_format_clock(elapsed), fg=c['text'], bg=c['soft']); self.pomo_remaining_value.config(text=_ms_v31_format_clock(left), fg=c['text'], bg=c['soft']); canvas = self.pomo_progress_canvas; canvas.configure(bg=c['soft'], highlightbackground=c['secondary']); canvas.delete('all'); width = max(260, int(canvas.winfo_width() or 420)); height = 18; fill_width = max(10, int(width * percent / 100)) if percent else 0; _ms_v29_round_rect(canvas, 2, 2, width - 2, height - 2, r=8, fill=c['card'], outline=c['secondary'])
        if fill_width:
            _ms_v29_round_rect(canvas, 2, 2, min(width - 2, fill_width), height - 2, r=8, fill=c['primary'], outline=c['primary'])
    except Exception:
        pass

def _ms_v31_build_progress_stat(parent, title, bg, fg, value_font):
    box = tk.Frame(parent, bg=bg); box.pack(side='left', fill='x', expand=True, padx=4); tk.Label(box, text=title, bg=bg, fg=fg, font=value_font(8, 'bold')).pack(anchor='center'); value = tk.Label(box, text='--', bg=bg, fg=fg, font=value_font(12, 'bold')); value.pack(anchor='center', pady=(1, 0)); return value

def _ms_v31_add_pomodoro_progress_panel(self):
    if not hasattr(self, 'timer_label') or hasattr(self, 'pomo_progress_panel'):
        return
    c = self.palette(); pomo_body = self.timer_label.master.master; self.pomo_progress_panel = tk.Frame(pomo_body, bg=c['soft'], highlightbackground=c['secondary'], highlightthickness=1, padx=14, pady=12); self.pomo_progress_panel.pack(fill='x', pady=(8, 12)); top = tk.Frame(self.pomo_progress_panel, bg=c['soft']); top.pack(fill='x'); tk.Label(top, text='Avance del Pomodoro', bg=c['soft'], fg=c['text'], font=self.app_font(11, 'bold')).pack(side='left'); self.pomo_percent_value = tk.Label(top, text='0%', bg=c['soft'], fg=c['primary'], font=self.app_font(18, 'bold')); self.pomo_percent_value.pack(side='right'); self.pomo_progress_canvas = tk.Canvas(self.pomo_progress_panel, height=18, bg=c['soft'], highlightthickness=0, bd=0); self.pomo_progress_canvas.pack(fill='x', pady=(8, 10)); stats = tk.Frame(self.pomo_progress_panel, bg=c['soft'])
    stats.pack(fill='x'); self.pomo_mode_value = _ms_v31_build_progress_stat(stats, 'Modo actual', c['soft'], c['text'], self.app_font); self.pomo_elapsed_value = _ms_v31_build_progress_stat(stats, 'Transcurrido', c['soft'], c['text'], self.app_font); self.pomo_remaining_value = _ms_v31_build_progress_stat(stats, 'Restante', c['soft'], c['text'], self.app_font); self.pomo_progress_canvas.bind('<Configure>', lambda event: self.v31_update_pomodoro_progress()); self.v31_update_pomodoro_progress()

def _ms_v31_build_study_tab(self):
    _ms_v31_prev_build_study_tab(self); self.v31_add_pomodoro_progress_panel()

def _ms_v31_update_timer_label(self, seconds):
    _ms_v31_prev_update_timer_label(self, seconds); self.v31_update_pomodoro_progress()

def _ms_fix_get_subject_file_index(self):
    lb = getattr(self, 'subject_files_list', None)
    if lb is None:
        return None
    try:
        selected = lb.curselection()
        if selected:
            return int(selected[0])
        total = int(lb.size())
        if total <= 0:
            return None
        try:
            active = int(lb.index(tk.ACTIVE))
        except Exception:
            active = 0
        if active < 0 or active >= total:
            active = 0
        lb.selection_clear(0, tk.END); lb.selection_set(active); lb.activate(active); return active
    except Exception:
        return None

def _ms_fix_open_subject_file(self):
    subject = self.selected_subject()
    if not subject:
        messagebox.showerror('Archivo', 'Selecciona una materia.'); return
    files = self.subject_data(subject).get('files', [])
    if not files:
        messagebox.showerror('Archivo', 'Esta materia todavía no tiene archivos.'); return
    index = self._ms_fix_get_subject_file_index()
    if index is None or index >= len(files):
        messagebox.showerror('Archivo', 'Selecciona un archivo de la lista.'); return
    path = os.path.abspath(files[index])
    if self.validate_subject_file(path):
        self.open_path(path)

def _ms_fix_delete_subject_file(self):
    subject = self.selected_subject()
    if not subject:
        messagebox.showerror('Archivo', 'Selecciona una materia.'); return
    files = self.subject_data(subject).get('files', [])
    if not files:
        messagebox.showerror('Archivo', 'Esta materia todavía no tiene archivos.'); return
    index = self._ms_fix_get_subject_file_index()
    if index is None or index >= len(files):
        messagebox.showerror('Archivo', 'Selecciona un archivo de la lista.'); return
    del files[index]; self.save(); self.load_selected_subject(); messagebox.showinfo('Archivo', 'Archivo quitado de la materia.')

def _ms_fix_build_subjects_tab(self):
    _ms_fix_prev_build_subjects_tab(self); lb = getattr(self, 'subject_files_list', None)
    if lb is not None:
        try:
            lb.configure(exportselection=False); lb.bind('<Double-Button-1>', lambda event: self.open_subject_file())
        except Exception:
            pass

# Alias congelados de la cadena de parches original.
_ms_fix_prev_build_subjects_tab = _ms_v10_build_subjects_tab
_ms_old_build_main_ui = MichiStudioApp.build_main_ui
_ms_old_ensure_schema = MichiStudioApp.ensure_schema
_ms_old_load_selected_subject = MichiStudioApp.load_selected_subject
_ms_old_refresh_all = MichiStudioApp.refresh_all
_ms_v17_old_build_main_ui = _ms_v7_build_main_ui
_ms_v17_old_refresh_all = _ms_v7_refresh_all
_ms_v18_prev_refresh_achievements = _ms_v16_refresh_achievements
_ms_v20_old_build_main_ui = _ms_v17_build_main_ui
_ms_v20_old_refresh_achievements = _ms_v18_refresh_achievements
_ms_v21_prev_build_planner_tab = _ms_v15_build_planner_tab
_ms_v23_prev_build_home_tab = _ms_v24_build_home_tab
_ms_v24_prev_build_home_tab = _ms_v13_build_home_tab
_ms_v24_prev_build_study_tab = _ms_v3_build_study_tab
_ms_v24_prev_style_ttk = MichiStudioApp.style_ttk
_ms_v25_prev_build_main_ui = _ms_v20_build_main_ui
_ms_v25_prev_style_ttk = _ms_v24_style_ttk
_ms_v26_prev_practice_flashcards = _ms_v5_practice_flashcards
_ms_v27_prev_practice_flashcards_quiz = practice_flashcards_quiz
_ms_v28_prev_build_main_ui = _ms_v25_build_main_ui
_ms_v31_prev_build_study_tab = _ms_v24_build_study_tab
_ms_v31_prev_update_timer_label = MichiStudioApp.update_timer_label
_ms_v3_prev_ensure_schema = _ms_v2_ensure_schema
_ms_v3_prev_load_selected_subject = _ms_v2_load_selected_subject
_ms_v4_prev_build_main_ui = _ms_v2_build_main_ui
_ms_v4_prev_complete_task = MichiStudioApp.complete_task
_ms_v4_prev_ensure_schema = _ms_v3_ensure_schema
_ms_v4_prev_finish_timer = MichiStudioApp.finish_timer
_ms_v4_prev_save = MichiStudioApp.save
_ms_v4_prev_shop_items = MichiStudioApp.shop_items
_ms_v6_old_ensure_schema = _ms_v5_ensure_schema
_ms_v6_old_refresh_control_center = MichiStudioApp.refresh_control_center
_ms_v7_old_build_home_tab = MichiStudioApp.build_home_tab
_ms_v7_old_build_main_ui = _ms_v4_build_main_ui
_ms_v7_old_ensure_schema = _ms_v6_ensure_schema
_ms_v7_old_finish_timer = _ms_v4_finish_timer
_ms_v7_old_refresh_all = _ms_v2_refresh_all
_ms_v8_old_build_home_tab = _ms_v7_build_home_tab
_ms_v8_old_ensure_schema = _ms_v7_ensure_schema
_ms_v8_old_refresh_control_center = _ms_v6_refresh_control_center
_ms_v8_old_shop_items = _ms_v4_shop_items
_ms_v8_old_use_inventory_item = MichiStudioApp.use_inventory_item

# Asignacion final de metodos conservada.
MichiStudioApp._ms_fix_get_subject_file_index = _ms_fix_get_subject_file_index
MichiStudioApp._planner_visible_to_index = _ms_v6_planner_visible_to_index
MichiStudioApp.achievement_rules = achievement_rules
MichiStudioApp.add_arcade_extra_panel = add_arcade_extra_panel_v3
MichiStudioApp.add_flashcard = _ms_v5_add_flashcard
MichiStudioApp.add_flashcard_category = add_flashcard_category
MichiStudioApp.add_planner_event = _ms_v6_add_planner_event
MichiStudioApp.animate_pet = _ms_v29_animate_pet
MichiStudioApp.anki_review_today = _ms_v8_anki_review_today
MichiStudioApp.apply_anki_rating = _ms_v8_apply_anki_rating
MichiStudioApp.apply_app_font = _ms_v21_apply_app_font
MichiStudioApp.apply_theme_variant = _ms_v21_apply_theme_variant
MichiStudioApp.auto_flashcards_from_notes = _ms_v5_auto_flashcards_from_notes
MichiStudioApp.auto_week_plan = _ms_v7_auto_week_plan
MichiStudioApp.build_achievements_tab = _ms_v16_build_achievements_tab
MichiStudioApp.build_home_tab = _ms_v23_build_home_tab
MichiStudioApp.build_library_tab = _ms_v9_build_library_tab
MichiStudioApp.build_main_ui = _ms_v28_build_main_ui
MichiStudioApp.build_planner_tab = _ms_v21_build_planner_tab
MichiStudioApp.build_room_tab = _ms_v17_build_room_tab
MichiStudioApp.build_settings_tab = _ms_v21_build_settings_tab
MichiStudioApp.build_shop_tab = _ms_v18_build_shop_tab
MichiStudioApp.build_study_tab = _ms_v31_build_study_tab
MichiStudioApp.build_subjects_tab = _ms_fix_build_subjects_tab
MichiStudioApp.bulk_add_flashcards = bulk_add_flashcards
MichiStudioApp.buy_shop_item = _ms_v12_buy_shop_item
MichiStudioApp.change_calendar_month = _ms_v6_change_calendar_month
MichiStudioApp.change_week = _ms_v7_change_week
MichiStudioApp.choose_bg_color = _ms_v21_choose_bg_color
MichiStudioApp.choose_primary_color = _ms_v21_choose_primary_color
MichiStudioApp.claim_mission = _ms_v4_claim_mission
MichiStudioApp.complete_planner_event = _ms_v6_complete_planner_event
MichiStudioApp.complete_task = _ms_v4_complete_task
MichiStudioApp.create_flashcards_from_notes = _ms_v8_create_flashcards_from_notes
MichiStudioApp.create_pomodoro_from_selected_event = _ms_v7_create_pomodoro_from_selected_event
MichiStudioApp.dashboard_summary = _ms_v8_dashboard_summary
MichiStudioApp.delete_flashcard = _ms_v5_delete_flashcard
MichiStudioApp.delete_planner_event = _ms_v6_delete_planner_event
MichiStudioApp.delete_subject_file = _ms_fix_delete_subject_file
MichiStudioApp.draw_cat = _ms_v29_draw_cat
MichiStudioApp.draw_mood_calendar = _ms_v7_draw_mood_calendar
MichiStudioApp.draw_mood_chart = _ms_v12_draw_mood_chart
MichiStudioApp.draw_room = _ms_v29_draw_room
MichiStudioApp.due_cards = _ms_v8_due_cards
MichiStudioApp.duplicate_selected_event_weekly = _ms_v8_duplicate_selected_event_weekly
MichiStudioApp.edit_flashcard = _ms_v5_edit_flashcard
MichiStudioApp.ensure_schema = _ms_v8_ensure_schema
MichiStudioApp.event_to_task = _ms_v8_event_to_task
MichiStudioApp.events_for_day = _ms_v6_events_for_day
MichiStudioApp.finish_timer = _ms_v8_finish_timer
MichiStudioApp.flashcard_exam_mode = _ms_v7_flashcard_exam_mode
MichiStudioApp.flashcard_write_mode = _ms_v8_flashcard_write_mode
MichiStudioApp.generate_mood_study_plan = _ms_v7_generate_mood_study_plan
MichiStudioApp.get_current_subject_cards = _ms_v7_get_current_subject_cards
MichiStudioApp.get_daily_missions = _ms_v4_missions
MichiStudioApp.go_calendar_today = _ms_v6_go_calendar_today
MichiStudioApp.go_week_today = _ms_v7_go_week_today
MichiStudioApp.load_selected_subject = _ms_v5_load_selected_subject
MichiStudioApp.month_start = _ms_v6_month_start
MichiStudioApp.mood_productivity_summary = _ms_v7_mood_productivity_summary
MichiStudioApp.move_room_object = _ms_v29_move_room_object
MichiStudioApp.move_selected_event_days = _ms_v8_move_selected_event_days
MichiStudioApp.open_backup_manager = _ms_v4_backup_manager
MichiStudioApp.open_bubble_pop_game = open_bubble_pop_game
MichiStudioApp.open_catch_game = open_catch_game
MichiStudioApp.open_daily_missions_window = _ms_v4_open_missions
MichiStudioApp.open_global_search = _ms_v7_open_global_search
MichiStudioApp.open_mood_calendar = _ms_v7_open_mood_calendar
MichiStudioApp.open_pro_dashboard = _ms_v4_pro_dashboard
MichiStudioApp.open_runner_game = _ms_v4_runner
MichiStudioApp.open_skater_game = open_skater_game
MichiStudioApp.open_subject_file = _ms_fix_open_subject_file
MichiStudioApp.open_today_overview = _ms_v8_open_today_overview
MichiStudioApp.practice_flashcards = _ms_v26_practice_flashcards
MichiStudioApp.practice_flashcards_quiz = _ms_v27_practice_flashcards_quiz
MichiStudioApp.preview_inventory_item = _ms_v18_preview_inventory_item
MichiStudioApp.preview_shop_item = _ms_v14_preview_shop_item
MichiStudioApp.randomize_room = _ms_v17_randomize_room
MichiStudioApp.refresh_achievements = _ms_v22_refresh_achievements
MichiStudioApp.refresh_all = _ms_v17_refresh_all
MichiStudioApp.refresh_control_center = _ms_v8_refresh_control_center
MichiStudioApp.refresh_game_status = refresh_game_status_v3
MichiStudioApp.refresh_inventory = _ms_v18_refresh_inventory
MichiStudioApp.refresh_inventory_cards = _ms_v18_refresh_inventory_cards
MichiStudioApp.refresh_moods = _ms_v13_refresh_moods
MichiStudioApp.refresh_planner_events = _ms_v6_refresh_planner_events
MichiStudioApp.refresh_shop = _ms_v18_refresh_shop
MichiStudioApp.refresh_shop_cards = _ms_v18_refresh_shop_cards
MichiStudioApp.render_calendar_month = _ms_v20_render_calendar_month
MichiStudioApp.render_week_view = _ms_v15_render_week_view
MichiStudioApp.room_color = _ms_v7_room_color
MichiStudioApp.save = _ms_v4_save
MichiStudioApp.save_mood = _ms_v6_save_mood
MichiStudioApp.save_room = _ms_v17_save_room
MichiStudioApp.select_room_object = _ms_v29_select_room_object
MichiStudioApp.selected_event_index = _ms_v8_selected_event_index
MichiStudioApp.set_selected_date = _ms_v6_set_selected_date
MichiStudioApp.set_shop_selection = _ms_v12_set_shop_selection
MichiStudioApp.shop_items = _ms_v8_shop_items
MichiStudioApp.smart_next_action = _ms_v8_smart_next_action
MichiStudioApp.start_focus_from_dashboard = _ms_v8_start_focus_from_dashboard
MichiStudioApp.study_weak_flashcards = _ms_v7_study_weak_flashcards
MichiStudioApp.style_ttk = _ms_v25_style_ttk
MichiStudioApp.task_to_planner_window = _ms_v7_task_to_planner_window
MichiStudioApp.toggle_dark_mode = _ms_v21_toggle_dark_mode
MichiStudioApp.update_arcade_best = update_arcade_best
MichiStudioApp.update_mission_progress = _ms_v4_update_mission
MichiStudioApp.update_timer_label = _ms_v31_update_timer_label
MichiStudioApp.use_inventory_item = _ms_v8_use_inventory_item
MichiStudioApp.v12_center_cat_canvas = _ms_v12_center_cat_canvas
MichiStudioApp.v13_make_scroll_area = _ms_v19_make_scroll_area
MichiStudioApp.v16_next_goal_text = _ms_v16_next_goal_text
MichiStudioApp.v17_ensure_room_data = _ms_v17_ensure_room_data
MichiStudioApp.v18_filter_shop_items = _ms_v18_filter_shop_items
MichiStudioApp.v18_motivation_text = _ms_v18_motivation_text
MichiStudioApp.v18_set_inventory_selection = _ms_v18_set_inventory_selection
MichiStudioApp.v20_apply_theme_to_widgets = _ms_v24_apply_theme_to_widgets
MichiStudioApp.v21_rebuild_keep_tab = _ms_v21_rebuild_keep_tab
MichiStudioApp.v21_style_planner_fonts = _ms_v21_style_planner_fonts
MichiStudioApp.v22_draw_michi_in_room = _ms_v22_draw_michi_in_room
MichiStudioApp.v23_fix_mood_tracker = _ms_v23_fix_mood_tracker
MichiStudioApp.v25_room_default_positions = _ms_v25_room_default_positions
MichiStudioApp.v26_draw_shop_michi_in_room = _ms_v28_draw_shop_michi_in_room
MichiStudioApp.v26_style_flashcard_window = _ms_v26_style_flashcard_window
MichiStudioApp.v27_open_flash_quiz_subject_picker = _ms_v27_open_flash_quiz_subject_picker
MichiStudioApp.v27_select_subject_for_flash_quiz = _ms_v27_select_subject_for_flash_quiz
MichiStudioApp.v28_get_transparent_michi_photo = _ms_v28_get_transparent_michi_photo
MichiStudioApp.v29_draw_room_cat = _ms_v29_draw_room_cat
MichiStudioApp.v29_draw_vector_michi = _ms_v29_draw_vector_michi
MichiStudioApp.v29_update_room_michi = _ms_v29_update_room_michi
MichiStudioApp.v31_add_pomodoro_progress_panel = _ms_v31_add_pomodoro_progress_panel
MichiStudioApp.v31_update_pomodoro_progress = _ms_v31_update_pomodoro_progress
MichiStudioApp.v9_button = _ms_v21_button
MichiStudioApp.v9_scrollbox = _ms_v10_scrollbox
MichiStudioApp.v9_style_buttons_deep = _ms_v9_style_buttons_deep
MichiStudioApp.v9_textbox = _ms_v10_textbox
MichiStudioApp.week_start = _ms_v7_week_start


# --- Fix flashcards: conserva selección de materia al editar/eliminar ---
# Tkinter comparte la selección entre Listbox por defecto. Al seleccionar una
# flashcard, podía perderse la materia activa y por eso Editar/Eliminar no
# encontraba qué tarjeta modificar. Este parche solo estabiliza esa selección.
_ms_flash_fix_prev_build_subjects_tab = MichiStudioApp.build_subjects_tab
_ms_flash_fix_prev_load_selected_subject = MichiStudioApp.load_selected_subject


def _ms_flash_fix_select_subject(self, subject):
    if not subject:
        return
    try:
        self._last_flash_subject = subject
        order = getattr(self, '_subject_order', [])
        if subject in order and hasattr(self, 'subject_list'):
            index = order.index(subject)
            self.subject_list.selection_clear(0, tk.END)
            self.subject_list.selection_set(index)
            self.subject_list.activate(index)
            self.subject_list.see(index)
    except Exception:
        pass


def _ms_flash_fix_current_subject(self):
    subject = None
    try:
        subject = self.selected_subject()
    except Exception:
        subject = None
    if subject:
        self._last_flash_subject = subject
        return subject
    subject = getattr(self, '_last_flash_subject', None)
    if subject and subject in self.user_data.get('subjects', {}):
        return subject
    return None


def _ms_flash_fix_selected_index(self, cards):
    try:
        sel = self.flash_list.curselection()
    except Exception:
        return None
    if not sel:
        return None
    visible_index = int(sel[0])
    index_map = getattr(self, '_flash_index_map', None)
    if index_map is not None and visible_index < len(index_map):
        real_index = int(index_map[visible_index])
    else:
        real_index = visible_index
    if real_index < 0 or real_index >= len(cards):
        return None
    return real_index


def _ms_flash_fix_build_subjects_tab(self):
    _ms_flash_fix_prev_build_subjects_tab(self)
    for attr in ('subject_list', 'flash_list'):
        widget = getattr(self, attr, None)
        if widget is not None:
            try:
                widget.configure(exportselection=False)
            except Exception:
                pass


def _ms_flash_fix_load_selected_subject(self):
    subject = None
    try:
        subject = self.selected_subject()
    except Exception:
        subject = None
    if subject:
        self._last_flash_subject = subject
    _ms_flash_fix_prev_load_selected_subject(self)
    try:
        subject = self.selected_subject()
        if subject:
            self._last_flash_subject = subject
    except Exception:
        pass


def _ms_flash_fix_delete_flashcard(self):
    subject = _ms_flash_fix_current_subject(self)
    if not subject:
        messagebox.showerror('Flashcards', 'Selecciona una materia.')
        return
    cards = self.subject_data(subject).get('flashcards', [])
    index = _ms_flash_fix_selected_index(self, cards)
    if index is None:
        messagebox.showerror('Flashcards', 'Selecciona una flashcard.')
        return
    del cards[index]
    self.save()
    _ms_flash_fix_select_subject(self, subject)
    self.load_selected_subject()


def _ms_flash_fix_edit_flashcard(self):
    subject = _ms_flash_fix_current_subject(self)
    if not subject:
        messagebox.showerror('Flashcards', 'Selecciona una materia.')
        return
    cards = self.subject_data(subject).get('flashcards', [])
    index = _ms_flash_fix_selected_index(self, cards)
    if index is None:
        messagebox.showerror('Flashcards', 'Selecciona una flashcard.')
        return
    card = cards[index]
    c = self.palette()
    win = tk.Toplevel(self.root)
    win.title('Editar flashcard')
    win.geometry('470x410')
    win.configure(bg=c['bg'])
    tk.Label(win, text='Editar flashcard', bg=c['bg'], fg=c['primary'], font=('Arial', 15, 'bold')).pack(pady=10)
    q = tk.Text(win, height=4, wrap='word')
    q.pack(fill='x', padx=18, pady=4)
    q.insert('1.0', card.get('q', ''))
    a = tk.Text(win, height=5, wrap='word')
    a.pack(fill='x', padx=18, pady=4)
    a.insert('1.0', card.get('a', ''))
    meta = tk.Frame(win, bg=c['bg'])
    meta.pack(fill='x', padx=18, pady=4)
    difficulty = tk.StringVar(value=card.get('difficulty', 'Normal'))
    ttk.Combobox(meta, textvariable=difficulty, values=['Fácil', 'Normal', 'Difícil'], state='readonly', width=10).pack(side='left')
    favorite = tk.BooleanVar(value=bool(card.get('favorite')))
    tk.Checkbutton(meta, text='Favorita', variable=favorite, bg=c['bg'], fg=c['text']).pack(side='left', padx=10)
    tags = tk.Entry(win)
    tags.pack(fill='x', padx=18, pady=4)
    tags.insert(0, card.get('tags', card.get('category', '')))

    def save_edit():
        nq = q.get('1.0', tk.END).strip()
        na = a.get('1.0', tk.END).strip()
        if not nq or not na:
            messagebox.showerror('Flashcards', 'Pregunta y respuesta no pueden quedar vacías.')
            return
        tag_value = tags.get().strip()
        card.update({
            'q': nq,
            'a': na,
            'difficulty': difficulty.get(),
            'favorite': favorite.get(),
            'tags': tag_value,
            'category': tag_value.split(',')[0] or 'General',
        })
        self.save()
        _ms_flash_fix_select_subject(self, subject)
        self.load_selected_subject()
        win.destroy()

    tk.Button(win, text='Guardar cambios', command=save_edit, bg=c['accent']).pack(fill='x', padx=18, pady=10)


MichiStudioApp.build_subjects_tab = _ms_flash_fix_build_subjects_tab
MichiStudioApp.load_selected_subject = _ms_flash_fix_load_selected_subject
MichiStudioApp.delete_flashcard = _ms_flash_fix_delete_flashcard
MichiStudioApp.edit_flashcard = _ms_flash_fix_edit_flashcard

__all__ = [name for name in globals() if not name.startswith('__')]

def run() -> None:
    root = tk.Tk()
    app = MichiStudioApp(root)
    root.protocol('WM_DELETE_WINDOW', app.on_close)
    root.mainloop()

if __name__ == '__main__':
    run()
