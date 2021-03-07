
-- Thrust(kN) = 3.6*Power(kW)/Speed(km/h)
-- engine_mount: Nose, Wings, Fuselage, Tail, Wings and tail
-- engine_type: Turboprop, Piston, Jet
-- wing_config: High, Low, Middle, Biplane

CREATE DATABASE super_trunfo;

CREATE TABLE flying_machines (
    name VARCHAR(50),
    thrust_kN INT,
    max_takeoff_mass_kg INT,
    speed_kmh INT,
    max_altitude_m INT,
    length_m DOUBLE,
    height_m DOUBLE,
    country VARCHAR(50),
    engine_mount VARCHAR(50),
    engine_type VARCHAR(50),
    wing_config VARCHAR(50)
);

CREATE TABLE ultra_jets (
    name VARCHAR(50),
    thrust_kN INT,
    max_takeoff_mass_kg INT,
    speed_kmh INT,
    max_altitude_m INT,
    length_m DOUBLE,
    height_m DOUBLE,
    country VARCHAR(50),
    engine_mount VARCHAR(50),
    engine_type VARCHAR(50),
    wing_config VARCHAR(50)
);

CREATE TABLE world_airplanes (
    name VARCHAR(50),
    thrust_kN INT,
    max_takeoff_mass_kg INT,
    speed_kmh INT,
    max_altitude_m INT,
    length_m DOUBLE,
    height_m DOUBLE,
    country VARCHAR(50),
    engine_mount VARCHAR(50),
    engine_type VARCHAR(50),
    wing_config VARCHAR(50)
);

CREATE TABLE fighters (
    name VARCHAR(50),
    range_km INT,
    speed_kmh INT,
    thrust_kN INT,
    max_takeoff_mass_kg INT,
    wing_span_m DOUBLE,
    length_m DOUBLE,
    country VARCHAR(50),
    engine_mount VARCHAR(50),
    engine_type VARCHAR(50),
    wing_config VARCHAR(50)
);

INSERT INTO flying_machines (
    name,
    thrust_kN,
    max_takeoff_mass_kg,
    speed_kmh,
    max_altitude_m,
    length_m,
    height_m,
    country,
    engine_mount,
    engine_type,
    wing_config
)
VALUES 
    ("Lockheed C-130 Hercules", 96, 70308, 510, 6060, 32.33, 11.75, "USA", "Wings", "Turboprop", "High"),
    ("Antonov An-32", 49, 27000, 510, 8000, 23.78, 8.75, "UKR", "Wings", "Turboprop", "High"),
    ("AI(R) ATR-72-200", 24, 21530, 530, 7600, 27.16, 7.65, "ITA-FRA", "Wings", "Turboprop", "High"),
    ("AI(R) ATR-42-500", 26, 18600, 500, 7500, 22.67, 7.59, "ITA-FRA", "Wings", "Turboprop", "High"),
    ("Socata TBM 700", 3, 2984, 555, 7800, 10.43, 3.99, "FRA", "Nose", "Turboprop", "Low"),
    ("Saab 2000", 44, 23000, 510, 9400, 24.28, 7.73, "SWE", "Wings", "Turboprop", "Low"),
    ("Beech C-90B King Air", 6, 4585, 460, 10100, 16.80, 4.33, "USA", "Wings", "Turboprop", "Low"),
    ("Antonov An-70T", 204, 170000, 730, 10900, 40.25, 16.10, "UKR", "Wings", "Turboprop", "High"),
    ("Fokker 50", 25, 21590, 530, 8900, 25.25, 8.32, "NDL", "Wings", "Turboprop", "High"),
    ("Piaggio P180 Avanti", 7, 5239, 690, 12400, 14.41, 3.99, "ITA", "Wings", "Turboprop", "Middle"),
    ("Cessna 208 Caravan", 6, 3645, 284, 9000, 11.46, 4.50, "USA", "Nose", "Turboprop", "High"),
    ("Lockhhed P-3 Orion", 67, 64410, 652, 8600, 35.61, 10.29, "USA", "Wings", "Turboprop", "Low"),
    ("Piper PA-42-720 Cheyenne", 14, 5080, 480, 9000, 8.80, 3.97, "USA", "Wings", "Turboprop", "Low"),
    ("DHC-CS2F Turbo Firecat", 19, 11793, 408, 6800, 13.26, 5.06, "CAN", "Wings", "Turboprop", "High"),
    ("Saab 340A", 19, 13155, 490, 7600, 19.73, 6.97, "SWE", "Wings", "Turboprop", "Low"),
    ("Super Guppy 377SGT-201", 132, 77000, 400, 4575, 43.84, 14.78, "USA-FRA", "Wings", "Turboprop", "Low"),
    ("Embraer EMB-120 Brasília", 18, 11580, 540, 7570, 20.00, 6.35, "BRA", "Wings", "Turboprop", "Low"),
    ("DHC-8-100 Dash 8", 22, 15740, 480, 7600, 22.25, 7.49, "CAN", "Wings", "Turboprop", "High"),
    ("Let 410 UVP E", 12, 6420, 330, 7770, 14.42, 5.83, "CZE", "Wings", "Turboprop", "High"),
    ("Dornier 328", 23, 13640, 620, 7600, 21.28, 7.23, "DEU", "Wings", "Turboprop", "High"),
    ("Short SC.7 Skyvan", 12, 6213, 320, 3050, 12.60, 4.58, "GBR", "Wings", "Turboprop", "High"),
    ("Junkers JU-52", 18, 11000, 270, 6500, 18.90, 5.55, "DEU", "Wings", "Piston", "Low"),
    ("Grob GF-200", 2, 1470, 425, 5000, 8.50, 3.20, "DEU", "Tail", "Piston", "Low"),
    ("Lockheed L-749A Constellation", 51, 48580, 525, 9000, 29.03, 7.02, "USA", "Wings", "Piston", "Low"),
    ("Beech 18 Lodestar", 7, 4490, 360, 5000, 10.70, 2.84, "USA", "Wings", "Piston", "Low"),
    ("Douglas DC-3", 19, 12200, 346, 6500, 19.66, 5.16, "USA", "Wings", "Piston", "Low"),
    ("Canadair CL-215T", 34, 21000, 375, 7500, 19.82, 8.98, "CAN", "Wings", "Piston", "High"),
    ("Noratlas", 25, 22000, 440, 7500, 21.96, 6.00, "FRA", "Wings", "Piston", "High"),
    ("Dragon Rapide", 5, 2495, 212, 5900, 10.52, 3.12, "GBR", "Wings", "Piston", "Biplane"),
    ("Pitts Special", 2, 521, 227, 6800, 4.71, 1.92, "USA", "Nose", "Piston", "Biplane"),
    ("Boeing Stearman", 3, 1275, 203, 3400, 7.63, 2.79, "USA", "Nose", "Piston", "Biplane");

INSERT INTO ultra_jets (
    name,
    thrust_kN,
    max_takeoff_mass_kg,
    speed_kmh,
    max_altitude_m,
    length_m,
    height_m,
    country,
    engine_mount,
    engine_type,
    wing_config
)
VALUES 
    ("Boeing C-17 Globemaster", 724, 265352, 740, 13640, 53.04, 16.79, "USA", "Wings", "Jet", "High"),
    ("Beriev Be-200", 148, 43000, 710, 8000, 32.05, 8.9, "FRA", "Wings", "Jet", "High"),
    ("Antonov An-225", 1374, 600000, 820, 10000, 84.0, 18.1, "UKR", "Wings", "Jet", "High"),
    ("Ilyushin IL-76MF", 628, 210000, 780, 13100, 53.19, 14.45, "RUS", "Wings", "Jet", "High"),
    ("Geophysica M-55", 98, 24500, 760, 21360, 22.87, 4.83, "FRA", "Fuselage", "Jet", "High"),
    ("Boeing F/A 18 Hornet", 196, 29932, 1800, 15500, 18.5, 4.87, "USA", "Fuselage", "Jet", "Middle"),
    ("Boeing F/A 22 Raptor", 512, 27200, 2335, 19812, 19.55, 5.1, "USA", "Fuselage", "Jet", "Middle"),
    ("Dassault Rafale", 150, 22500, 2350, 16775, 15.27, 5.34, "FRA", "Fuselage", "Jet", "Middle"),
    ("Mig 39UB", 173, 18000, 2440, 17000, 17.05, 7.7, "RUS", "Fuselage", "Jet", "Middle"),
    ("Boeing E-3A Sentry Awacs", 372, 147400, 855, 11000, 44.61, 12.73, "USA", "Wings", "Jet", "Low"),
    ("Boeing 747SP", 888, 317500, 880, 10600, 56.31, 19.94, "USA", "Wings", "Jet", "Low"),
    ("Airbus A310-300 MRTT", 476, 157000, 860, 12000, 46.66, 15.81, "EU", "Wings", "Jet", "Low"),
    ("Airbus A318-100", 212, 68000, 860, 11250, 31.44, 6.76, "EU", "Wings", "Jet", "Low"),
    ("Airbus A300-600 ST Beluga", 525, 150000, 780, 10000, 56.16, 17.25, "EU", "Wings", "Jet", "Low"),
    ("Embraer ERL-135", 66, 20000, 833, 11300, 26.33, 6.76, "BRA", "Tail", "Jet", "Low"),
    ("Raytheon Premier I", 20, 5860, 835, 12500, 14.03, 4.67, "USA", "Tail", "Jet", "Low"),
    ("Gulfstream G 1159-V Gulf V", 132, 41277, 852, 15500, 29.4, 7.7, "USA", "Tail", "Jet", "Low"),
    ("Canadair Global Express", 130, 42356, 880, 15500, 29.45, 7.62, "CAN", "Tail", "Jet", "Low"),
    ("Bombardier CRJ 700", 123, 32885, 785, 10600, 32.41, 7.32, "CAN", "Tail", "Jet", "Low"),
    ("Grob SPn G180", 25, 6300, 754, 12497, 14.81, 5.12, "DEU", "Tail", "Jet", "Low")
;

INSERT INTO world_airplanes (
    name,
    thrust_kN,
    max_takeoff_mass_kg,
    speed_kmh,
    max_altitude_m,
    length_m,
    height_m,
    country,
    engine_mount,
    engine_type,
    wing_config
)
VALUES 
    ("Antonov An-124", 918, 392000, 820, 10000, 69.20, 20.78, "UKR", "Wings", "Jet", "High"),
    ("British Aerospace 146-200", 125, 42185, 730, 9600, 28.55, 8.61, "GBR", "Wings", "Jet", "High"),
    ("Lockheed L1011-500", 666, 234620, 900, 10000, 50.04, 18.86, "USA", "Wings and Tail", "Jet", "Low"),
    ("British Aerospace BAC 1-11", 124, 45201, 780, 10300, 32.61, 7.74, "GBR", "Tail", "Jet", "Low"),
    ("Fokker 100", 124, 43320, 770, 10600, 35.53, 8.50, "NLD", "Tail", "Jet", "Low"),
    ("McDonnell Douglas DC-9-15", 109, 35245, 900, 10300, 31.85, 8.39, "USA", "Tail", "Jet", "Low"),
    ("McDonnell Douglas MD-90-30", 222, 70760, 860, 11300, 46.50, 9.40, "USA", "Tail", "Jet", "Low"),
    ("McDonnell Douglas MD-83", 193, 72580, 820, 10600, 45.00, 9.00, "USA", "Tail", "Jet", "Low"),
    ("Boeing 727-200", 216, 95028, 880, 10000, 46.70, 10.40, "USA", "Tail", "Jet", "Low"),
    ("Yakoklev Yak-42", 191, 56500, 750, 9050, 36.38, 9.83, "RUS", "Tail", "Jet", "Low"),
    ("Tupolev Tu-154M", 309, 100000, 900, 10900, 48.00, 11.40, "RUS", "Tail", "Jet", "Low"),
    ("Yakoklev Yak-40", 44, 16000, 550, 10000, 20.36, 6.50, "RUS", "Tail", "Jet", "Low"),
    ("Tupolev Tu-134B", 133, 49000, 885, 10900, 34.90, 9.02, "RUS", "Tail", "Jet", "Low"),
    ("BAe/Aerospatiale Concorde", 676, 185065, 2170, 15550, 62.17, 12.19, "GBR-FRA", "Wings", "Jet", "Low"),
    ("Ilyushin IL-96", 628, 216000, 860, 10000, 55.35, 17.60, "RUS", "Wings", "Jet", "Low"),
    ("Ilyushin IL-86", 508, 208000, 840, 11800, 59.54, 15.81, "RUS", "Wings", "Jet", "Low"),
    ("Tupolev Tu-204", 314, 103000, 880, 12100, 48.00, 13.88, "RUS", "Wings", "Jet", "Low"),
    ("Boeing 767-200ER", 508, 179140, 920, 13000, 48.50, 15.90, "USA", "Wings", "Jet", "Low"),
    ("Boeing 737-200", 142, 58100, 927, 11500, 30.48, 11.28, "USA", "Wings", "Jet", "Low"),
    ("Boeing 767-300F ER", 536, 186850, 860, 10600, 55.00, 15.90, "USA", "Wings", "Jet", "Low"),
    ("Boeing 757-200 PF", 356, 115650, 860, 11600, 47.30, 13.60, "USA", "Wings", "Jet", "Low"),
    ("Boeing 737-700", 214, 60320, 785, 12400, 33.60, 12.50, "USA", "Wings", "Jet", "Low"),
    ("Boeing 737-800", 233, 70530, 785, 12400, 39.5, 12.5, "USA", "Wings", "Jet", "Low"),
    ("Airbus A320", 244, 73500, 820, 11200, 37.57, 11.76, "EU", "Wings", "Jet", "Low"),
    ("Airbus A319", 213, 70000, 880, 12500, 33.74, 11.76, "EU", "Wings", "Jet", "Low"),
    ("Airbus A380", 1424, 575000, 903, 13000, 72.72, 24.09, "EU", "Wings", "Jet", "Low"),
    ("Airbus A330-300", 664, 217000, 860, 11800, 63.70, 16.90, "EU", "Wings", "Jet", "Low")
;

INSERT INTO fighters (
    name,
    range_km,
    speed_kmh,
    thrust_kN,
    max_takeoff_mass_kg,
    wing_span_m,
    length_m,
    country,
    engine_mount,
    engine_type,
    wing_config
)
VALUES 
    ("Panavia Tornado F-2", 3500, 2400, 142, 26490, 13.9, 18.06, "GBR-ITA-DEU", "Fuselage", "Jet", "High"),
    ("Panavia Tornado", 2700, 2400, 142, 26490, 13.9, 18.06, "GBR-ITA-DEU", "Fuselage", "Jet", "High"),
    ("British Aerospace Lighting", 2500, 2500, 120, 19000, 10.6, 16.8, "GBR", "Fuselage", "Jet", "Middle"),
    ("IAI Kfir C2", 1550, 2400, 80, 14700, 8.22, 15.65, "ISR", "Fuselage", "Jet", "Low"),
    ("Mitsubishi T-2", 2200, 1800, 67, 12800, 7.87, 17.86, "JPN", "Fuselage", "Jet", "High"),
    ("Sepecat Jaguar", 2800, 1700, 65, 14700, 8.69, 16.83, "GBR-FRA", "Fuselage", "Jet", "High"),
    ("Saab JA37 Viggen", 2000, 2300, 115, 17000, 10.6, 16.4, "SWE", "Fuselage", "Jet", "Low"),
    ("Saab S-35E Draken", 1500, 2300, 80, 12270, 9.4, 15.35, "SWE", "Fuselage", "Jet", "Middle"),
    ("Dassault Mirage 50", 1300, 2200, 70, 13700, 8.22, 15.56, "FRA", "Fuselage", "Jet", "Low"),
    ("Dassault Super Etendard", 1500, 1250, 50, 12000, 9.6, 14.31, "FRA", "Fuselage", "Jet", "Low"),
    ("Dassault Mirage 4000", 3600, 2300, 200, 20000, 12.0, 18.7, "FRA", "Fuselage", "Jet", "Low"),
    ("Dassault Mirage IV", 3500, 2300, 140, 31600, 11.85, 23.5, "FRA", "Fuselage", "Jet", "Low"),
    ("Dassault Mirage 5", 2600, 2300, 61, 13700, 8.22, 15.55, "FRA", "Fuselage", "Jet", "Low"),
    ("Dassault Mirage 2000 B", 1400, 2300, 88, 9000, 9.0, 15.33, "FRA", "Fuselage", "Jet", "Low"),
    ("Dassault Mirage III-R", 2400, 2300, 61, 13700, 8.22, 15.5, "FRA", "Fuselage", "Jet", "Low"),
    ("Dassault Mirage F-1", 3000, 2300, 71, 15200, 8.4, 15.0, "FRA", "Fuselage", "Jet", "High"),
    ("McDonnell Douglas AV-8 B", 4800, 1200, 96, 13494, 9.25, 14.12, "USA", "Fuselage", "Jet", "High"),
    ("McDonnell Douglas F-15 Eagle", 4000, 2600, 230, 30000, 13.05, 19.43, "USA", "Fuselage", "Jet", "High"),
    ("Grumman F-14 Tomcat", 3500, 2600, 186, 33724, 19.45, 18.89, "USA", "Fuselage", "Jet", "High"),
    ("McDonnell Douglas F-18 Hornet", 2500, 1900, 142, 21319, 11.43, 17.07, "USA", "Fuselage", "Jet", "High"),
    ("Northrop YF-17", 1900, 2300, 136, 17237, 10.67, 17.07, "USA", "Fuselage", "Jet", "Middle"),
    ("General Dynamics F-16", 2000, 2100, 112, 16057, 9.45, 14.52, "USA", "Fuselage", "Jet", "Middle"),
    ("Northrop RF-5E", 2200, 1700, 46, 11193, 8.13, 14.68, "USA", "Fuselage", "Jet", "Low"),
    ("Northrop F-5G", 1250, 2100, 72, 11857, 8.13, 14.78, "USA", "Fuselage", "Jet", "Low"),
    ("Northrop T-38 Talon", 1835, 1300, 35, 5362, 7.7, 14.13, "USA", "Fuselage", "Jet", "Low"),
    ("Northrop F-5E Tiger", 2863, 1700, 46, 11193, 8.13, 14.86, "USA", "Fuselage", "Jet", "Low"),
    ("McDonnell Douglas F-4F Phantom", 2600, 2300, 160, 28030, 11.77, 19.2, "USA", "Fuselage", "Jet", "Low"),
    ("McDonnell Douglas RF-4E", 2600, 2300, 160, 28030, 11.77, 19.2, "USA", "Fuselage", "Jet", "Low"),
    ("Rockwell B-1", 11600, 2400, 540, 176820, 41.67, 45.78, "USA", "Wings", "Jet", "Low")
;

-- Make one table for rule them all:

CREATE TABLE airplanes
SELECT 
    name,
    thrust_kN,
    max_takeoff_mass_kg,
    speed_kmh,
    NULL AS range_km,
    max_altitude_m,
    length_m,
    height_m,
    NULL AS wing_span_m,
    country,
    engine_mount,
    engine_type,
    wing_config
FROM flying_machines
UNION 
SELECT 
    name,
    thrust_kN,
    max_takeoff_mass_kg,
    speed_kmh,
    NULL AS range_km,
    max_altitude_m,
    length_m,
    height_m,
    NULL AS wing_span_m,
    country,
    engine_mount,
    engine_type,
    wing_config
FROM ultra_jets
UNION 
SELECT 
    name,
    thrust_kN,
    max_takeoff_mass_kg,
    speed_kmh,
    NULL AS range_km,
    max_altitude_m,
    length_m,
    height_m,
    NULL AS wing_span_m,
    country,
    engine_mount,
    engine_type,
    wing_config
FROM world_airplanes
UNION 
SELECT 
    name,
    thrust_kN,
    max_takeoff_mass_kg,
    speed_kmh,
    range_km,
    NULL AS max_altitude_m,
    length_m,
    NULL AS height_m,
    wing_span_m,
    country,
    engine_mount,
    engine_type,
    wing_config
FROM fighters;


