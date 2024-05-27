from lzma import decompress as lzma
from base64 import b85decode
from hashlib import sha256

WORDS = '{Wp48S^xk9=GL@E0stWa761SMbT8$j;FHD~6I}psp$rZbtm*LC5e#t_<v{Dy`c34p<kAGZr{0XUZ_$Eq2k|0wj-1Gb)L4xmEjDeMteA|OYf-`7^@tsbF{}3znNF|aEaH*7y_Sd_!~gBJ+#uHSZ5m`C=AFBi9Gb3#69sfD5W0h2ZfYeDAk_?m1uKn7{Y9kEe#O)%96iFhaxj6{#$f%DNPZHS9B8%#c`P2Hs?0gZOvw2iCcq*%<on^u%evi4jN3o4pt7pS7qga-1-6G%;v~?xNmed*`P1rKjzi5-BMVg(ZK<2S_nTZ6-!HSXf5WuX-^nlMm&R1irSOns81)-?dfmjGjwJ6!qP}clqo3UhOJTOOzj*2LJ`{bfdc!>_*D85n$UWb%DPEH_fNe1pGlXoy%;qa#<)#-PnhB@*Wn%g+S!5#FzqQ>j29R_iFhySqFXX3EH>LaA(35a>(`4*Mv60r6iyOS4(~X@)zOMNv(8Mr8i!;X|S#K{M)y3mvKX@C45$wTNWAi+qYML*i)35N}gO1UoyTvecjeA#MraF+Nem9*MEJwr!iQvmKkpPkYX3DZ@nkDe@0(A0~hk{0wQ;Y;kK6Rs3O{M7LCAZvZ5@LH5g2t2d7#yAxv>UZ)aNU{(;Zr#cI2M9L_XItA+P=7scnPYV+lay=5`v36&ef`5&r^5sr}Biu{Sg6MzK}}em<j#2tXLKPl6EibC;#TIk)g0sI<cK>x0t}NIXToH6E#7SsdvHwa$QsTQ%p_z$G5!CV%e;9&U(RCnw21w8#Amy*0urkDbJ&BN&J0ZBdF~ze7W=ry)d}oD6-5QE;qrv-P<FmvN(qKW-{R^e5NJ7S$QV9<w$_~!XqfM*VQc~bQ3!Yz~zFTa+Dk41TCC%>;OlIV57r;?RK(x&FcA?;)J+hsYdea5daD66bl-Q2V$;xw24i<w~Q?3lmah;+C&_H9>xiCn;`HGgwPi9Y3q5ur;{FWV{$ze_lXt<;wzY{jf@yc+ne=c6wAFw__W-#<l?vC&I&b?II&>TF?~awakQrWw!C9SEc{fiQJcg}lHh*>xTcp;9h`mcmLkso?=>g}U#P43n<&g+@HTG0p};BZ=&)%~BTptSb#FXGGQcfUgT3H^$eaP%=DEil+7!yqAZh`B<}kgmb2bye%Wwt%7MV+3GDcC|lR1kjpTiBJDND?h&H6<)RM+m|h+qnCHzh^*t~;%V3Jh-22TzcAt0ZAMGrI01Yl<7+w*o=~tQmy%sGo~^Q5{e6eQf!2&=MLWhkE=+Bog4jPjKILZNjIh*A#*(ydd+X)a34pzPqhx=vYljKm9FfnxULrm4<f?ur^gHwzlAxI#ZNE&d}moR5d1t|7$9KclC|m`@oza7!0t5VrUV2)Q4Gv8Gh0wq65IXOF)VjAAdj0&?1)72J85sa2kIsec}MNo1b6w!cO}lJ;N|d-z)i(BOJd8t(MFz;j#cX6W4BXRIvI1fvYd?${}vY-`_7?s3M3S5a?q~1<E-lNjA!W;lTgdz!Q4)2);0Xs`8GK5xpdsJnAvqj~5)ixiC^Crh{W3=vkOG;XsbtZxR9)rBOBo_&0NklLbxv&-5Ah;w35l(KtrekrwW{3wrhb<+>Vv!&l7zEFoYMfKpyF1aKfZuz*UdB%7W_Vs;l6cK*R{H(ZbOB(MQD#tknjnF0x+FSM1IbfUm)`&m=N6<?uC`yuJ-LqV+<;$(E0YTg#lliPuBQv1?6*o#HVpvCUR)0!K`1BL*}b?h8M!WLJ0Z7%LMUQ;7&IFr*plt#oW`bG1h+l<aytUL*E_X-jPSIrj3<MBUGvSE<eiUhboNO>u-sOjbJb43$W{OvI5_+sSwwH8Kivh!=*l3TW$5+`e6CmwMak80;*&ZtEdkKeZj*?zuUP5djDNX+q-l=*BAaw}g-_Oepc{x80^7(i%^;6AeUGNfgWygT%^-sQUHb~3j4d7TfbFAt|&VS!gEnfAOzIK)o$aB-z-2d6<#LtNOl(0QoNiG{V~mRDCIU&M(MoAD<VS>?+j#Y3FyN9INh_YjyVCY*KemW;iVCG@G#BNJWhAmKr#LfDF>mC(JW%Nx9IDyIRokTC`eHC9v7+)WgV>WHF!*07=eGmi*FJUg$3>K$2g;6Ht(DDErhMY+}Y{kSZ1FWdlOb_Dl(z@^1gd|e~%vc`6z<SU_wbDF93L8?rR(tQ76I(i^~YD60C@Qu--DdO|yg(v(=#gr4|#lXAh9MZ7YXLN4wG<43O6!lyhf@AQLPj=Q&Z>v;wiyrR?zRuBR{JxPej=Zf2f&;$=DR~O?$iA%RSu{_M+bqZU1)Dc7_{WMf?k0jz0fA!oB2|>NSw{E~QJgkpl}M16bd(rC5iLEejAX?fv2eokllq0*6PokTW{>PHaX*}n*HZeUYvni$zEbSRtVDq5I>j$=AV=On2^B7^(uq=OBR@sNBc;+Xo@hTQ@*>$(rDa<)1H8!wcJJauRs$tIyylCO6>ziRpop-7GMd!qb13fwRP1KW!BwJ6yS$^J8pL^=Bd1;@ix)z)Z;_B*{$jmc_~GAQ5iag%j6dVKK=`4o&sw3zdg^#Mw9tX3#H-{InBV_5iwCPS9RJN0^e?x@*N(mYSK9@O)|Y6FpL>wRSeso=LFk)E@g2&ia_8ti@dQ)F#*-5QX>`R%Xt;-qb<&6Yon2n$7Y-TBIqlE@<s+}#67Ju@$#Zz09s&r<HM}?EaBQhvv}Au>1(%gr*)ku|e6ZEZCyg*5@f-^=%mnDqB*`2%H==K5Y1C2a?$$c(*_i0w^Qz`u1@E<}S{RM?W?C^|wmqXSXGnq}<1sErG1eG{gL~=fi7Vb5zM8enJ0r(l28ZP8G-X*&Ed|gVFzKo89=2;KxG;r%Vx6*Ao^jIDRjBD-lew3Y;?Ess1!1ioq~{Op97zlndOy&+U?6a&^X@cY0FhZ~oXHWx3Sj`Ns#!^{t&Hl0n|msT?qPwP_k1eCE0<gsbwRzgBzsM1XxGf7vh28RjeQdLlz*Fkp?aOGrYN>Ght#Q~stjkRojF*3Wn$(;*)#5C5Cb#|a&*XA(b9h<vKtw;0?3T`(XDP2yq3hs*6NxtB?P}hlKr%_kgFPL)BK@HTR(j=(W2u%Qw`MH;;=hpCfZl|1w0f2f6on4g$}vj`^)f#{BJmrIt;H7V&NxF!zt04z*2wi@;(E>BcT!XpVtaxEsTN{S#Qy!UWgbSzgg3u+LBAb-$Ll*3+!LQ7?5$3D5N(Dek=&?oop$WVSEv{U&HZ;dOdoJ2oK~~r5SAB4h#67xW=+d!E!DlV=}qcJRZwiuRdxtGzPK<GXv(d49G}OIhhS01*yG(x_A4SHO*9gB>18j3Xf9g2vmjZE#7f9kd@tJi9K*3hLGEI<h-2uA)U-@R)CV879tDr^nH{N3)RZc-GL@><YR)B3{TQ$9XTuQG4=7(5HVKs%Uyk&nb$fmFS4eqX4{DZ_`uZSIjmg(s==h)bji!ZYcCP2Kafntdy8XjN)c%$nhCjgpK=?Shn+B}uf;Qk5`WXm7X-cHH4Vu^q}rv1De0Czoa?Z~mc?6E@jZ+NbPMon1M~!sbG)km7$=$z){xN<8!BbKTF-Ub5U{Gy>OH$e`2|6v;-pc3fB;TJ%u)L)EP>_j5)xJf!Gf4Jo?PSM5D;^$g)Q5!bY1)=MMs>%)A&A5FMgw2lXO=RDo!BVN1<4{#qs#jfi-Y+&#`*sCN>r|>DZ{!St}?zmz?Y~?<D8zP1UBCJ3b<wTV0gt5{}Gae^>=F?t}8-b@{fMcN$=R6NJGMK?NVls>TpFy02?KgkZWCFiz_dBU~gDOfORAfHn8ZHZV=l#l_7zkxTPNKM#%}$CKH7QFQg2*_O!583!XjJvw)`4!+|s!nsePnCxZHj2t(Zlr++>w4Fl|$*8(v3&F_8!8WMTW6>LLc=fAR5Y)&WSM1);M+hN`$tgt~I4?tE*)E??GtR#Hh<8WwY}CHbe&{-F=CO23i+AoTj=vh;+R=<DeB_!r`COR6lKJYDb)Ih^?G-S4##i1)NoCt4udM21{E|@#);E!==mbGw1MT^LYnmi47c+zo>k<UE_NBmmY(%)^24k9$_-@>=V$v<9?|=ELdq)GpQ1wk`YXDpG!5^sx`UJqvY3Qd51V3Ya>;H8)g$!_9P>dw+#@jf1R$r;UQK1o*I2_LIq>}##nhqQ0L(eT$__G?dEjQpV)<v@+4ZaL38NiQrFP%EZLGxvTOqXQT7Y9mMaDtad7%&|v9_L9um5TY=>%~l)<z%FaBn=LXXcj&zT^i*GuB?Y0z(WN}5oZxQn_7d@p-Rd40MbJYO^~6BArPxsL>&!xzp}&G48+)zh>Zb#1y@ZInIS*J*%bE-c9ejA@cEAL4}hkrg1F|-*J~N-ZFHQv1hnv89B5S~OyVV7@{+sfAzWngVxK;=5lZS|Kmowzx>2T|qlt`mSDxXJSn=Z_R$GkCo?c6w*aJQ|@!s`-yGr=ikTuS29`+^eB#X<{g*BmNzUvVyrQ;ryZ>9Yc!Ou0QrxwIdY!@$OPpvGPSzzcG!?B)Sj;FARIv7#}vA?5JWi@p0{yNLUUijGFwgY3I^RKFYk}ECfMyMnhsfdpDQ8+Zi#``RtF+n;U09FM9^YTM}rPUy14wJvp2Ax$`bT4D-@Za)Q9RyT)_VYR<uykLRCV1ohaltHTa#W-E*s!kIRO?#34?PIM%b$L$*zAmGgkw<_<&2oqYVn5Wm-p!4U`QZlgZ<WgBh$1~RwdYd?(r|4je@~*cdZfujl@$fq(=QR{{4e%Nx72r&&d0&oy!&IQfY9ZS(HL@xlc^^%()Ntk$kxRl=}^F9mk;G*2TR`|Kv+a|6&2XlG9Vb?|lMs7K1)Oh+71Hy`D{>#!@!iM$ZytY2UthL<O;1nmmgN=6tGuj+G*on??gIHoyuCdW{#&J3cqC=$d<+!0;w_VglqQ=P2_?50*OT$iNQVvC~Tqj%#<<vHXhR6%Mf+>}aKKq<lM57~SC}IRC}szC#yIPt-q!psuvz2!|#fWv_+I>0`wquTUS$xuka7A1q#M4GKD;(B^)C3;Cal5w$TL$}Cd@)Gi9~H|*K$9eL>y1;p<gAbiF;Jm}KkC~Zt1i+j(+DFnI=>a`vqA_O>51aWhXoW9HyI=aLV`(7vRs&`9Fk?_lgzH+;9^gfMo;Zsbk$%M>0M^bw=Ur%iS6w_@;K)z+6c{5+BJhXo;xTJkO?X4*~Wv;V(&oszp9*=<>FJNS~O*IOPdnRZ<vf=hy=d2zqVN?$2UJ%3!alOw9Z44TC2L)qJt)7Fm4kn6WJB2M@Vnxl$e2qtX*OVnGoT${IX_+GN9#-q@lb4&y;Ol^MWEf5s9e2?87sh^!l~W;9oq4Z_9L9YThtT%b0#E}rnEXO+`9HsBJ=3E1o~l$kQQFuahPTLD@^-PN{}M$A9@*GuNGD9TPs5VTZyFML`;6y7o0Zpx|D>g{_mijSETFP_G_`$!ri6+6FShM(4LgCZMEWnMOYs@JsLd&>Cpu)(gP6yJ+Wk6CLPlhYQ+iR+xyb1{Qr~+#5)sIIu(QDB`zm1su`HT)FFE3EsyFb%(~q_wS*i0fu&i1-oMC@xyD?%d1ICduWp}J2w(9O9$~@|&cx2D1Qy5kTmY_TF<|U06$5aIE#3IPhWNgdtfHqzFJ(i1Zk`Bd6wCQUKkEHOFGj8AuM!>*TT)=FzvFJoNYgPj!F4IdHeh=BNli$plSb!t$bD_OwoO4L`X$LT=eq$)sU^Sr-G(GD;)*h4c4BxSfRRWo-KeJGDhn}av4vf{Vzx+-#h6_ea7!8zx)N1n#YjOILF~Yttn5F@m(siYpFOY$Mdz^yw_!h}ZmNJTBy3#xkwP-ijOZbEaPJ~I%a)M5z-8B+56yaRGC-<^9(=2<2ezfLlQvKdxnIty?`nba7{#7A2*OsHDGto?Y6u;ZB;_IV3E^cDW*pBA!%n)_`6DO3cXue5}h3z-7U)#GKaJVwa`_st#(6Hd%I-Q7Q%h`X-yH1qJfA&n7NW@xcVJ>)q@ApILsw9FjMQ}#YgtF<S6*r7E(@bedrXl~DIJd~56_1w6bKn#<`dYztW37@R@)cNjN)#k&c7%Ezfqddr1}@A5jJx<Uqp|I(yP;)bVR>-q5B+RJg|6gGW6}Nu-n4B>`{Zi5YL7y^`U_;+|24REhX&aKH&Wf6N%+fQ^otE4GBulzvic!!MU$WFe;^nzuiH{53dcqpRuUB%_&|Lz>ZZ+U3tMyogJwUPgqL@cwnnnhmZ!V5F?(X0vv`dr$lIZlw`>RN@3X_5p>uheS<u4O0i-_>3wvl^l$vGtXj{)%YL1RV0?1&rG>r2UZLaQZj2eyQ|0+>8mli`p_3_k=0Q0xB7JH0K4gzszVbMj4t`R3#*{>Vx9d<%f96QpJPv|2x^C8@ethH|WVG%s#cMG~$g!f6nbvZ`G)c{9Cvqk=<VW``r&@|sg-8v8~w$g=~(CEv>(pZZ8)@ytD?1`v_j<8D#7jCUB8X&jwi<^_IPI>4ng4ut4tmL7z{lwT-L8++fq^+jC&H+_d)|0=9A6qd;PnztCy?J=mt_4xnt8wD!qtylsz!A<vbe202Z2E8b<7DfC0dBTjhI_gjX%=B=$FJu!qUob=>i<Sb?g<@U!+ydkABQKjK}`Ka*3-*l_@pdl+fx0-Z^L%xmfsS(?c$;d4)c+3oEbE2*`xwF%ubC?-el`75tGd-uQC5KB0Minu@;V<SEPPG^TF=o2wZ`*W$RyE9ghLMjwJgJ2p+v*;exBiYcSZ;(tT6`0jNu+7P`#()V??{u%vyV?oE{VM}s8|NX71XO+){=kGQYJ;esjw!_=%H<MMI9TH$2KE+~?P-Rvc#8HK_XyHE=GVXR!aR0HF2=k9~_2d5Yf4^7A@iTD4TM8{}+qCK3Gecr-$#BI|qdy9SI2GcWI<*fHS!Sb!gh!+yE-ta5!JQJ>nA8&6;2(S@}WW`~Dv@5Du3rf+51VDoA;aFb#@0~>DoGlHWCH&TE0xaFeC{^g(+<1QZ-MYrN7jV@ypLK$g?W(hi-^_U$8!b-;&YHezF~!USR&PG!l+jA}zbeQryNoKe&LjSHDa$LeFpvJa81dUEU<gA(PyP{Fm}aN<Dpo;<mHRTbQ<QaNKn)5U1!Db>?!xh|i-ThWr_wj6zs}!$CI!JFInEoXM2|g~R6^RsJDJq2q=YLO@-iTV_T6>Kl#X;neIq}V4B^UdCEog!)FgtvSkK#Dp=9rSB;Qv9Z<%!kG%RS1&J4f~{Jwe^!1QxiO)x9nyon-MfkS_Cju}tzv3;(8?2gU(7A`WwJg5d7;}(UX&q=D_SMc)7u+leekV{0*+p#4z$V^p*6b_UnO0^V{yEsG>_p2kmx+Fz;FQrE`jCK;9<7?R#?~Fp5Sn~Ody4wTz`VV}qRaLaGQac!<F0XF1PU;nnF6EL}LN``iiSJ)ge5}W)`6cPHNB}ZamSZp(^2nj+Lw*Gu<W(KFh2(>a*ca`M9zZlp@QZB&OnsxT(->WzpqskyLi3>tB{q+lEkN|JNoe_%$8sC`gqH%YpLnwEmNB&J3STz_hpZ*q`7vy97L|DCO<zu#K)7#JSl9VB|7ZfgHQ+%s!EnS+idZQ$cbRdZ$^Jl-nlBN+$q$2g4?$lW)q&jOth;n;vxyJ0fUen!h<bX?^9X8&@B?f(!u%E7>boxsPSsn3peCGQ(0e@2gJD6q$<4Fy&{Jt*npq2vCjj(Gz6>*cHb?hQ_>Pclo$fQI0fUs^W5sYZj<0cOAwP`H?7`q=U5cqu;8$2N5m8;-R`DGUBQ=)n_l;IWY21x(Un;daP0-_a00W{94hLZ|7@-=%sa5V#d@<gkv9yz^kaT~b;A)~2$0ci!<CGW1Ou+P~@*1H0fMg)?f}O*$a+3~*-NDdGRSOVI|1?rz71xPiPkqQT?s@7G0ytx#&K0NGQEzp_T0K~_Ss1_oq72`{ifPh}CTo1V+!U2<kq=CgOws(CLQRw0XEv&-_nuvepIz6@#(+o&$dmv_Ea0c~jp~0y<dPMJ&1HczrKJ;hC6}*Bgm~2wX>O?985owfn|1pRi@B;|7{KCY;*Q7fcIGCVFM@RTAP38DH%y{fta>1ewe`e6ohJA$Z;PZF;L0ZU+MET`1ACn*ex7q8DzHIUp`IDFih`lMhNw7j&h8m;Drrqm@i?}s+FXA)#)aBeOxz}953(<|W8jr#BxhbZ+}t<N6w4pi$AgE{#UT4gLU`Aj>%*BG741<(Uo-#!0-N_S0PPqI00FNu$EN}S*kfh&vBYQl0ssI200dcD'
words = lzma(b85decode(WORDS.encode()))
assert sha256(words).hexdigest() == '0c26059ed7ede977d7fa1c40443e71793e7850aa6a3d8aabf0cbcec91c1f95ec'
words = words.decode().split(' ')

polyseed_lang_en = {
    'name': '한국어',
    'name_en': 'Korean',
    'separator': ' ',
    'is_sorted': True,
    'has_prefix': False,
    'has_accents': False,
    'compose': True,
    'words': words
}