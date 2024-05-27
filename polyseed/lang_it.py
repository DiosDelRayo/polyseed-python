from lzma import decompress as lzma
from base64 import b85decode
from hashlib import sha256
from typing import List
from .lang import Language

WORDS = '{Wp48S^xk9=GL@E0stWa761SMbT8$j;69%i5M2N;n21TUB<Rr>MK&_-Mi3R$yV#~PS$4g|kFRdDj+&`pqK|<l^}a}7I)ui&lcE}=4f%Iy^jy1dvmRIy@23B3d{{S68cW2Z5XApQ)(F!d(nLuYZUxB>pGus4sXeGQ`E$<X#lznzf`e*q+Uf1Cc}wf5tf~*{qqu;lvSb8lPx-gw#ezxb07WG`Rw-o$zn!mna(k<%xjF0^mlFa0nsf>&&59<X>36pTkABNuy03Of+J{1ah3Tz7tImSBP9EX;5MX`JsKH=)C**k$Do0d-I}J<g&U<`#z-1D-M`OVUP=g9{q?fHC;q*W^8omppiVjE@^k12wn)IxhW0C!KaqLwXiBstb!ESD`&}<thh(UiJ`q$1l%T_~4>`OH3_8$pV<R6ch8kDXCSzJcHd(eNl<k%-5r{Uu~uvXuL*T-t;!0P=@4YYbDynza5ru2Tq;7-gL|NVh9e7><{!X80_&trZ9gjRsc*O64<rnn4(c~n=#6DCttrnylD)~Kmamx_&CbFeKY<r+RCh_s{~C!t0N+c->eh}Wp_0eo1u4KZuI7?*Sn6hW3dUwe1gaI0+Fz&?t~H9mD&-?9|<l*Bhu(02^1@#_kSs&aiyE4x|!fl0kVJ8Y3Eeq{+>5>r{CI8GmZad_c5W&N*Of)R$?nLPutDFzS)`lk_u9hw1=^Wx0t)eBCkBoUvG_W9tb+}}R^yJ$TjI_SfC=+nNf?#n9oxVOj=xAy%`z{~a{gA~2%1^wBL6L$S>HU{*QPor@6rxE!16U_d{+c9q<V@5k7r%SxP2a1I@YY{C2S^{XGvBldX>8v1Gjn4oz<&r%pdW3@}$64EASecHrk(w!E9eWjPzVeAh0ZX-L<nma>)(by2v9kx2&A>YXh{XpnUTN8}LxCA|^=)#It{h_Vd*fUJbCg$C9$%!e9ZOvYDizzXWu^Wmjk1+s<p3M31V%6$+KR6drIPBS;;<-$9{Fu2Gg>!sz%Q=t=CsV?Go`D*{6TV%RH1<joR=a_ey`dV?#?FwO#`z2$`MHZWH{-><_QXZVQdTNg3hx0g(_P4S0<tXwc^HaQ=H{)z!GF_-3w61%@ZCQO38#~QT*Gre=i9mXV=$$6~z^Hdw$J$pkpK1KuRx&ZsA0h-xJlf|4@vr&wFo`be`RzUat8OZY?Z$+?N2abX|Jhi@@jAkxWsCk`mU5zB4={?%Neg0Em1eVzTjUdOb;XZ%7bF_>J&@uVdKoBeA#(xZSWejPW7S6HCN;J}=~|J2LcZkiovHJv!uEj?w6TX*>D1h2gx9@*ZTo7+n0i|BGMo+XedMJo&Xva%N08w-##HLPaI?mm#KD9!Q#?Xp6<*mMNWUKl2F)UZm{>r%*a2*(i!k*b)EsZokjea;rC^(b7}ZC^q|^N}Ggr0|n#Z*Q*!g!64DU80&L%9EF_^*8{FJ2Sz`Wy@F7;AeYkQcG`MVFc(0gnF%-#oE*rRZ&648+JfwpUB*wur=*sSMt`q=SO%8bZ)*x<L;jjVHx+FZ5Bv}Sc%{ta)Wo*5*TulHzGX;uG94!+)C{-Sf-g_JT1x)`><3I7NO6pLU&!Ni2zB_OiIl&@Z0rBV0DiBZ!C?N{qo80h*=nG$yTYv{jd6g&(uR}Wu4)&f;c^%sep`AVt_}3Fj>fE^nPld><a#fTcz5@0OQjLf{yH|LDp1&;8W!ymTv}Ig*u$O7iCW(x)^Rp(W3<9{Wuz5#dDkyrn9r+AO0to;Dxf!N2SN^8DQb(a%zD)dVU_ImpmUAVKsdQ$b2fCd%RjiAkeXe7W(G8G4Zoq7qwnqy`n#o}2ZhhFDU8HKW^3e@&oqxbwgo+hZn+YI9xB7H9PCOXmkof?&?j^j6CTeFmh|^BQdnWd`w}8K%k<E355)ZGLJSiK;l=PBPFynTKx;ZGwAP2uxkiV}ly2?Bf7ZfQ4N=-kMv<}c9?&auy^6VRPhY$2{AHqEWt?<fcixw_iBXW1=xUWJ#-ZeRLWIuoc3WCZix_i1QZ^203e-g^j?b-@Mz)tL9P1sLLw2%f{v$q~4;^swJ21#D7`ic}5bffScySC+fFT#MbXNT^FAND$$(uV#!t5IQ!7i~w-#3(c7sus#T-#hR++9WNyyj+^RB)7tG^{^3q&6WwxuIHqgQ<45PNFh6w?~~ZBPmgYQsW+IPmsf@yQob(46IVS9=xprb*{j-COA+Y*)wb*DjrViW@)f;h;wkxpU6D@K=z!K>hCd~w7U0oS8@``YkE^0Z|;z2L-c)nT?{r+ztG!VBJ3vs7?T;=_1{IA7qcN-=*iC<(Kc+?LwF7pn2UuCSd(+=XQZT00QQF;X`TC&Ka0tU*h7ohafl9SdE2QF<6gXOPTJM!;islhfZ-;?cLTkEmpxU<QGb>F*ytbBTEHPeWGLA#bz5u$S2*TL8t*wHt$TyK2UWlaK(QrWqN!Bq=z>`j$e`5JiYdp(v+Q;Bo;g3b9=MCbIj66GlNhu?Nd#>92&P85)Y&s|R4|cRNCl)M*;)ccOuIA_nGB$gUiDrA$}W>*?s?nvk+8c#k8xojEz#F5N_CCU3In-bSX-fNK_*cz8@xDCe1Yo<&8_>hHl#W40~qcZ>W==+MLNBY<GuW8L6U&_Mz$)$a+{nE#nT(^2=-SW3K*+9^2ecblNo%MHfl`{cySsvUGB#~Iv?^E=?5LL4va0&h`AVNVmwt+-3X7eW?sxfVHdYZdV3Icb=9Fdb50rX+p6*5$qgR*H;4si@2im|MzYQRMRw;w%-cnuztS1nkivZU99I<}gpJDO6nJ2pY8yM4?Q-G+5<ElfpoAF4Cn0w2l%(|qF96|RI_c}?aBe6+2xL^EVt;U6rB2y*<eGD(2*tEHJUgVmDL^DTEZc1HCz6%8GEjHqy#`rzRM^06kJT9g%WyItDSW+wY^Or-n69;!8&QzY$db124JHIoC<jg6l%05JFFX`Wo?TgyK1?SPaHbh;08hi^jc|()=t)l6H{SDx950L#`IwT*ryAVpPAOSc6}f_JjWO$QCJS)GA1pRNSM8m@YeasY_=&_1{URppm_Hl@*7|D~9?&VfoDJPQJ(hKiO;9tc9ha>tZPM>D#b*BK74Vw2fZi=OH+^osW_<DTOF?mH)$=T)1F#{Hy3q=Ot$5I|N!NJg@WTz&1?9^41HHZ3Xa*cY8dg2pW)S<C{wMcx=H4BP=032gdgT%MoCZlp840Vd=Fze;yMUAvG<hAchPr(Z*3?=(d?ZIiTfK+Ww`)OwBwKs2s(i8StlNQ{I%#VLL{Z6t(LuF0k!tR_`sa*+L-4s%2!1|<i8WDp-Cz1~c55pRq%TIqt!j2e!vX5b;E0FEaGXb-sG<8=Ot6i|^cg0QHfJX_rH+oXKT%$}v?W^antl3-^A}YQ1L>qy&oB)qItnG?U`%?1#*~^H2w&z%&X~mcJ-J_7v#FDaKQQ^9Iov9hMkEI%j=^XJ=~Uj9WqmIH9~u+Xh$SWbl*r7yAU0{2QKv#mj~sFxIs&WguWlHLZZN|j0l-RfT0mZ_L8I&^X&r2U7MS78e!(hb>WKvFbCc`o0S7=VcrfrcL){lk>*FAoJvdOnlI=joZNHPl_-F1*izU1$w^g>&8py8R@a{l&CwA=~ygy!j5O3L1yeD823GL^G@{PcGfgKoRaHRca8rXIh@0}Uo&<FFzZod8pC>P+Sg~`WywC$BYe>(F+H6AXCo;<cWj?I`}Iz~=(!|y0(3mH<h_|UEW&dhB$QFV`p9c)`5d<la_L8&*%FWJ&i?-yi>Ead=bX}(R2?E-Q@BtY9_@`wr*xdYchQ*V1YNYHAOcQ%BZ4+4y~4Ax1mb8A8GG_dpP-vsM_k<<ieCJ_4I$s0T~f2jpas%0!;Ad6rcUK_1u3zI(ljOJb%$+I9CNn6g5pOYScpN@tMi6JdsztP9JN>Ab)V06W*v8z-OppU?5PmBEb<!$2i%h^V?xzh;o$Y=;txD){3Y(o1B(aLJq(7-0fIm(qjv*WrP(>L)a?+Y&cK9;$%qQI#byPV@h`e@1NhQl$F5zqj;87`rAhttqjBO+@S#wl;0s(*m^w`_!ki->!Qya$D4*e33B9Y0TG5FOfKKri+p5#cu-;vbrGl8$1HTrky3kNW5{>6A{BbDg*aGdrNq_wQ2X`fO1|V%ZE9(fmj0+gA;hwc{w^SS}MzliW|MrU~;Fto&z8P^a`FJ?T#?RvrmJd3!68o4YqQ)X&@OYf4Eo3R6Rd+)kb#%1eo#j+Sp!2!duYs|EVky2|V$G2k`ph!ggAhs&v^qyrQwz+v*yl+B)NGd&a7qIFY5OE0KgTcj)u;~i}5A3nPt*R0fa`Twt3Phh5(<{T2^I{<Vx>{Hy*3s-^g4)KgkaS4VEw8_3zt)}OO=w)#5wZ#^BR9{BGTAU&|HWQOchpI_KTpq%Gsfr-nuy-y%f`4Kl>*c`}!6eY^pXuZP@!;HP$_U?cak7DQ|ECJy2I(=O091D@RdP}V%3sjKg}t|Oz7KD31|%7$Y?{;Jg<=+*2H(uZwop6c4Z0J?C9^px_P<(0O|Zq*xBTOt{tHrt2E<l~Cq7E`w12;}?Yy5phW1$=QQ1<6)key(8BE8D1I}XJaXw}ZGPvIWa!um;*A7QgQhOfc?1rTXCT^fCwi<cl!0RieN6riF40Mh;hKx8;wF#8OVZVSzDZq%#gfj=r$fuegCYD{vcmVa9dPW1{vm$52l`UGcq)<fgL}A|Wo2fR*8|}qs!~-+V&9ieNH<d$pk`IK|I^l=t$87*_HcA6(_sR&#0JULGQG2h<I}AP$aON$g%6;V_W|3`_kTiVw`!IreJmC`Y%nrlyCarZui4$1X?9;N`%kV}O=Ro#_8Pj~_+PJYBChKKjd<~q4xUTnu`J5`_uImX>g5AygFkiU5gOTx@QrDSkYDc`xbQ5aGandrm6aaRVhIY=dA)ZHu1CA{U&1sZt{Lm?%f-z}_ANr(hRJZ2b_<tv+!5Cu-l``dxr6!*dgth&PuI9>EUW9!vHGHdcZqQE9av_2JzPmCR21ZO}4uNM!beK?I3Y$`)X$|`I++sv8VzT1b+kyVmJ$(}kmRj<4M%^(y2oCq$88R4KvNJw+%z&0g{rIempO_YKZ;ft%Hzn%L89a1y;pf|XxELwL!CUc{Uu#42V$s2Bt_wP7`YW1X15GodKDrZB1jxb{dGN!T<uni27UNndKP6@2oe3JBj$ML=`gmZp_{eRGG<V<njuXTjHFj@}P?2waLx>=a;P{xw=iB(jX^)7?st>9&T=!Gdw?KX|@fwWNY6QM>&#wE1x7ZV8wh*oa-jrEQZ}o?wgjzYPaUx<fGfTO(jY}-U#q5ihK>AFk)c!oh1SnonSFk;MuLqLK3zcU&JE@!*5#6Z^WcA$;_mUo9BnS1Al1J3|aFa;IN#T8uO%Grg4iYWWT`hg|*41^Qf@VLpL~CN%mL{kckBQX?570>CRt2UTGEY9CVO=?=W%tEbV1rV#x-)xZ*qqLoLW~3<oyL~L#+fQ?5O0OV^knyoRQ0J#tF<z7jrX{8rIFhDvmr2a*d5zzHOG{oIlMmI5A!eGp@REs5)Qjf5<f^nIKyq22cbbM3}eg-Ijy>4Pt!UgW8g>7F@ojNn0W0J+dcdRD4ag#4`?Mr3*2C!x>J5!=KlE}y4Jj01i9RjXV-+;r>uUW8ijPeaKu*#wt2ZNEap0r8>b5DI!b!?zjghQ1X1o`{t4t#4FA4y0mDubn`=H=q;SBjJ<D#nTFjNGSfW(553Qa7!8OE!_O$U%kC?r(twZRx6NM`$Rw;$qgKZaAdj(`<a{#M3t(T%nAO38#AST3!*OphLv(A$CPY`^uoo*VjftSEJnI@9%S3YaxW{F2|-W(Bkyr&m?=UUAsCqM`3`50F%-XAYosX7`8)8EEy=(Zvc)zk%l?<de)_Bq5*r4jVbDM0rk^8tw)Ej;hVceCt};5u3q$D5|V&cj`&#&*&(ryJpZ9;wk(maGRC8Wu_l%Ku>XV)NXZgOX1Ey3a<1tcbxrpK4WD*(cywI!MTnf`&h1by1Vc@<R5KStm&SEuzx?m`(zhK79Fyiz14v+1R<r{a0vR5?l&ut)^z--Ky$&BC(Qpi%Op3&2S0JaH2jdM)nev%QpnO3bHUg=doqYMI{_vPq>e@^mR@od-gm3!k0Dx2_lZL{y!$gFxrqN4aej)6q0i3`GJ#TUNJxTtU$z$%T@ZjBRC&<z>n3@ekm52>I;*CzV&F_4qbv?;qo*PH5uV4%-V@2oJ%L{UMzgxl(R7$vO!$IV<*QQ5+8#N+Y>;&_Q4NQ_Hx=L@6r$JKzPLE0yZ;sm#%2MSNw>aoDH;Tra2li=z?hB^^AA?<;qJI6TjxBWGc1HH)0CeA+p48B4`9L&ePb__M;FyfjXX5B1@6}f<%qkkHdk?HEMHu<tQf^Qnqw*F|b28&l@0b(Tg{v?jNh)8<0bN-r=Vm`Cxh@5*L7MGq*7?9;=!8H*Nqmi~$tlr_pW`8`7lO++xn#KxKyl699iNo4mpnTT+@R8dd}x?C~w3=tPYS$rO)A;MX7nZL?kb$@eU@&VRijc-2+mf5~lCNAAd0n-#<G`_Sx~Ynw{ia?-a`x=-gTbTcnJ<Ej_wxFyf}MSx;tii^MJ)2IR>>SXUN1X)g(^<t>2_xHP&SndffZls^;2VeVEQowZMJ1MoutH>WkZQ@7OOLI?K|3_0iz8PS=aIsdL1)!kzeEXs}N@HB6qP@VHxDLi?aMN;&lnzBw-wFxpN5QLH4^*P)Zx#>v6A?yReE&Dx>vr(pZh*schL5BHkaoo%sOl4qHkOJgsyUA?7TswEAUvNT7E6yxY%I^Ge;pKc3lj$Rv9Hwhx9A=}@Mk;Ec5AoU2Sh#fYy=v4h#TpXa6lmX6ThYdir{?(uyl;#lKfWmRs-M^+TxbOhh)LHXg-XR_~6`eaefI2rv3y#THY@9K;{Bzj*Endt~9xLx8>EIiT;o0MEO7iE8DFQEc5iiqDEXggUSDy^0;wm_M=IOzx0TXO#cI5QTif481sLkvGy;Ts@VI}zh+l~eagMoOWheQT)?CI$(3QORETz*GU>Ri2i~7$wPf}Klkis+5Ab&i+L;0F-~0?PG$g+$d6ZPu!oZWO<zjvSsW$=NSz%zul3T95A0R;C_XJwl4IuoeT64?_Jm;^J#&VQ^Xw937P{iiAWl?q_3@g(KoERV=nhjyc;VxP5bn7Y;$kMrk8NcZ(4Z~63RAbhnIe>SSU2*sCQ!kTosJ*I7xU=k+X0=-#tLtf|mkBGMQ}|pcnw(bVrx=R>`$iXoQnu?KUt##nmwWy6z)u<I;BbHsf}d{Y4pSI*(JVwZr^0_a1^woEoJnklz47f|6M+71-4aNe+P`VhChh9z143db$~2y~?p86!Uf{HfiY~BYNQFSSQ<aY^aechizo<PBH8T(ssy;S=a-O<X=ISXTS#Vh&D$Vlyr=sK9pH!|COHbCnflr~YrlM)2QoY-WN6JZ_mHjA=P$q%$wDKnD&rNmJl;l1HCRRf-j6!0%mIeEN9>}(xv)znKGEw=p>Dwgblgp7q5?xaN|CcP~0O!gV5P7HgjD0vq>A-Yv*DUk7F7RL8f@1Q+EH}}j%qkS1X6v@pwdSU3{aFI{m$Y!Lw}_8|OpqqJW_Fzh-$I|T!tm>xJ8Nr3@PH}0%K42F`d4_u)PPziCNp)*egS-qyB-%B`OXEUarkzPbVB;gm8}x@7~!q`0VidUn|haegr#lC;WB5ukc^YkCYDt<>rV`k%OXM0qH^A-?To55hp5M6>0E0IVmj=-c6e%F#$~1_P?*?R8XUL_aH&PItops|M2DPfL!vXjxa8ai6kLW)bkh$IVIM887B8+(3#>RWOdv%DpCkBGpDnZK{0&_=FC8ulO{J^#E>4Ke(%o?YqLka<^fh{;00FEppnU)U$Y1CkvBYQl0ssI200dcD'
words = lzma(b85decode(WORDS.encode()))
assert sha256(words).hexdigest() == 'd9664953fe4c49e0b40eb6f6378c421f5f01dc9360aaac6d2a3c294f046ef520'
words = words.decode().split(' ')

class LanguageItalian(Language):

    code: str = 'it'
    name: str = 'italiano'
    name_en: str = 'Italian'
    separator: str = ' '
    is_sorted: bool = True
    has_prefix: bool = True
    has_accents: bool = False
    compose: bool = False
    words: List[str] = words

LanguageItalian.register()