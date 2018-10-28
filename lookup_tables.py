
indexes = {
	"StartTime": 0 ,
	"Dur": 1 ,
	"Proto": 2 ,
	"SrcAddr": 3 ,
	"Sport": 4 ,
	"Dir": 5 ,
	"DstAddr": 6 ,
	"Dport": 7 ,
	"State": 8 ,
	"sTos": 9 ,
	"dTos": 10 ,
	"TotPkts": 11 ,
	"TotBytes": 12 ,
	"SrcBytes": 13 ,
	"Label": 14 
}

direction = {
	"   ->": 1,
	"   ?>": 2,
	"  <?>": 3,
	"  <->": 4,
	"  <-": 5,
	"  who": 6,
	"  <?": 7
}

proto = {
	"tcp": 1 , 
	"udp": 2 , 
	"icmp": 3 , 
	"esp": 4 , 
	"rtp": 5 , 
	"arp": 6 ,
	"igmp": 7 , 
	"ipx/spx": 8 ,
	"rtcp": 9 ,
	"pim" : 10 ,
	"ipv6-icmp": 11 , 
	"udt": 12 ,
	"ipv6": 13 ,
	"rsvp": 14 ,
	"rarp": 15 ,
	"gre": 16 ,
	"unas": 17 ,
	"ipnip": 18 ,
	"llc" : 19
}

#hardcoded flags
expand_state_flag = False
state_count = 379

state = {'SRA_SA': 0, 'SR_SA': 1, 'S_RA': 2, 'SR_A': 3, 'SRA_FSA': 4, 'SRPA_FSPA': 5, 'SRPA_FSRPA': 6, 'SA_FSA': 7, 'R_': 8, 'SRPA_SPA': 9, 'FSRPA_FSPA': 10, 'FSPA_SRA': 11, 'FSPA_FSRA': 12, 'CON': 13, 'RPA_PA': 14, 'INT': 15, 'PA_PA': 16, 'FPA_FA': 17, 'FPA_FPA': 18, 'A_PA': 19, 'FSPA_FSPA': 20, 'PA_RPA': 21, 'FPA_': 22, 'RA_FA': 23, 'FRPA_FPA': 24, 'FPA_FRPA': 25, 'RPA_FPA': 26, 'FA_FA': 27, 'RA_FPA': 28, 'RSP': 29, 'FSPA_FSA': 30, 'FSPA_FSRPA': 31, 'PA_A': 32, 'URH': 33, 'URP': 34, '_FSPA': 35, 'RED': 36, 'FA_A': 37, 'SA_': 38, 'SPA_SRPA': 39, 'FA_R': 40, 'FRPA_PA': 41, 'URFIL': 42, 'FA_': 43, 'NRS': 44, 'FSA_FSA': 45, 'S_': 46, 'TXD': 47, 'PA_FSPA': 48, 'PA_R': 49, 'SPA_FSPA': 50, 'A_': 51, 'RA_': 52, 'FRA_FA': 53, 'FPA_FPAC': 54, 'FA_FRA': 55, 'A_A': 56, 'S_SA': 57, 'FA_FPA': 58, 'PA_FPA': 59, 'FSRPA_SPA': 60, 'RPA_RPA': 61, 'FPA_FRPAC': 62, 'SRC': 63, 'FSPA_SPA': 64, 'PA_RA': 65, 'ECO': 66, 'FRPA_FA': 67, 'FA_RA': 68, 'FPA_RA': 69, 'FPA_RPA': 70, 'SA_R': 71, 'FPA_PA': 72, 'RPA_FA': 73, 'FPA_A': 74, 'ECR': 75, 'FRPA_RPA': 76, 'SPA_SPA': 77, 'SRPA_SA': 78, 'FPA_R': 79, 'SA_SRA': 80, 'PA_': 81, '_SPA': 82, 'FRA_': 83, 'URN': 84, 'FSRPAC_FSPA': 85, 'FSPAC_FSPA': 86, 'SPA_FSRA': 87, 'PA_PAC': 88, 'FRPAC_FPA': 89, 'A_R': 90, 'SRA_': 91, 'FSA_SRA': 92, 'SPA_FSRPA': 93, 'FRPA_FRPA': 94, 'SR_': 95, 'FS_SA': 96, 'URHPRO': 97, 'FSRPA_FSRPA': 98, 'SA_RA': 99, 'FRPA_': 100, 'FRA_A': 101, 'NNS': 102, 'FSA_FSPA': 103, 'FS_': 104, 'FSA_FSRA': 105, 'FRA_R': 106, 'FSPA_SRPA': 107, 'FSPA_SA': 108, 'FSPAC_FSRA': 109, 'FSRPA_SRPA': 110, 'URO': 111, 'SRA_RA': 112, 'S_FSPA': 113, 'SPA_SRA': 114, 'FSAU_FSA': 115, 'FSRA_FSPA': 116, 'FSAU_FSRA': 117, 'SPAC_FSPA': 118, 'FSRPA_SA': 119, 'SPA_SA': 120, 'SPAC_SPA': 121, 'SRA_FSPA': 122, 'RPA_R': 123, 'SPA_RPA': 124, 'S_R': 125, 'FSRA_FSA': 126, 'SPA_FSA': 127, 'URF': 128, 'FSRA_SPA': 129, 'FSR_SA': 130, 'SRPA_FSA': 131, 'FSRPA_SRA': 132, 'FSPAC_FSRPA': 133, 'FSRPA_FSA': 134, 'SRA_SRA': 135, 'FSPA_FRA': 136, 'FSA_FPA': 137, 'FSPA_FPA': 138, 'FPA_FSPA': 139, 'FSPA_FSPAC': 140, 'SRE_': 141, 'FSRPA_FSRA': 142, 'FSRPAEC_FSPA': 143, 'FSRAEC_FSPA': 144, 'SA_FSPA': 145, 'SREC_SA': 146, 'SRPA_SRPA': 147, 'SPAC_FSRPA': 148, 'FRPA_FSPA': 149, 'RPA_SPA': 150, 'FSA_SA': 151, 'FSRPAC_SPA': 152, 'A_FA': 153, 'FSPAEC_FSPA': 154, 'SRPA_PA': 155, 'S_SRA': 156, 'FSRAU_FSA': 157, 'FSRA_SA': 158, '_SA': 159, 'FSRA_FSRA': 160, 'SRPAC_SPA': 161, 'FSA_FA': 162, 'FA_FSA': 163, 'SA_RPA': 164, 'SRPA_FPA': 165, 'FPA_FSRPA': 166, 'SEC_': 167, 'S_RPA': 168, 'SPAC_SRPA': 169, 'FSRA_SRA': 170, 'REQ': 171, 'RPA_A': 172, 'SA_FR': 173, 'SPAEC_FSRPA': 174, 'RPA_FRPA': 175, 'SEC_RA': 176, 'FSRAUC_SA': 177, 'SRPA_FSPAC': 178, 'FSA_': 179, '_PA': 180, 'S_FRA': 181, 'FRE_': 182, 'FSRPAC_FSRPA': 183, 'S_SPA': 184, 'SA_FSRA': 185, 'SA_SA': 186, 'PA_SA': 187, 'RA_PA': 188, 'SRA_SPA': 189, 'FSPAC_SRPA': 190, 'SRA_R': 191, 'S_A': 192, 'FSPAC_FSA': 193, 'SA_SRPA': 194, 'A_FRA': 195, 'SRPA_SRA': 196, 'SA_FSRPA': 197, 'F_': 198, 'SA_FA': 199, 'FSPA_FSRPAC': 200, 'PA_FRA': 201, 'FSPA_SRAC': 202, '_RA': 203, 'FPA_FRA': 204, 'FSRPAC_SRPA': 205, '_SRPA': 206, 'RPA_FSPA': 207, 'SPA_': 208, 'FAU_R': 209, 'RA_A': 210, 'PA_SRPA': 211, 'FRA_FPA': 212, 'SR_RA': 213, 'FSRA_': 214, 'MRQ': 215, 'FSRPA_FSRPAC': 216, 'SR_SRA': 217, 'FSR_': 218, 'FRA_PA': 219, 'A_RA': 220, 'SRPA_FSRA': 221, 'PA_FRPA': 222, 'SRA_FSRA': 223, '_FSA': 224, 'SPAEC_SRPA': 225, 'SA_SPA': 226, 'FPA_SRPA': 227, 'FRPA_FRA': 228, 'RPA_': 229, '_SRA': 230, 'DCE': 231, 'SRA_PA': 232, 'SRA_FPA': 233, '': 234, 'IRQ': 235, 'RC_': 236, 'UNK': 237, 'R_FPA': 238, 'R_FA': 239, 'PAR': 234, 'S_FPA': 235, 'FA_FSPA': 236, 'FPA_SA': 237, 'PAC_PA': 238, 'FSPA_': 239, '_FRPA': 240, 'FSPA_PA': 241, 'RA_R': 242, 'TST': 243, 'SREC_SAE': 244, '_': 245, 'FSPU_': 246, 'FPU_': 247, 'MAS': 248, 'TSR': 249, 'RTA': 250, 'RTS': 251, 'State': 252, 'IRR': 253, 'MSR': 254, 'UR': 255, 'NRA': 256, 'SKP': 257, 'ROB': 258, 'AHA': 259, 'MRP': 260, 'TRC': 261, 'WAY': 262, 'SEC': 263, 'NNA': 264, 'MHR': 265, 'IAH': 266, 'PHO': 267, 'DNP': 268, 'FSPAC_FSPAC': 269, '_FPA': 270, 'FPAC_FRPA': 271, 'FA_FRPA': 272, 'PA_SPA': 273, 'FSPA_FA': 274, 'SRPA_FRPA': 275, 'RA_S': 276, 'FRPA_A': 277, 'FRA_RA': 278, 'FRA_RPA': 279, 'SRPA_': 280, 'RA_RA': 281, 'FPAC_FPA': 282, 'FSRA_FA': 283, 'A_RPA': 284, 'FSRAEC_SPA': 285, 'FSRAC_SPA': 286, '_FSRPA': 287, 'FSRPAE_FSPA': 288, '_RPA': 289, 'SRAEC_FSA': 290, 'SRPAC_FSPA': 291, 'SA_A': 292, 'FRA_FRPA': 293, 'A_FPA': 294, 'SPA_FA': 295, 'FRPA_FPAC': 296, 'SPA_R': 297, 'FSRPA_FSPAC': 298, 'FSPA_FRPA': 299, 'SRC_SA': 300, 'SRA_FA': 301, 'FSRPA_FPA': 302, 'FSPA_A': 303, 'RPA_FSA': 304, 'SEC_SA': 305, 'RPA_FSRPA': 306, 'FSAU_SRA': 307, 'FRPA_SPA': 308, 'RA_RPA': 309, 'SRPA_SPAC': 310, 'SPA_PA': 311, 'FSA_A': 312, 'FSPAC_SRA': 313, 'SRAE_RA': 314, 'PA_FA': 315, 'FA_PA': 316, 'SRE_SA': 317, 'A_RPE': 318, 'RPA_RA': 319, '_FA': 320, 'FRPA_R': 321, 'R_PA': 322, 'FSA_FSRPA': 323, 'SRPAC_SRPA': 324, 'SPAEC_SPA': 325, '_R': 326, 'FRPAC_PA': 327, 'A_FSPE': 328, 'FSAEC_FSPAE': 329, 'SR_FSA': 330, 'SRPAEC_FSPA': 331, 'SREC_': 332, 'SA_S': 333, 'FSAU_SA': 334, 'FSRPAC_FSRA': 335, 'FSPAEC_FSPAE': 336, 'FAU_': 337, 'FPA_SPA': 338, 'FPA_FSA': 339, 'S_RAC': 340, 'FSA_FRPA': 341, 'FSRPAC_FSA': 342, 'SR_FSPA': 343, 'URNPRO': 344, 'S_SRPA': 345, 'SA_FPA': 346, 'RA_FRPA': 347, 'SRC_': 348, 'SPA_FPA': 349, 'RPA_SRA': 350, 'RE_': 351, '_A': 352, 'FRA_FPAC': 353, 'FRA_FRA': 354, 'FSRPAEC_SPA': 355, 'SRAEC_SA': 356, 'DNQ': 357, 'PTB': 358, 'URNU': 359, 'URHTOS': 360, 'FSA_PA': 361, 'FSA_R': 362, 'RA_FRA': 363, 'FSRAE_FSA': 364, 'A_FRPE': 365, 'A_AE': 366, 'FSRAEC_FSA': 367, 'SRPAEC_SPA': 368, 'A_FSRPE': 369, 'SRA_FSRPA': 370, 'SPA_RA': 371, 'FSPAEC_FSA': 372, 'FSPAEC_FSRA': 373, 'RPAC_PA': 374, 'FPA_PAC': 375, 'FSPA_R': 376, 'SR_RPA': 377, 'FS_RA': 378}


