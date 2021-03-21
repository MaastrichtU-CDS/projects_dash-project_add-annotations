import requests

endpoint = "http://docker-graphdb-root-johan-graphdb.app.dsri.unimaas.nl/repositories/Maastricht/statements"

query1 = """
PREFIX db: <http://localhost/rdf/ontology/>
PREFIX dbo: <http://um-cds/ontologies/databaseontology/>
PREFIX roo: <http://www.cancerdata.org/roo/>
PREFIX ncit: <http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX map: <http://172.20.10.14/rdf/data/triplifier_test_HN_Maastricht/>

INSERT  
    {
    
    GRAPH <http://annotation.local/>
    {
    
     db:triplifier_test_HN_Maastricht.years rdf:type owl:Class.  
   
     db:triplifier_test_HN_Maastricht.years rdfs:label "Years".
    
     db:triplifier_test_HN_Maastricht.days rdf:type owl:Class.
    
     db:triplifier_test_HN_Maastricht.days rdfs:label "Days".
    
     db:triplifier_test_HN_Maastricht.Gray rdf:type owl:Class. 
  
     db:triplifier_test_HN_Maastricht.Gray rdfs:label "Gy".
   
     db:triplifier_test_HN_Maastricht.radiotherapyClass rdf:type owl:Class.
    
     db:triplifier_test_HN_Maastricht.radiotherapyClass dbo:table db:triplifier_test_HN_Maastricht.
    
     db:triplifier_test_HN_Maastricht.radiotherapyClass rdfs:label "Radiotherapy".
     
     db:triplifier_test_HN_Maastricht.neoplasmClass rdf:type owl:Class. 
     
     db:triplifier_test_HN_Maastricht.neoplasmClass dbo:table db:triplifier_test_HN_Maastricht.
    
     db:triplifier_test_HN_Maastricht.neoplasmClass rdfs:label "Neoplasm".
    
     ?tablerow dbo:has_column ?neoplasm, ?radiotherapy.
    
     ?neoplasm rdf:type db:triplifier_test_HN_Maastricht.neoplasmClass.
    
     ?radiotherapy rdf:type db:triplifier_test_HN_Maastricht.radiotherapyClass.
  
}
}

where 
{
    BIND(IRI(CONCAT(str(?tablerow), "/neoplasm")) as ?neoplasm).
    
    BIND(IRI(CONCAT(str(?tablerow), "/radiotherapy")) as ?radiotherapy).
    
    ?tablerow rdf:type db:triplifier_test_HN_Maastricht.
   
}
        """

query2 = """
PREFIX db: <http://localhost/rdf/ontology/>
PREFIX dbo: <http://um-cds/ontologies/databaseontology/>
PREFIX roo: <http://www.cancerdata.org/roo/>
PREFIX ncit: <http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

INSERT 
{
    GRAPH <http://annotation.local/>
    {
        
	 ?tablerow roo:P100061 ?patientID.   #has_identifier
        
     ?tablerow roo:P100018 ?gender.		 #has_biological_sex
        
     ?tablerow roo:hasage ?age. 
    
     ?age roo:P100027 db:triplifier_test_HN_Maastricht.years.	
        
     ?tablerow roo:P100022 ?hpv.		 #has_finding
        
     ?tablerow roo:P100214 ?asa.		 #has_measurement
        
     ?tablerow roo:haswhostatus ?whostatus.   #has_WHO_status
        
     ?tablerow roo:P100029 ?neoplasm.
   
     ?neoplasm roo:P100244 ?tstage. 	 #has_T_stage
        
     ?neoplasm roo:P100242 ?nstage. 	 #has_N_stage
      
     ?neoplasm roo:P100241 ?mstage. 	 #has_M_stage
            
     ?neoplasm roo:P100219 ?ajcc. 		 #has_AJCC_stage
        
     ?neoplasm roo:P100202 ?tumour.		 #tumourSite
        
     ?neoplasm roo:P10032 ?metastasis. 	 #has_metastasis
        
     ?neoplasm roo:P100022 ?eventrecurrence, ?eventrecurrencedays, ?localrecurrence, ?localrecurrencedays, ?regionalrecurrence, ?regionalrecurrencedays, ?metastasisdays.  #has_finding
        
     ?localrecurrencedays roo:P100027 db:triplifier_test_HN_Maastricht.days.
        
     ?regionalrecurrencedays roo:P100027 db:triplifier_test_HN_Maastricht.days.
        
     ?metastasisdays roo:P100027 db:triplifier_test_HN_Maastricht.days.
        
     ?tablerow roo:P100403 ?radiotherapy. #treated_by 
        
     ?radiotherapy roo:P100027 ?rttotaldays. #has_unit
        
     ?rttotaldays roo:P100027 db:triplifier_test_HN_Maastricht.days.
        
     ?radiotherapy roo:P100023 ?graytotaldose. #has_dose
        
     ?graytotaldose roo:P100027 db:triplifier_test_HN_Maastricht.Gray.
        
     ?radiotherapy roo:P100214 ?graydoseperfraction.   #has_dose_per_fraction
     
     ?graydoseperfraction roo:P100027 db:triplifier_test_HN_Maastricht.Gray.
    
     ?radiotherapy roo:has ?rtfractions.
      
     ?tablerow roo:P100403 ?surgery.     #treated_by
     
     ?tablerow roo:P100254 ?survival.    #has_death_finding 
        
     ?tablerow roo:has ?overallsurvivaldays.
        
     ?overallsurvivaldays roo:P100027 db:triplifier_test_HN_Maastricht.days.
        
     ?tablerow roo:C94626 ?chemo.        #chemo_administered
      
        
     db:triplifier_test_HN_Maastricht owl:equivalentClass ncit:C16960.
        
     db:triplifier_test_HN_Maastricht.id owl:equivalentClass ncit:C25364.
        
     db:triplifier_test_HN_Maastricht.biological_sex owl:equivalentClass ncit:C28421.
        
     db:triplifier_test_HN_Maastricht.age_at_diagnosis owl:equivalentClass roo:C100003.
    
     db:triplifier_test_HN_Maastricht.overall_hpv_p16_status owl:equivalentClass ncit:C14226.
        
     db:triplifier_test_HN_Maastricht.pretreat_hb_in_mmolperlitre owl:equivalentClass roo:asaScore.
        
     db:triplifier_test_HN_Maastricht.performance_status_ecog owl:equivalentClass ncit:C105721.
        
     db:triplifier_test_HN_Maastricht.clin_t owl:equivalentClass ncit:C48885.
     
     db:triplifier_test_HN_Maastricht.clin_n owl:equivalentClass ncit:C48884.

	 db:triplifier_test_HN_Maastricht.clin_m owl:equivalentClass ncit:C48883.
        
     db:triplifier_test_HN_Maastricht.ajcc_stage owl:equivalentClass ncit:C38027.
        
     db:triplifier_test_HN_Maastricht.cancer_surgery_performed owl:equivalentClass ncit:C17173.
      
     db:triplifier_test_HN_Maastricht.index_tumour_location owl:equivalentClass ncit:C3263.
    
     db:triplifier_test_HN_Maastricht.event_recurrence_metastatic_free_survival owl:equivalentClass roo:eventrecurrence.
    
     db:triplifier_test_HN_Maastricht.recurrence_metastatic_free_survival_in_days owl:equivalentClass roo:eventrecurrencedays.
                
     db:triplifier_test_HN_Maastricht.event_local_recurrence owl:equivalentClass roo:localrecurrence.

	 db:triplifier_test_HN_Maastricht.local_recurrence_in_days owl:equivalentClass roo:localrecurrencedays.

	 db:triplifier_test_HN_Maastricht.event_locoregional_recurrence owl:equivalentClass roo:regionalrecurrence.

	 db:triplifier_test_HN_Maastricht.locoregional_recurrence_in_days owl:equivalentClass roo:regionalrecurrencedays.
        
     db:triplifier_test_HN_Maastricht.event_distant_metastases owl:equivalentClass ncit:C19151.
               
     db:triplifier_test_HN_Maastricht.distant_metastases_in_days owl:equivalentClass roo:metastasisdays.
        
     db:triplifier_test_HN_Maastricht.event_overall_survival owl:equivalentClass ncit:C25717.

	 db:triplifier_test_HN_Maastricht.overall_survival_in_days owl:equivalentClass roo:overallsurvivaldays.
        
     db:triplifier_test_HN_Maastricht.chemotherapy_given owl:equivalentClass ncit:C15632.
    
     db:triplifier_test_HN_Maastricht.radiotherapy_total_treat_time owl:equivalentClass roo:rttotaldays.
    
     db:triplifier_test_HN_Maastricht.radiotherapy_refgydose_total_highriskgtv owl:equivalentClass roo:graytotaldose.
        
     db:triplifier_test_HN_Maastricht.radiotherapy_refgydose_perfraction_highriskgtv owl:equivalentClass roo:graydoseperfraction.
    
    db:triplifier_test_HN_Maastricht.radiotherapy_number_fractions_highriskgtv owl:equivalentClass roo:rttotalfraction.
   
     db:triplifier_test_HN_Maastricht.years owl:equivalentClass ncit:C29848.
      
     db:triplifier_test_HN_Maastricht.days owl:equivalentClass ncit:C25301. 
    
     db:triplifier_test_HN_Maastricht.Gray owl:equivalentClass ncit:C18063.
    
     db:triplifier_test_HN_Maastricht.neoplasmClass owl:equivalentClass ncit:C3262.
    
     db:triplifier_test_HN_Maastricht.radiotherapyClass owl:equivalentClass ncit:C15313.
    
     dbo:has_value owl:sameAs roo:P100042.    #has_value
    
     dbo:has_unit owl:sameAs roo:P100047.    #has_value
       
    } 
}
  

WHERE

{  
    ?tablerow rdf:type db:triplifier_test_HN_Maastricht.
    
	?tablerow dbo:has_column ?patientID, ?gender, ?age, ?tumour, ?whostatus, ?hpv, ?tstage, ?nstage, ?mstage, ?ajcc, ?asa, ?surgery, ?chemo, ?rttotaldays, ?graytotaldose, ?graydoseperfraction, ?survival, ?overallsurvivaldays, ?localrecurrence, ?localrecurrencedays, ?regionalrecurrence, ?regionalrecurrencedays, ?metastasis, ?metastasisdays, ?neoplasm, ?radiotherapy, ?rtfractions, ?eventrecurrence, ?eventrecurrencedays.
          
    ?neoplasm rdf:type db:triplifier_test_HN_Maastricht.neoplasmClass.
    
    ?radiotherapy rdf:type db:triplifier_test_HN_Maastricht.radiotherapyClass. 
    
    ?patientID rdf:type db:triplifier_test_HN_Maastricht.id. 
 
    ?gender rdf:type db:triplifier_test_HN_Maastricht.biological_sex.
    
    ?age rdf:type db:triplifier_test_HN_Maastricht.age_at_diagnosis.
    
    ?tumour rdf:type db:triplifier_test_HN_Maastricht.index_tumour_location.
    
    ?whostatus rdf:type db:triplifier_test_HN_Maastricht.performance_status_ecog.
    
    ?hpv rdf:type db:triplifier_test_HN_Maastricht.overall_hpv_p16_status.
    
    ?tstage rdf:type db:triplifier_test_HN_Maastricht.clin_t.
    
    ?nstage rdf:type db:triplifier_test_HN_Maastricht.clin_n.
    
    ?mstage rdf:type db:triplifier_test_HN_Maastricht.clin_m.
    
    ?ajcc rdf:type db:triplifier_test_HN_Maastricht.ajcc_stage.
    
    ?asa rdf:type db:triplifier_test_HN_Maastricht.pretreat_hb_in_mmolperlitre.
    
    ?surgery rdf:type db:triplifier_test_HN_Maastricht.cancer_surgery_performed.
    
    ?chemo rdf:type db:triplifier_test_HN_Maastricht.chemotherapy_given.
    
    ?rttotaldays rdf:type db:triplifier_test_HN_Maastricht.radiotherapy_total_treat_time.
        
    ?graytotaldose rdf:type db:triplifier_test_HN_Maastricht.radiotherapy_refgydose_total_highriskgtv.
        
    ?graydoseperfraction rdf:type db:triplifier_test_HN_Maastricht.radiotherapy_refgydose_perfraction_highriskgtv.
    
    ?rtfractions rdf:type db:triplifier_test_HN_Maastricht.radiotherapy_number_fractions_highriskgtv.
        
    ?survival rdf:type db:triplifier_test_HN_Maastricht.event_overall_survival.
        
    ?overallsurvivaldays rdf:type db:triplifier_test_HN_Maastricht.overall_survival_in_days.
    
    ?eventrecurrence rdf:type db:triplifier_test_HN_Maastricht.event_recurrence_metastatic_free_survival.
        
    ?eventrecurrencedays rdf:type db:triplifier_test_HN_Maastricht.recurrence_metastatic_free_survival_in_days.
        
    ?localrecurrence rdf:type db:triplifier_test_HN_Maastricht.event_local_recurrence.
        
    ?localrecurrencedays rdf:type db:triplifier_test_HN_Maastricht.local_recurrence_in_days.
    
    ?regionalrecurrence rdf:type db:triplifier_test_HN_Maastricht.event_locoregional_recurrence.
    
    ?regionalrecurrencedays rdf:type db:triplifier_test_HN_Maastricht.locoregional_recurrence_in_days.
        
    ?metastasis rdf:type db:triplifier_test_HN_Maastricht.event_distant_metastases.
        
    ?metastasisdays rdf:type db:triplifier_test_HN_Maastricht.distant_metastases_in_days.
 
}

"""
def runQuery1(endpoint, query1):
    annotationResponse = requests.post(endpoint,
                                   data="update=" + query1,
                                   headers={
                                       "Content-Type": "application/x-www-form-urlencoded",
                                       # "Accept": "application/json"
                                   })
    output = annotationResponse.text
    print(output)

def runQuery2(endpoint, query2):
    annotationResponse = requests.post(endpoint,
                                       data="update=" + query2,
                                       headers={
                                           "Content-Type": "application/x-www-form-urlencoded",
                                           # "Accept": "application/json"
                                       })
    output = annotationResponse.text
    print(output)

runQuery1(endpoint, query1)
runQuery2(endpoint, query2)

def addMapping(localTerm, targetClass, superClass):
    query = """
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            INSERT {
                GRAPH <http://annotation.local/> {
                    ?term owl:equivalentClass [
                        rdf:type owl:Class;
                        owl:intersectionOf [
                            rdf:first ?superClass;
                            rdf:rest [
                                rdf:first [
                                    rdf:type owl:Class;
                                    owl:unionOf [
                                        rdf:first [
                                            rdf:type owl:Restriction;
                                            owl:hasValue ?localValue;
                                            owl:onProperty <http://um-cds/ontologies/databaseontology/has_value>;
                                        ];
                                        rdf:rest rdf:nil;
                                    ]
                                ];
                                rdf:rest rdf:nil;
                            ]
                        ]
                    ].
                }
            } WHERE { 
                BIND(<%s> AS ?term).
                BIND(<%s> AS ?superClass).
                BIND("%s"^^xsd:string AS ?localValue).

            }
            """ % (targetClass, superClass, localTerm)

    annotationResponse = requests.post(endpoint,
                                       data="update=" + query,
                                       headers={
                                           "Content-Type": "application/x-www-form-urlencoded"
                                       })
    print(annotationResponse.status_code)


# T stage
addMapping("0", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48719",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48885")
addMapping("1", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48720",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48885")
addMapping("2", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48724",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48885")
addMapping("3", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48728",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48885")
addMapping("4", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48732",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48885")
# addMapping("T4b", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48732", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48885")


# N stage
addMapping("0", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48705",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48884")
addMapping("1", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48706",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48884")
addMapping("2", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48786",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48884")
# addMapping("N2b", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48786", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48884")
# addMapping("N2c", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48786", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48884")
addMapping("3", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48714",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48884")

# M stage
addMapping("0", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48699",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48883")
addMapping("1", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48700",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48883")

# gender
addMapping("female", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C16576",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C28421")
addMapping("male", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C20197",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C28421")

# survival
addMapping("1", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C28554",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C25717")
addMapping("0", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C37987",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C25717")
# 0=alive
# 1=dead

# tumorlocation
addMapping("oropharynx", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C12762",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C3263")
addMapping("larynx", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C12420",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C3263")
# addMapping("hypopharynx", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C12246", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C3263")
# addMapping("nasopharynx", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C12423", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C3263")
# addMapping("Base of tongue", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C12762", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C3263")
# addMapping("Tonsil", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C12762", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C3263")
# addMapping("Soft palate", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C12762", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C3263")
# addMapping("Glossopharyngeal sulcus", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C12762", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C3263")

# WHOstatus
addMapping("0", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C105722",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C105721")
addMapping("1", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C105723",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C105721")

# hpv
addMapping("positive", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C128839",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C14226")
addMapping("negative", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C131488",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C14226")

# ajcc
addMapping("i", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C27966",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C38027")
addMapping("ii", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C28054",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C38027")
addMapping("iii", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C27970",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C38027")
addMapping("iva", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C27971",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C38027")
addMapping("ivb", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C27971",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C38027")
addMapping("ivc", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C27971",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C38027")

# chemo
addMapping("concomitant", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C94626",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C15632")
addMapping("none", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C15313",
           "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C15632")
# addMapping("chemo radiation", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C94626", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C15632")
# addMapping("Concurrent chemoradiotherapy", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C94626", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C15632")
# addMapping("Induction chemotherapy+Radiation alone", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C94626", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C15632")
# addMapping("Induction chemotherapy + concurrent chemoradiotherapy", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C94626", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C15632")
