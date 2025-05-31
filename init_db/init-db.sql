-- Wstaw pytania do tabeli Survey
INSERT INTO users_survey (id, question)
VALUES
    (1, 'Co Cię bardziej interesuje?'),
    (2, 'Co Cię bardziej interesuje?'),
    (3, 'Co Cię bardziej interesuje?'),
    (4, 'Co Cię bardziej interesuje?'),
    (5, 'Co Cię bardziej interesuje?'),
    (6, 'Co Cię bardziej interesuje?'),
    (7, 'Co Cię bardziej interesuje?'),
    (8, 'Co Cię bardziej interesuje?'),
    (9, 'Co Cię bardziej interesuje?'),
    (10, 'Co Cię bardziej interesuje?'),
    (11, 'Co Cię bardziej interesuje?');

INSERT INTO users_department (id, name)
VALUES (1, 'Wydział Lekarski i Nauk o Zdrowiu'),
       (2, 'Wydział Nauk Inżynieryjno-Technicznych'),
       (3, 'Wydział Nauk Prawnych i Ekonomicznych'),
       (4, 'Wydział Nauk Społecznych'),
       (5, 'Wydział Nauk Ścisłych i Przyrodniczych'),
       (6, 'Wydział Humanistyczny'),
       (7, 'Wydział Artystyczny');

INSERT INTO users_departmentinterest (department_id, interest_id)
VALUES
    (1, 13),  -- Biologia i zdrowie
    (1, 4),   -- Pomoc i praca z ludźmi
    (1, 14),  -- Sport i dietetyka

    (2, 9),   -- Automatyka i technologie przemysłowe
    (2, 18),  -- Produkcja i inżynieria systemowa
    (2, 12),  -- Informatyka i dane
    (2, 1),   -- Projektowanie
    (2, 21),  -- Ochrona środowiska

    (3, 6),   -- Prawo i administracja
    (3, 2),   -- Ekonomia i Finanse
    (3, 8),   -- Zarządzanie i logistyka
    (3, 10),  -- Polityka i bezpieczeństwo

    (4, 4),   -- Pomoc i praca z ludźmi
    (4, 20),  -- Psychologia i emocje
    (4, 19),  -- Projektowanie społeczne i kampanie
    (4, 10),  -- Polityka i bezpieczeństwo

    (5, 3),   -- Nauki przyrodnicze i eksperymenty
    (5, 12),  -- Informatyka i dane
    (5, 11),  -- Astronomia i kosmos
    (5, 13),  -- Biologia i zdrowie
    (5, 22),  -- Fizyka i matematyka
    (5, 21),  -- Ochrona środowiska
    (5, 14),  -- Sport i dietetyka

    (6, 5),   -- Języki i kultura
    (6, 7),   -- Media i komunikacja
    (6, 16),  -- Literatura i filozofia
    (6, 17),  -- Gry i kreacja narracji

    (7, 15);  -- Sztuki wizualne i muzyka

-- Wstaw zainteresowania do tabeli Interest
INSERT INTO users_interest (id, name)
VALUES
    (1, 'Projektowanie'),
    (2, 'Ekonomia i Finanse'),
    (3, 'Nauki przyrodnicze i eksperymenty'),
    (4, 'Pomoc i praca z ludźmi'),
    (5, 'Języki i kultura'),
    (6, 'Prawo i administracja'),
    (7, 'Media i komunikacja'),
    (8, 'Zarządzanie i logistyka'),
    (9, 'Automatyka i technologie przemysłowe'),
    (10, 'Polityka i bezpieczeństwo'),
    (11, 'Astronomia i kosmos'),
    (12, 'Informatyka i dane'),
    (13, 'Biologia i zdrowie'),
    (14, 'Sport i dietetyka'),
    (15, 'Sztuki wizualne i muzyka'),
    (16, 'Literatura i filozofia'),
    (17, 'Gry i kreacja narracji'),
    (18, 'Produkcja i inżynieria systemowa'),
    (19, 'Projektowanie społeczne i kampanie'),
    (20, 'Psychologia i emocje'),
    (21, 'Ochrona środowiska'),
    (22, 'Fizyka i matematyka');

-- Powiązania pytań z zainteresowaniami
INSERT INTO users_survey_interests (id, survey_id, interest_id)
VALUES
    -- Pytanie 1: Projektowanie, Ekonomia i Finanse
    (1, 1, 1),
    (2, 1, 2),

    -- Pytanie 2: Eksperymenty, Pomoc
    (3, 2, 3),
    (4, 2, 4),

    -- Pytanie 3: Języki i kultura, Prawo
    (5, 3, 5),
    (6, 3, 6),

    -- Pytanie 4: Media, Automatyka
    (7, 4, 7),
    (8, 4, 9),

    -- Pytanie 5: Zarządzanie, Biologia
    (9, 5, 8),
    (10, 5, 13),

    -- Pytanie 6: Polityka, Sztuka
    (11, 6, 10),
    (12, 6, 15),

    -- Pytanie 7: Astronomia, Literatura
    (13, 7, 11),
    (14, 7, 16),

    -- Pytanie 8: Informatyka, Gry
    (15, 8, 12),
    (16, 8, 17),

    -- Pytanie 9: Sport, Projektowanie społeczne
    (17, 9, 14),
    (18, 9, 19),

    -- Pytanie 10: Inżynieria systemowa, Psychologia
    (19, 10, 18),
    (20, 10, 20),

    -- Pytanie 11: Ochrona środowiska, Fizyka
    (21, 11, 21),
    (22, 11, 22);