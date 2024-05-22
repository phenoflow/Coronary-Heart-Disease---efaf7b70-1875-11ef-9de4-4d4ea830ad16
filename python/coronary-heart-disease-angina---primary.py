# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"G311300","system":"readv2"},{"code":"14AJ.00","system":"readv2"},{"code":"8B27.00","system":"readv2"},{"code":"G33z600","system":"readv2"},{"code":"G311200","system":"readv2"},{"code":"G311.14","system":"readv2"},{"code":"G331.00","system":"readv2"},{"code":"G330000","system":"readv2"},{"code":"4139PA","system":"readv2"},{"code":"4139M","system":"readv2"},{"code":"4139N","system":"readv2"},{"code":"4139AT","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('coronary-heart-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["coronary-heart-disease-angina---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["coronary-heart-disease-angina---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["coronary-heart-disease-angina---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
