import csv
import pickle
from collections import OrderedDict
from positions import QB, WR, HB, TE, K

with open('../data/Initial export/players.csv', 'r') as csv_file:
    player_list = []
    reader = csv.DictReader(csv_file)
    for row in reader:
        od = OrderedDict()
        if row.get('position') == 'QB' or row.get('position') == 'HB' or row.get('position') == 'WR' or row.get(
                'position') == 'TE' or row.get('position') == 'K':
            # if row.get('lastName') == 'Perriman' :

            od["Name"] = row.get("firstName") + " " + row.get("lastName")
            od["Position"] = row.get("position")
            od["Team"] = row.get("team")
            od["Age"] = int(row.get("age"))
            od["Health Rating"] = int(row.get("injuryRating"))

            qbOVR = ((.01 * float(row.get('accelRating'))) + (.16 * float(row.get('awareRating'))) + (
                    .08 * float(row.get('playActionRating'))) + (.1 * float(row.get('speedRating'))) + (
                             .15 * float(row.get('throwAccDeepRating'))) + (
                             .15 * float(row.get('throwAccMidRating'))) + (
                             .12 * float(row.get('throwAccShortRating'))) + (
                             .03 * float(row.get('throwOnRunRating'))) + (
                             .15 * float(row.get('throwPowerRating'))) + (
                             .05 * float(row.get('throwUnderPressureRating'))))
            hbOVR = ((.1 * float(row.get('accelRating'))) + (.12 * float(row.get('awareRating'))) + (
                    .11 * float(row.get('bCVRating'))) + (.01 * float(row.get('cITRating'))) + (
                             .13 * float(row.get('carryRating'))) + (.06 * float(row.get('catchRating'))) + (
                             .1 * float(row.get('changeOfDirectionRating'))) + (
                             .08 * float(row.get('jukeMoveRating'))) + (.01 * float(row.get('releaseRating'))) + (
                             .01 * float(row.get('routeRunMedRating'))) + (
                             .01 * float(row.get('routeRunShortRating'))) + (
                             .09 * float(row.get('speedRating'))) + (.08 * float(row.get('spinMoveRating'))) + (
                             .02 * float(row.get('stiffArmRating'))) + (.02 * float(row.get('strengthRating'))) + (
                             .05 * float(row.get('truckRating'))))
            wrOVR = ((.06 * float(row.get('accelRating'))) + (.1 * float(row.get('awareRating'))) + (
                    .02 * float(row.get('bCVRating'))) + (.1 * float(row.get('cITRating'))) + (
                             .03 * float(row.get('carryRating'))) + (.11 * float(row.get('catchRating'))) + (
                             .08 * float(row.get('changeOfDirectionRating'))) + (
                             .03 * float(row.get('jukeMoveRating'))) + (.04 * float(row.get('jumpRating'))) + (
                             .08 * float(row.get('releaseRating'))) + (
                             .05 * float(row.get('routeRunDeepRating'))) + (
                             .05 * float(row.get('routeRunMedRating'))) + (
                             .05 * float(row.get('routeRunShortRating'))) + (
                             .03 * float(row.get('specCatchRating'))) + (.12 * float(row.get('speedRating'))) + (
                             .03 * float(row.get('spinMoveRating'))) + (.02 * float(row.get('strengthRating'))))
            teOVR = ((.03 * float(row.get('accelRating'))) + (.12 * float(row.get('awareRating'))) + (
                    .01 * float(row.get('bCVRating'))) + (.13 * float(row.get('cITRating'))) + (
                             .03 * float(row.get('carryRating'))) + (.12 * float(row.get('catchRating'))) + (
                             .03 * float(row.get('changeOfDirectionRating'))) + (
                             .01 * float(row.get('jukeMoveRating'))) + (.04 * float(row.get('jumpRating'))) + (
                             .08 * float(row.get('releaseRating'))) + (
                             .05 * float(row.get('routeRunDeepRating'))) + (
                             .06 * float(row.get('routeRunMedRating'))) + (
                             .06 * float(row.get('routeRunShortRating'))) + (
                             .05 * float(row.get('specCatchRating'))) + (.1 * float(row.get('speedRating'))) + (
                             .01 * float(row.get('spinMoveRating'))) + (.02 * float(row.get('strengthRating'))) + (
                             .04 * float(row.get('truckRating'))))
            kOVR = ((.1 * float(row.get('awareRating'))) + (.45 * float(row.get('kickAccRating'))) + (
                    .45 * float(row.get('kickPowerRating'))))
            hbOVR -= (2 * int(row.get('dropOpenPassTrait')))
            hbOVR -= (int(row.get('dropOpenPassTrait')))
            wrOVR -= (2 * int(row.get('dropOpenPassTrait')))
            teOVR -= (2 * int(row.get('dropOpenPassTrait')))

            if row.get('position') == 'QB':
                od["Overall"] = round(qbOVR, 1)
                player = QB(od)
            if row.get('position') == 'HB':
                od["Overall"] = round(hbOVR, 1)
                player = HB(od)
            if row.get('position') == 'WR':
                od["Overall"] = round(wrOVR, 1)
                player = WR(od)
            if row.get('position') == 'TE':
                od["Overall"] = round(teOVR, 1)
                player = TE(od)
            if row.get('position') == 'K':
                od["Overall"] = round(kOVR, 1)
                player = K(od)
            print(od)
            player_list.append(player)
            print(player_list)

        else:
            continue
#rint(player_list)
#for i in player_list:
    #print(i.getOverall())

with open("../data/players.pkl", "wb") as output:
    pickle.dump(player_list, output)
