from lzma import decompress as lzma
from base64 import b85decode
from hashlib import sha256

WORDS = '{Wp48S^xk9=GL@E0stWa761SMbT8$j;4?ZDJzW4Wn21WR2~SN+PtI?bJR*YqdhorTGI^h5s6rBe;k9*`P;vADxW!uq6ud9G`Ryq|uIakUrKX0S{>^H;DHJAH%e&gKef~1EXSD0Us}VywB$hQSCL24wlCsKYCV<&UARZHOh)&>5DZ-~ie;w#}??6<JOl|mq9eKdcew;FDEcSIuPSsz9ifo`zRLj%vg=z0~cu*vAMA6cb5GSaXO7n>$%xTl&8@gxbgANqLq@*=qXFu|h=a2+%Xss$^84V29ubWU|Jis}ZeS^SfW}jww7nw9K&Cx%HKy;0Y37#)`+p3zY1bZ`7k+YIMR3u^uY^9ccN{kp=S?u6N4zisDC8gkIJo$^^m6wM^a$8H3bAYEsAIc966#xe{9j&hY0zxEiT${N!QqS^qX$el?jg>&rnPf$K-yrI;)DRZN%5N67_SO#n=yj@!>$4Hz)evAV5=sYEQS$z7tp@GUj@>>S;S=L=!OK{Jtif0|-p%w0w#bxt71|pkbpS}&H*pv#^=Et7p$ITGaVb29^yoJQ!zsLIcy9`T(hCW;CliZjzHlUHk5C~^7<s${pyjkGSHqDb$3%6Ql)O^B*BWTyC_6sP9t*>_nJ1EUY6*S-;1uIhueo7A2kS$(TLIuv1k&86r%i)z0*-`orY@!pD9im@rths?CuQ90QmSY+!iP@8%nQ%d2Mnv#BVLo#w-6V9c5aG@e2d9O-C!?y>GSCUs5I^54+iV}u#dj~6%nU^oJ!C{P_)~vNh$*wcdG_&J;l!^sRRdSF->(8X?IogT__SWD7&M;TnqE9)DN*23c>sJsQxXi3;5J6DDh(_H0P%C?nxktxwmY48g%V-yV%hhv^I6Ce>JHekwn>p4V#Z$&Ak`?YynWXHvXe4%xMD2|MsU5L07yJy6e|vp2IG$#02=$PkL?tnJ&J=E0pa~T(Ag^Qd$%#w%Z}inkIDF?yP?}ND>5PXW-?f2wPyub80I{iUrK*T$y3+?Z3}t{-lQ>+q#(>{}#Py8)eUlp>%)ax@@X>T34OE*QR@P8VU6Whw3T`*ySMV3$(e<DkR+2{_N=?S;7lEoDJ`L?gU`UD_5c2amltdmwkn;Lf(DpTBgUnHyDhbM}(Y$j7FBrmu@C=SzP!FkI<hw8@L*uC{<!jRN_(J!JjCao+d{L3qb1SSpJ&g79V6q!wq8$|Lgzb%f)+Rd=Z<$W?vc^)FxemKJWR&WkLBADTw58*Jjf@laMHzDxvlb!PV@^h$+zc_<Nyss-9hTh~rWSZ^^ap88bYrg%*q5Zo<ir@EJuN7EUQ@ZlqaB?g}!wB_inxX~1e+^EmmKV*wlQGQY|>^?=EI&**lc0Sqkbc|J6Rfyp>V@W8P|qGp9S3a^^i(Kb%wuV+#yUw7sTmZf{kMQ!sa{POY6vK*s2Ifb^`hU88|DWtm%pHoC{3F=fToD=V6$RjTAJ0%4P2fzYnDmPE)$I;u3jH4EH2Ik*cOe!^maMvpwssA}~x*iB23hCQR$N&$tk;ZY9aB)mrWBth~*;Fu()hDgfVor-@K~yK<uP-*ZRzTT&B!OSH$yuDq{9@jFT)C9hO%w>yX>BjQjmMr19@;?+RM>2?b_KQyE?-Rntt@O+F_{sZZMA_fsn4Na*-4S%NfF3?WwG0NlKJ@jw>URPHg5Ii1kgg}^XmQ}XCQS#Z`$d~PeWBFEhK`rZre}~_PLj_x{M4kJZx0I#-x_@VOgT2l%#VaQD&G?J{Yx{+@F4MXSkX9NH8*ST449{IG|uWEjRL>aT9OZHyNDkc!{3%ghToSL;PKG))`o_sRm}J#K4hz8ABeyW@iUw>!70%#kAAlI13)TP2SLCL%UWvM|PRiZvL*jiLT@K>yZ|`iq<S+w&<KfVx{eK7R-u}RTrIY<yi;J$*o{X<EQ#?d+)3|kuUjb=(RzIg>5Q{|GygX8XQa)o!}ov`f}D^*VAX3BD;;Z#HfHae-{3@3L)RY#P`TGsOD-1tWnN5Z7T{(!RpXo<M=tNFdt^?xV`&I)!9D+g;*{3tRc8i+nI%cs16RUuplemu$Nh%JbYaIw|C3vtG@H|#KYDCUh}?*2-Z?X!#v>SVJxkCP|39*4r`$l_OnSDn0=U}M0~Gv|HJV+VCRs7o<02%hdr{NoA%pqQH&6&M;x66w_QU?TX;OFAHj6Y0i#nCG3e9HG)mcz0nkrq9Y`tHX{8F7c930q*(g&w1`cZ4xBY?t$Qmvo?dG0?PECfDDAz|jPv@+Ho%exJ{nB4SYDW|7gCx9TZ4BV$wh)x#{qG{i(T^sMhTsXb^iJYOYijChaYKebZm3}hBei>J+V-&u2K{QOkCzNc!oS94t{zpR46i;P3aWLqSIzGsu}Vx^{QE;#k>=C_h2y%|F8^r%&S3819ET!K{HUwp4}@lzh<6ojDEF7hX0jG+^Zi+cWXhq=Dc<!e^7tag*h_w>8Td;TIu4-PV8?*6nhT~N%h|XsIB`r`i^_r@)k<W8v*3bS=i$N<0GE(~orOuOQgM9^WmKC=9|lDt1atEYSS0rGF1B~P{X{?aw)-Vcv7MQK+9g~uS+1PIAO9!{r`B7L9b!20&tlP+@JD^HV0{jGk9Z~r-f0@?GvfdPB~K3+xgQz99RPE0$ypmfLpQPcBc#H1lE%0IVanKt;%G@37HzxN<45L(HjJlzLtCI*D8tymZtt%*bGL6nuCKYi(>+Z2GDz*c#fx?;FKze->oU++H|?$dWEyvH(slLR9kNJ@7#fJoM~3GnZN%U_gwM(<e5k+kR^gj)2uh!*r3{Lz$HF{JV9=cVebNzPz&Xu5C8ktkNNV$WM<ZpkUQQ5SSV2B(PG-m7*utJ4k(x1s6QjdVPR&*UPR6@wws0~9hNrN99lTA&@aNHX0i7-8n<owGD3hymGsz>{A;qdr&c*UQf0wX*aNNKug~E&3F(g~s`!z>*if=)t8(ez<O4~`rq+>_)<W0{b309TjMf`9lyfs1S{SMGi8=5h9ajYOF%oNg^S^u6%Z9{h^HtE4lNKawe9Ag~ZrVfCQT$OYsbdh8V4gi_veh$k#(Oy$C`6DZoWM{<o6)Zkc#w^V7No*D7u&H4=vsdM&+Wj@omEqlsOpWvHCb(viuC+jIQ~25)TZaZO{Ls!Lg=dfkHU5FMaT$_8HptjqxWV(5O7KPOCz>v3Wh5yhz0E#M6OtM>$=`O6DU)3eOQE%@DvS|R?UNiWcMd)IB7Hk=LUY8|qSFaR-}hVxXXtSGZH0qMqb4Zbnh*C6r+wb`Xp*BANpSEHOUb<VLY7OQep$#5Y(s*%S@=$&Ko$7IiYJBNA}BtDyL0~sb&JRk7Tc;=$n4Azead{|z&)=6N~JdTgtJOk@>{|S1(zof0g;P4g{f7C$-x9CV|T^@$;QH5XWxu(c#f|ou_cREl0iH6;3;*S1mMxBAEE@9u*lIoXhO2d=ZB#`iqotoy{DU&5dg<qZ2c?2tQ@bN8U6SzLEyDE^{dtc+iId2?bmL&Ea(JxLKh&07Mod4lYd|09mb!H3J{5T#i|i?B9b0^Box3YOw-!o-)-kDE?o7<sZkF>9EkAf%J7B^QSni3%w|BuGff>}Eaw%SlPpm!cc)#%`gFqj)-4FGdGlr(!(r4*r-e~Mi&OgtpQ|erk6`i{DygqTjDe2Z!6~8DR4AjC-$fzHbgjm7gzCju)_@%=MXWWWQDl_eE@H+i*Ad|mI4UIa;j29BqwPI(z`P;m50;Fj=TL)2Nc)2tuVGYxIh3nSVMGY1!6R}yfd^b`9v|S6PY`^Fx=}CayHMrli=C^TT3RvK|Ee*<MW59q6O;Yz)Mam_)ic7jo)YXD=NPK(op9l|6I$`UPgcslivyu%1|G`iViiM)gI7*I+>JBhIA76%mxEH;M|j#>PS0X>@9+3?OAYMVeBx?+H<NbZR`Go5#$5JSFni?x)Nu;rsZ@zNKyT(cWXT%B+E-PM<t|t3O|TCfD$U^9{h93!ZITftBfvVapQP9%;!Gm(7MrL7$PdDDlnTv{pdQiH+mbfD$&wW@#?1|NN~^1+?Gb1V06AE9%8)o2a8t4V#JCvURwu%?o4i_jo~H)ENC+~=?qDGmpd6lUs1I9F8rpLM<{6PB2v((4vDXf_v#4t(JpcL*LM-6j6@Q`5fyAY7in+WmJ!_kYe&!xGXNslNf$oB%^%dfsp9_=R38REKBN~m_MiG^qK=o4RIWIm69on`>x-U2JdRN`9O>-45xh{D`eZWc6TS#SdXC=K-@P;X(G443jia|wfazi(kNVgqIvrFsEAYu;bV~acCToj7<i0#a)@3G%`)h=7nm9ypN^8RW7%kz9LrS@1aWiq4Ro5BW&B%mM-xD9T=A`Q$%e$@Al^!<!3LPiYI`^U9-7%ag+nT^&R)>Q)vAhI_;mNDvhPN6Y*kP7rN(b)#p>95k9`}#$87JPeA>GRxC-!4B^1gUUKsgKp0RM7_|j}~$I-whj;&I?FLr4y%axwo;NB53@Zg&Y86@L?kX+LjcJ?l_F;fwgOY;K*Pby?+#~k#J)t06N2ELBS8n7yAi5EAB<=Xy9u56MlUs)0k!5!yH)7(Y7cbk^XuL?CYVrfj67I#NPlx!WT5ib9*G9jx~`LIN1&X=#r>W<t$U{3aEqOYM7hpD@e(m9g_<t$3nMYI;mb9)$ORRZq{SjD8&MK5@hDMk%gk&4Ls)`dXO-0HBjpWSxXI0#4oF-Q#51`uOtm#E5>yGye2<KwIF34z;pbNsdVeq&EoSqU>qO~lq*oNowmIl@TZphv!Av?D}vn%zkTb^+J*jvMK5h=lB;1Vq5>iOTI8RZ<060!)n=`kudD^(yBB!-c4Vz6wYUIooxdSt(avBUGe!d!I7(Y4@DF-5OEeR+J1B^X{u4`!KPV&<l^ZshB>}*_w~@3yM^0o5<hxqcy=w?wDnK}WE+xsuq|aIepUnf839KIX05P&awGy24iFHl=Mn|HI$n?dA;}Uq?x>KeuVm+srUmw2HW}QaF=A};fMK{lB;5_dK_%z!`k;z4RcGH7P2``t*DKt_Kl*15s6v%at5Go;|aM+v2$S>n64fC0dRyZZOzox4^Zt<dFKj*aNw@$ecKsR2cN#Kz3B4Y&;G5zZiQ|^C8z7R(;DYOeMbP8(ZlqjSy!a(AC)K#n<IHZrmd*i=Wf)nOC0;m^tq}f#?91)BSVTk+g5nEE?(*Ge$-5_nhoc-?&X2$ZBtuI}~)PDEMQa2IEt@z><1x4m)YL|B&+n10%o+Pf6d8gR>S`hj!v-l;*q@=7pNsvt;$WU2=9!AlK*}`obi!7iodC(0-E{r3aUupc2BN!ohsPLwY05C9;M|aA5o$22z!Bb*$RHRHzLxLphMt-W(ww)r4kdG?Sc<PL0buSTTFvNxPXVHn^Qaq9*h*hb6L?eerq&WQ#rVou1$otE5$=#u!%&Pd)fJ3j+B9dG$H9rYat{Ox69OkmNrTad~8%kiq<$~?_UETmJn>J<xB8uco5+yNo3HSXsTy<z<G>oe3i{BcGb+Mu5O0}QTSK+GZ@<)wzy5ai|FGVJMrtd_5Qlfb_Zb3%R(o|`b5*Hc@uS|#2WQl}IaA$|0-UP#^VQliQXjAAnhBvliHGn-ens;mPXB?+8=q`HBZMX&2GUj1Khpi(3hCF422`mp%)Z0%KS6B=F)d|2Vy8_`%O9QH2!3wB|yX7QToWHz8@Y!~erQnXNpw(eIbb@uZ5>S?FqSfze*_mV&V7i<J=fAGF@jz%0&=Qs-E2lGjPWxSFg{X|X74YVheUsapRtLvGTz#`!*O*cYS}d0TN`ry0o6nradODKE#Rk`I+p5*{WTrpb!%^I}fc24(TU^5+I|;O@V;=gtiybnlso8>}5Q~AD?9kmIcoFX&ukbQLX(%5%x01G2>86MMwxhjDmTr_sU$L$@9PD&uxTyHCDjg(~8?A7FIS#pg)2{19J@EBKvoeySHpvSPg#*6)x2Hs5?BJMiv$%Pe!q%JVgYe!?{mzF<AWpKoxzP9hWilb(L9;f0nu8Qcj(s}o;ZHrij{u2P=XSRSD9U<yJz~lEn*Yh0tkai<8<m8WHy0>WcVmm7msax_X&XrXSVoCl7Pg>4j_rI(e*Qp8(!S?1*<&YxCQ)!^*s#?N-VcMLi2W9P<yqId#-cAON&S9SG1RS9gb*Mez{c|rtaF<8K+DCezjYvL7tM*b_s*@~6ziuX-!234T4fQJZ%#F6N|vjt5;~Vg%b`IXJpeBMyIX`c?m(o?AEX_3He$m~<8w|s+^H<2X(&Z@#ht7r_TMxdlixh6;l!UPGq#QtL>P`axbRIk!0S&8<#iX|L3B}nZr+RdhiN2EU({8zE~}eWBxr%re>sIH_A0eCAs@w)R#3T2h6V1(&YhmGGyeC<=ZD51@sPQrLJ`nomo7}LR6MdX&5>I?;J8w0P@A1MSyzLfjP%7*jg-7#kkJaauM|rtVA;7(@H?{|F4yO<qoL)h-&NyquidVU{xTaSi=}x!k|>PTkw2;eT3Eyl{4N_F5jE-)K>RWv(sze?YF5lME7{soSgy`vsDp&Ljb(zoNs22ToTr4v;^roynvlDQB9@F|>{Bi{f)QdZ!{o1*S7w@Y86vccBiGORXd-~loPl39Q^{`Mp*PJciu&|&+Dzoygpt-92j+M_00000#McWaKKD+@00G%3yJi3Y_JjO^vBYQl0ssI200dcD'
words = lzma(b85decode(WORDS.encode()))
assert sha256(words).hexdigest() == 'f18b9a84c83e38e98eceb0102b275e26438af83ab08f080cdb780a2caa9f3a6d'
words = words.decode().split(' ')

polyseed_lang_en = {
    'name': 'English',
    'name_en': 'English',
    'separator': ' ',
    'is_sorted': True,
    'has_prefix': True,
    'has_accents': False,
    'compose': False,
    'words': words
}
