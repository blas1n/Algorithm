SELECT
    sample_id,
    dna_sequence,
    species,
    IF(dna_sequence LIKE 'ATG%', 1, 0) as has_start,
    IF(dna_sequence LIKE '%TAA' or dna_sequence LIKE '%TAG' or dna_sequence LIKE '%TGA', 1, 0) as has_stop,
    IF(dna_sequence LIKE '%ATAT%', 1, 0) as has_atat,
    IF(dna_sequence LIKE '%GGG%', 1, 0) as has_ggg
FROM Samples