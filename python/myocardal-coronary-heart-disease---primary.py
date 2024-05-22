# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"G34y100","system":"readv2"},{"code":"G312.00","system":"readv2"},{"code":"G32..11","system":"readv2"},{"code":"G35..00","system":"readv2"},{"code":"G32..00","system":"readv2"},{"code":"G351.00","system":"readv2"},{"code":"G30X.00","system":"readv2"},{"code":"G30z.00","system":"readv2"},{"code":"G311011","system":"readv2"},{"code":"G30..17","system":"readv2"},{"code":"G364.00","system":"readv2"},{"code":"G304.00","system":"readv2"},{"code":"G306.00","system":"readv2"},{"code":"G31y300","system":"readv2"},{"code":"G30..13","system":"readv2"},{"code":"G32..12","system":"readv2"},{"code":"G353.00","system":"readv2"},{"code":"G301z00","system":"readv2"},{"code":"G311000","system":"readv2"},{"code":"G360.00","system":"readv2"},{"code":"G30y.00","system":"readv2"},{"code":"G30..00","system":"readv2"},{"code":"G30yz00","system":"readv2"},{"code":"G361.00","system":"readv2"},{"code":"G362.00","system":"readv2"},{"code":"G30B.00","system":"readv2"},{"code":"G301.00","system":"readv2"},{"code":"G365.00","system":"readv2"},{"code":"G305.00","system":"readv2"},{"code":"G344.00","system":"readv2"},{"code":"G35X.00","system":"readv2"},{"code":"G308.00","system":"readv2"},{"code":"G36..00","system":"readv2"},{"code":"G350.00","system":"readv2"},{"code":"G30..15","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('coronary-heart-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["myocardal-coronary-heart-disease---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["myocardal-coronary-heart-disease---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["myocardal-coronary-heart-disease---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
