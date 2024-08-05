from lzma import decompress as lzma
from base64 import b85decode
from hashlib import sha256
from typing import List
from .lang import Language

WORDS = '{Wp48S^xk9=GL@E0stWa761SMbT8$j;2-`Ei(LS7ri_92AugD_$iX1PL|$;ll~@_zQVAf#oT#TrMfxNe)2}U@4J9V343z{Kvr^Vr>!-#60sm?oC$iurw2hYS>(8xhY~zooo44_+l~*^vrOv-1c)2!*qF0NGjM2_FI38oFQb)*dvG*49c5dQMV&M&Sdf>Y%bqs~pVsEf97boS%1brt>t@~F34Vgha@nVjmtH)ivb_?-8o0IZO^yMZl^>`yB@^4SNQW8@WEY2gzTp+t0da(dP(j#hpjozKl=}Y*pKO2&VuwcAUPf;5_{c#+|JCHfIYMSIUkI({!;U%E&AM4w-`_T+_P|&NFi+y4qB8vIPnx+)IwoEbB+IiSzbKGUNErWncm~}8vkAVhe!o0Un_+rVx3J{_fSz2~7h!yeMps^NIeZi6)A@=>W1$I~HV!*pSqzv7#=H@qDzBA*YhO;&*&()fsXt@M+A{i=!sEVop8-v>mNE<bK&VvOEb=@H>w=u~PZCHQm!WoCylB3umv^i%S=(%A3W2F7qHU?#fD<BlBWdvIy_Ji`Mw;$WM$rmD{KZzfaiJRh9L2NI#uVf(053szFUwBza_VeCfpNIDLnTle@_~NP;uW!`*TLrxsStG}8-DawK5hl2m1G`&hqb#x}Nw;^sb9vjL6h_v5CSihlzZKL89tj)qY09W*R#E(KKmRss<K&)xjNc!fn&pBxk>@I)H{_&7^ogq-r&<i_X?EEx6drE=_lOoM)VRzxKG?{_1D9JF*MLEYXz)|wEz7u!tLU|6;*B0};B2ntPq}$S3Op+VloY)VD>7YAF4YB)CiDq<PZhBCsRCbQIYa-X7zJ(d<nN0bl)rRHt9Nb)N1}Zn!*;-nDB}U_oC!DfY)D^))9-Q5%PI~2#_Smbn2bhbJM-{s)tO1jr86opZ9v(N$t%b4(oEF!S{~6KxZy%9FQg5n%VK<{d@Z5lTlqt^buyzhuh<)i%_-iNB^s%v4Q)Psnas8J(^S@-haz-Lh!xZ6Zn>3VYeiQ<IQpl1!sX%6t`|UGJ7tiw`MgiEItF#~A4m3Fas2<uM$MJcgwsvi#^4hVroQR*2njg~0@%<)6)&xY4mOVXj`nx_HCBV4;=v2n#uhVI@l=J(bPzU7ScSpcAtPz8i$H(0MXD_>v;<<<8iNtYxv+Rc`z94!-VyLf_Mj0W!c&3c614y(;6vRqOs5q#F%pA~&Pth_NU0=E^(gM|Pb%I-(?lfehRm`jn~mdFS6~C0FyY-jVrl1?du{(C^hbwi;&QDPphY}^#58Jup(VUrnFOa)T>Awk5^5XAl=a=>t=P)kc}qqOoi#J~l-BTu##q}~_Uf_kR^3@GCnwdgx*P);cTKMmOnOeIo7SR;fD^}NPqmp<QWcsWso&V1&41V&y&4Mwb#$H_>IDbmlbl6bP8m+53=43kp^IbpIa<@@CCUsL#gij-T%O-Q->N!Tl$HRllY7V$_Wp{nP)w_b`Q6tXT(yn!(NE813~w!03(J|gyJ*4Efw0=U<Q>64646C00vC>LHxy^jLAalZQl^f2ocNnA_h40nKl~%RZ=>6}W+o@nX0AEVUg$?Lf>~NBYF4>VHNgXA5=kx&VPQ@aTS;1s)LKJ<K@F=XwMU2@M(v7i<N_N-eT$-j;U(Iio4J+C5L9eYldnp_z%Cf&fzNa<r^R73j6Y-quGWj6)?#N9SXdxGuaq0^V&p(z-5}`m>ssdyi&reS?&ta}<Pac;a8szg3UuMr>CE&Rw#wxWJ`4(&3?8khu2WkFtz;Qs`|`1WujM}*q}BOXLR<ylb*)KRgO_TUuZh0XlpCb8prpgFd*r1BY0Rl%WZrBuUZ61wQ;q)!WmmC@l+qB$UwS_&;$F44_jTaDcW1y_5}1}O#eJCUpHJn80U<Rn^m_{Nvq}RZUsqvRx)ID#FEuRHDA&c_3wTiTeNok3Wz9e8WEEj1L6h?Ju86g}Xzh)@%&I4;5l53?w2ld)B!qlO#O*(r;E(^NbBfyw7roM4umLy9Z#~N*g<#sk_QQ~TmOLiX*HaX8Tovt?tF6+wiD&b^Vg^I*7*M-3U%K9+z8kswxx#*y#aWu*{B+oeHLofNaPWJCvu{rfn2_yAw2Urz?Z;yYT+AHJuHjg_RXYIx$OZ^MH7k$yR^MwD!f;?jwL#(59C5}ySV>jcH=G?U?oZ{ZJ202?Nso%SnEn+`4ox<g=`4N2edg3SKWZQ7S(86HF)0S6T#faj4#0DX7w=~1avAgpv1I?ceRLu#oV3<W;$?z!qZeA+D~I}*?pno}CdH!7jyAxW+{<rEC#@%*8lKN7+ET6E^E$nPl;=`>9ghYvoUVN}USCFTup)kg8l&P+^3cBx5`XYH00iI|K=HcujtB^!9=T8M+;<jUfX>qSruBMf?+?`qMXrg^d%;?{I8m~1=e%^Uzb}v}==y!D4Sm-qvDa29o2JnE5~CWAI(a%s=8q~zQ){fdQW%j+zHXV*@kgCyzF9FumDT<{ft+~9jIxZ;#()KRWS(>9p&RZC0K`LFkuDOMnPyuM^Ka4V)Kvig5s#?Y(J~@Pf(WeKa~u?~xvl$zoi07qxF{<FjcEAps|b+5<+S&8PW`^~;4jdT?6RPU%J<m6HBP43e}|;HZ3s;$n0yw<nG%n0@qT%0Lrl0FlF^NA$~;Hh;K04Av!p*&$7mS1KTA@WB@b>8tvBV2UDmZqn<+tThp)b^b_#b>D|AAZtO@l`3P+jIm#@0t*!B+!36qCR@!Nu=+cVvCq=fz1i;dp+%=U~}y8{wmN|#keF$pK;^+IM0Nrdwspz!%+c2%L$S_hd1ZfGHf+;7JjL%)b$i08{CbpT-mP~i&KLCSQ<KV?b?v}aj}#?>s%mJ`PD8lHQapmNOTDD9+tF^?F(?QLZ3&%#6j#{U#wTe9Q{9sMp^(nt9Muh*|LmYre5!&0<<M#V(X&V%h!^1!ZYCf8!0C>ITU7wK&G#eL>7tHU@A8YP|&@xr|v(yot!3`xLQY7`M0rz3OUcLR>8uJ)Q>T1ll~Q#G%91>e=%!k6aTE=fDnxJA|nhL9)YFq%n9;C1yIxSC2ku9s0eL0xC?Ceh|p(w5!<q28Gq6iQrs$WdZ^SJ@f4P{uc%Wb^=Pxid0Own+5eNeW4v1s5-Esq~rhT|VsC)ACOSX)YO^9V%mnjQo|f7M-MK7@l%|DF4=mrH18q;a4gDx!r*3*ciHY4%cOySLQ-lzo*t#I>P_1XVWl1^1XnWryTYK@6xG;9VuqAQ&p~~|I;V`hEDpz)3~r18)?(SrDvN=Km_PN&Et5AB7hpY6SrB+ohtT7>Ri%zA?*m+_HW?UN1kz|0Pon1$#!;1NQ!=%dl1Z-dsJi2)4Z3ZF3he@H(gIqws&9D$kxlOr~E($3f6}|?n+gRGuec+;>V1p_7Hyb_KjGiI&1Z>$W-)?tSb+l*YU*+Vn({jo*0IAaYZ((fTBe2f1x^)mupMx(*EI4zEANXlj|cVaqyQb-8r1xP-+mJvbLRx{+}U>z3xxntgKhkqg8qbFW48^POsw+8f4$pX%i2Jku&n5bz1vG(e=ew0fxAtuqqQ!2un>dos|JHQ6hoW-4VF)baqleW>n%bDzTa*=twe@d`&@L@^<5>d+M#VVTFW9CxiV!aiVY7CICgXh0{AVS-8%}*t^Wl?1_J?KOQfEgL~+bst%svJMJ2>%?z=f?nra*dd$ZV=!<HdwyYMY65`20WydTXYG#00l|LXN`{+<VeP`ZBQs3SZ{pb}r%9k*0--OwrDz$$xTDRXU;M|=yOBdq8XL9nUTFj{%L{_79mxkiv`6u!}W+7_e2n4B1kk5T!b~hfhuG&q*XHwOAM7Vh0mw-=21+x&v`H#RZT9ucf42pQCTa!z2PWf}942ltGVMVcVB2mKB9!L?Fs|336f9*<nzfON7>*3#!SLYPzrOh5bm%Q*L0j@_fIi#+mfgMIXS6WJnVq)<aP<ZB&n(p|IhbC3)_}tO$Pg|*Sr6oK0y~AE8FY6%g6ZVD_$DZ3Ha!VhslCM$b56F2<a26K@{cRfmePUn{rNW9W1T2PhfO-N8>q#?~eN(LkU)}(fsvO}9@#@~ww5x^pzvM_c(H;(5X^1Fd90a@K<KvB^3vpR?(m<;f`%AG{PQ2p&Hit|~%5g_{hWy^--FkRAQ$W}OB=okNsk}2rvi;qHcfsg^sDHU}!DB2+?l}D?7MA!<&w;VZBd$RvL|P}3x9BR;Fcu)cOuFYIwZCdN%NvuwG_)Msva`=t9u5)pnC!-$4x2i+f5c3Y`dAs!-)1zS3O9RZnqW&Ud;`X$fog<;d-)qb3|;^|H1po_RAXy7po@>J(w0M2vYujRxB%u=!y<i3$T(b&$Y^_?uLBTMa#xnD>gev}*!0-zPB7}ZL+j{<4si@wuYQWzdl;HH`~2F77|IjDEZyP|RM7|A4j5>aOa$ubMht_ZgRRB4sPl25MBxXfBqo3!{zCt!+k%vcSipril=-0&B-7of^4rH(CFxAjwg;x(O@Hj$yQSf>89$1q7nTO#f}=Q`f}SAV;>S?*JVt%9*#?x+w-<Cwmh&qbhEjSzEv{k}UGWHu;w)E@DH<Z1QinJ%=SIS9+AsXFiZg#{@nK-K{?|6X*Y9f@)GYTjnMg<%4uD?xHn5dUs>2W%aPp8CW6m@Hh3yB@8d!?}Ju#wK%{M=#UG|m-QzXOB>D=h})@tCo%>i2x<|2$|N+NN#xbhN;Xz}CU`Im-q6p*;T_#Hj5FrJT2K>sDTXUQF~awSRQUY7GqXB2H(Smtsan^AWRGhQ?n_OthQrsfh-tWsO?E)Ea|5<uHhC9>$)V!e$P$OFi8jo?Z$*+<>%X)}GWZ+---(CHYBHdPd`&Xjb_9hWTUH?ZIsTp+jEga2c22r-C!JzV_141E}27)nrZ6(xCp+CD|^nh@K?jH`dFPE2~UBZ=1(T~gRSz6*d^eW4Y&HS^LPktb(!8N-tiV^g?fgv$tuJPskXr@d+L_F@6)$|Q*{bE(4TH+0Jo_#F#;E=hv@Edu{RPVxDw1Wr^IO2}Z!(9kNI%{K*C2IYKfN9)qn>6x}V7l3vLYs{g^&yXh(m&E4S`37SasshgvQW1PhC<Z?Fnw_O;{(k@f|Hm%O;4{Xg00E~T|33f#gi+4avBYQl0ssI200dcD'
words = lzma(b85decode(WORDS.encode()))
assert sha256(words).hexdigest() == '11ef479f2f44b6d4f7fb6239dff06e3cd7a1473b83df6cf91adcbbbee598acf6'
words = words.decode().split(' ')

class LanguageChineseTraditional(Language):

    code: str = 'zh_Hant_TW'
    name: str = '中文(繁體)'
    name_en: str = 'Chinese (Traditional)'
    separator: str = ' '
    is_sorted: bool = False
    has_prefix: bool = False
    has_accents: bool = False
    compose: bool = False
    words: List[str] = words

LanguageChineseTraditional.register()
