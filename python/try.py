
# # data = [
# #     {'Date': '10-11-2022', 'Description': 'IMPS/P2A/231417192935/XXXXXXXXXX6446/methu',
# #         'amount': '3005.90', 'type': 'DR'},
# #     {'Date': '10-11-2022', 'Description': 'IMPS/P2A/231417192935/XXXXXXXXXX6446/methu',
# #         'amount': '3005.90', 'type': 'CR'},
# #     {'Date': '10-11-2022', 'Description': 'IMPS/P2A/231417192935/XXXXXXXXXX6446/methu',
# #         'amount': '3005.90', 'type': 'CR'},

# #     {'Date': '11-11-2022', 'Description': 'IMPS/P2A/231417192935/XXXXXXXXXX6446/methu',
# #         'amount': '3005.90', 'type': 'CR'},
# #     {'Date': '11-11-2022', 'Description': 'IMPS/P2A/231417192935/XXXXXXXXXX6446/methu',
# #         'amount': '3005.90', 'type': 'CR'},

# #     {'Date': '05-11-2022', 'Description': '09530100026966:Int.Pd:01-08-2022 to 31-10-2022',
# #         'amount': '7.00', 'type': 'CR'},
# #     {'Date': '11-10-2022', 'Description': 'UPI/228422570101/18:25:51/UPI/suriya740227-1@okax',
# #         'amount': '15.00', 'type': 'CR'},
# #     {'Date': '06-10-2022', 'Description': 'UPI/227989221739/14:46:16/UPI/dmdakshesh@oksbi/UP',
# #         'amount': '31.00', 'type': 'CR'},
# #     {'Date': '23-09-2022', 'Description': 'IMPS/P2A/226616401918/XXXXXXXXXX4918/dk',
# #         'amount': '502.95', 'type': 'DR'},
# #     {'Date': '23-09-2022', 'Description': 'UPI/226693761466/16:39:33/UPI/kesavhari2000@okici',
# #         'amount': '500.00', 'type': 'CR'},
# #     {'Date': '23-09-2022', 'Description': 'SMS Alert charges for Qtr Sep-22',
# #         'amount': '17.70', 'type': 'DR'},
# #     {'Date': '21-09-2022', 'Description': 'MBK/226440127774/18:43:49/',
# #         'amount': '19.00', 'type': 'DR'},
# # ]

# # # for d in data:

# # # if d['type'] == 'DR':


# # # dates = set()
# # # decs = set()
# # # amounts = set()

# # # for d in data:
# # #     target_date = d['Date']
# # #     target_desc = d['Description']
# # #     target_amount = d['amount']

# # #     # print(target_date)
# # #     if target_date not in dates:
# # #         decs.clear()
# # #         amounts.clear()

# # #         date_dicts = [transaction for transaction in data if transaction['Date'] == target_date]

# # #         sample_dicts = [ transaction for transaction in data if transaction['Date'] == target_date and
# # #                                                             transaction['Description'] == target_desc and
# # #                                                             transaction['amount'] == target_amount ]

# # #         if(len(sample_dicts) > 1):
# # #             # print(sample_dicts)

# # #             current_value = sample_dicts[0]
# # #             for i in range(len(sample_dicts)):
# # #                 next_value = sample_dicts[i+1] if i+1 < len(sample_dicts) else {}

# # #                 if len(next_value.keys()) > 0:
# # #                     print(current_value)
# # #                     print(next_value)
# # #                     print()

# # #                 current_value = next_value

# # #     amounts.add(target_amount)
# # #     decs.add(target_desc)
# # #     dates.add(target_date)

# # # current_value = sample_dicts[i+1]

# # # if(len(date_dicts) > 1):
# # #     # print(date_dicts)
# # #     # print('\n')
# # #     if target_desc not in decs:
# # #         desc_dicts = [transaction for transaction in date_dicts if transaction['Description'] == target_desc]
# # #         # print(desc_dicts)
# # #         # print('\n')

# # #         if(len(desc_dicts) > 1):
# # #             # print(desc_dicts)
# # #             # print('\n')

# # #             if target_amount not in amounts:
# # #                 amount_dicts = [transaction for transaction in desc_dicts if transaction['amount'] == target_amount]

# # #                 if(len(amount_dicts) > 1):
# # #                     for i in range(len(amount_dicts)):
# # #                         current_value = amount_dicts[i]
# # #                         next_value = amount_dicts[i+1] if i+1 < len(amount_dicts) else {}

# # #                         if len(next_value.keys()) > 0:
# # #                             # print(current_value)
# # #                             # print(next_value)
# # #                             print()

# # # if i+1 < len(amount_dicts):
# # #     print(i, i+1)
# # #     print('\n')

# # # pass

# # #                 amounts.add(target_amount)

# # #         decs.add(target_desc)

# # # dates.add(target_date)

# # # if d['Date'] == target_date:
# # #     description = d['Description']
# # #     if description in description_counts:
# # #         matching_dicts.append(d)
# # #     else:
# # #         description_counts[description] = 1


# # # for transaction in date_dicts:
# # #     print(transaction)

# # # print(description_counts)

# # # if d['Date'] not in dates: dates.append(d['Date'])
# # # else: pass

# # # specific = ['impbill']

# # # deduct_keywords = ['INS', 'INSURANCE', 'LIFE', 'HEALTH', 'PROVI', 'FUND', 'PF', 'PF', 'SCHL', 'SCHOOL', 'CLG', 'COLLEGE', 'UNIVERSITY', 'EDUCATIONAL INSTITUTE', 'EDU INST', 'STAMP DUTY', 'REGISTRATION FEES', 'STAMP', 'REGISTRAR OFFICE', 'PENSION', 'MONEY', 'MUTUAL', 'FUND',
# # #                    'ASSET', 'FINAN', 'LIFE', 'MEDI', 'HOSP', 'HOSPITAL', 'CHECKUP', 'BODYCHECKUP', 'SCAN', 'INT', 'EDU', 'FINAN', 'INSTITU', 'CHARITAB', 'DONATION', 'DONA', 'TRUST', 'HOME', 'RENT', 'INT', 'HOUSE LOAN', 'INTEREST', 'INTREST', 'ELECTRIC', 'VEHICLE', 'POLITICAL', 'PARTY']
# # # deduct_keyword_list = '|'.join(deduct_keywords)
# # # deduct_key_pattern = re.compile(
# # #     r'\b(?:' + deduct_keyword_list + r')\b', flags=re.IGNORECASE)



# # # krishna07.2750@okax x
# # # krishna072750@okax x
# # # 07.2750@okax /

# # # patt = re.compile(r'(?=.*[a-zA-Z]{3,})(?=.*\d{3,})[a-zA-Z\d.]+@.{3,}')
# # # match = re.findall(patt, input_string)
# # # print(match)


# # pattern = re.compile(r"\b[a-zA-Z\s@]{5,}\d*\b")
# # match = re.findall(pattern, input_string)
# # final = []
# # print(match)



# # def contains_keyword(string):
# #     result = key_pattern.search(string)
# #     print(result)

# #     if bool(result):
# #         final.append(string)


# # # for m in match:
# # contains_keyword(input_string)

# # if final:
# #     print(str(final[0]))

# # else:
# #     print(None)
# #     # if none returned
# #     pass

# import re
# input_string = 'UPI/306154472654/20:51:42/UPI/paytmqr281005050101'
# # input_string = 'WITHDRAWAL TRANSFER RENUGA K S/IDIBH22182470256/NEFT TRANSFEREE BANK IOBA TRANSFER TO 89634032894'


# import re
# keywords = [ 'ACCOUNT', 'neft', 'upi', 'imps', 'chq', 'rtgs', 'atm', 'coll', 'vps', 'transfer', 'paytm', 'transferee', 'to', 'from', 'by', 'depo', 'clearing', 'withdrawal', 'NEWCARDISSUE', 'impbill', 'trf', 'payment', 'chrgs', 'remit', 'bank', 'atm', 'ecom', 'pos', 'apbs', 'chg', 'cash',
#             'cheque', 'dd', 'eft', 'swift', 'web', 'net', 'liq', 'mobile', 'tfr', 'wdl', 'dep', 'deposit', 'tds', 'grant', 'emi', 'inst', 'installment', 'int', 'interest', 'pf', 'pension', 'deposit', 'closure', 'terminated', 'ins', 'insurance', 'refund', 'advtax', 'advancetax', 'bill']
# keyword_list = '|'.join(keywords)
# key_pattern = re.compile(r'\b(?:' + keyword_list + r')\b', flags=re.IGNORECASE)
# # input_string = 'UPI/236123350176/UPI/harishlive99-1@/Indian Overseas/ICIbd783772427f4cdab0 15a5ab128bd7c9/'
# input_string = "NEFT CR-YESB023802423-E-COLLECT ACCOUNT-K diwkaer"

# pattern = re.compile(r'(?=.*[a-zA-Z]{3,})(?=.*\d{3,})[a-zA-Z\d.]+@[a-zA-Z]{3,}')
# match = re.findall(pattern, input_string)

# if match == []:
#     pattern = re.compile(r"\b[a-zA-Z@\s]{5,}\d*\b")
#     match = re.findall(pattern, input_string)
#     print(match)

# if 'WITHDRAWAL TRANSFER' in match[0]:
#     print(match[0].replace('WITHDRAWAL TRANSFER ', ''))

# else:
#     for string in match:
#         pattern_result = key_pattern.search(string)
#         if not bool(pattern_result):
#             print(string)

# import re
# a = '2610007728.0\n0'

# pattern = re.compile(r'^\d+(\.\d*)?\n(?:[a-zA-Z]{0,2}|\d+)$')
# print(bool(pattern.match(a)))

# import re

# def contains_non_alphabet_substring(input_string, substrings):
    
#     for substring in substrings:
#         pattern = re.compile(rf'(?<![a-zA-Z]){re.escape(substring)}(?![a-zA-Z])', re.IGNORECASE)
#         if pattern.search(input_string):
#             return substring
        
#     return None


# main_string = "NEFT CR-YESB023802423-E-COLLECT ACCOUNT-K"
# substrings = ['CHARGES', 'CHG', 'BG CHARGES', 'CHRGS', 'FEE','MISC', 'MISC-REMIT', 'BULK']

# result = contains_non_alphabet_substring(main_string, substrings)

# if result:
#     print(f"The string contains a substring from the list.")
# else:
#     print(f"The string does not contain any substring from the list.")


a = '1223754694.72'

print(float(a))