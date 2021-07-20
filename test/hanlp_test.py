# -*- encoding: utf-8 -*-
# @File:   hanlp_test.py    
# @Time: 2021/7/14 11:01 下午
# @Author: ZHANG
# @Description: hanlp_test

import re
import hanlp

from time import time
HanLP = hanlp.load(hanlp.pretrained.dep.CTB7_BIAFFINE_DEP_ZH)
HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH, tasks=['srl'])
text = "诊断依据：患者因“突发口齿含糊1天”入院。查体：BP：110/60mmHg。神清，精神尚可，颈软，无抵抗，脑膜刺激征（-）。呼吸平稳，双肺呼吸音清，未闻及明显干湿罗音，心率78次/分，律齐，未闻及心杂音。腹部平坦，未见腹壁静脉曲张，全腹质软，无压痛，无反跳痛，未扪及肿块，肝脾肋下未触及，肝颈返流征(-)，无移动性浊音，肝肾区无叩痛，肠鸣音不亢，无振水音，双下肢无浮肿。专科：眼睑无下垂，眼球活动不受限；眼球无震颤；无复视；双侧瞳孔圆形、等大、位置居中边缘整齐；对光反射正常。双侧额纹、眼裂对称，双侧鼻唇沟对称，闭目完全，粗测听力正常。发音含糊，伸舌居中，四肢肌力肌张力正常，指鼻试验、快速轮替试验、跟膝胫试验双侧正常，闭目难立(Romberg)征未查。躯干、肢体疼痛刺激正常，左侧腱反射++，右侧腱反射++，Babinski征：左侧（-），右侧（-）。2018-05-15 头颅MR：双侧基底节区、侧脑室旁及半卵圆区多发腔隙性脑梗死、缺血灶，老年性脑改变；符合空泡蝶鞍，请结合临床随访。根据患者病史、体征、头颅MR可诊断。"
s = re.sub(r'(。)', r'\1\n', text).rstrip('\n')
s = s.split('\n')
print(s)
s = [
    "肝肾区无叩痛，",
    "双下肢无浮肿。",
    "眼球无震颤；无复视；",
    "四肢关节无红肿",
    "患者无红肿",
    "淋巴结未扪及肿大",
    "脑CT体现脑病",
    "律齐，未闻及心杂音。"
     ]
start = time()
tree = HanLP(s)
print('用时：', time() - start, 's')  # 2.7s
tree.pretty_print()
print(tree)

