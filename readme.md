# Port Scanner (ScanSentinel)

* **Naam:** Joshua Klamer
* **Klas:** 24A
* **Studentennummer:** 2205022
* **Projectnaam:** ScanSentinel

---

## Inleiding

Dit project heet **ScanSentinel**. Wat is het doel van dit project? **ScanSentinel** is gemaakt voor mensen die willen bekijken welke poorts open en dicht zijn. Ik heb dit idee gekozen omdat ik graag in cybersecurity wil gaan en mezelf daar heel erg in verdiep. Ook vindt ik het een intressant concept en zie ik er veel leer potentie in. Het hoofddoel van dit project is om een goed werkende port scanner te bouwen die gebruikt kan worden voor profesioneel gebruik.

---

## Functionaliteit (Hoofdfeatures)

* CLI- en configuratie-gestuurde scans (single IP, IP-range, CIDR)
* Host discovery (ping / TCP connect)
* Multi-threaded port scanning (configurable thread pool)
* Scanprofielen (snel, grondig, op maat)
* Resultaatexport naar JSON en CSV
* Basis rapportage in de CLI (samenvatting + per-host details)
* Validatie en foutafhandeling (IP-validatie, timeouts, retry)
* Unit- en integratietests (pytest)

---

## Python Advanced — technische eisen

* **OOP**

  * Klassen: `Scanner`, `Host`, `ScanResult`, `Scheduler`, `Reporter`
* **Multithreading**

  * `concurrent.futures.ThreadPoolExecutor` voor snelle scans
* **Error handling**

  * Duidelijke excepties (bv. `ScanTimeoutError`, `InvalidIpError`)
  * Robuuste input-validatie (CIDR, IP-format)
* **Testing**

  * Unit tests met `pytest`
  * Mocking voor netwerkcalls, lokaal `localhost` testcases
* **Codekwaliteit**

  * Modulair, goed leesbaar, type hints (PEP 484)
  * Linting (flake8 / ruff) en formatting (black)

---

## Planning ( aanbevolen verdeling )

| Week   | Doel / taken                                                        | Uren p/w | Commits (doel) |
| ------ | ------------------------------------------------------------------- | -------: | :------------: |
| Week 1 | Projectopzet, requirements, voorblad, repo init, basis CLI-skeleton |      6-8 |       3-5      |
| Week 2 | IP-range parsing, CIDR ondersteuning, simpele host discovery     |     8-10 |       4-6      |
| Week 3 | Threaded port scanner (ThreadPoolExecutor), connect-methodes        |     8-10 |       4-6      |
| Week 4 | Error handling, timeouts, retries, input-validatie                  |      6-8 |       3-5      |
| Week 5 | Resultaatopslag (JSON/CSV), simpele reporter/exporter            |      6-8 |       3-5      |
| Week 6 | Tests schrijven (pytest), mocking netwerkcalls, localhost tests     |      6-8 |       3-6      |
| Week 7 | CLI polish, configuratiebestand (yaml/toml), logging toevoegen      |      4-6 |       2-4      |
| Week 8 | Documentatie, readme uitbreiden, eindrapport & demo                 |      4-6 |       2-4      |
| Week 9 | Buffer: bugfixes, presentatie voorbereiden, final testing           |      4-6 |       1-3      |

---

## Tests (voorbeelden)

**Test 1 — IP-range parsing**

* **Doel:** Controleer dat `parse_ip_range("192.168.1.0/30")` de correcte hostlijst teruggeeft
* **Waarom nuttig:** Voorkomt dat scans verkeerde adressen targeten

**Test 2 — isPortOpen**

* **Doel:** Test `is_port_open(ip, port)` voor bestaande (localhost) en gesloten poorten
* **Waarom nuttig:** Verifieert betrouwbaarheid van connect-logica en timeouts

**Aanvullende tests**

* Host discovery mock tests (simuleer unreachable hosts)
* Timeout- en exception-tests (foutafhandeling)
* Integratietest: scan localhost met bekende open poorten

---

## Architectuur / Schets

```
+----------------------+         +--------------------+
| CLI / Config         | <-----> | Scanner (Controller)|
| - IP range input     |         | - manage scans     |
+----------------------+         +---------+----------+
                                           |
          +--------------------------------+--------------------+
          |                                                     |
+---------------------+                             +----------------------+
| HostDiscovery       |                             | PortScanner          |
| - ping/check host   |                             | - threaded port scan |
+---------------------+                             +----------------------+
          |                                                     |
          +----------------------+--------------+---------------+
                                 |              |
                         +-------v-------+  +---v------------+
                         | ResultsStore  |  | Reporter       |
                         | (JSON/CSV)    |  | - export/pdf   |
                         +---------------+  +----------------+
```

---

## Projectbroncode

[Repository](https://github.com/DextenXD/ScanSentinel.git)

---

## Mogelijke uitbreidingen als ik tijd over heb

* GUI (web-interface) voor rapportage
* Nmap-compatibele output
* Service-detectie en banner-grabbing (optioneel, pas op met legaliteit)
* Scheduler voor periodieke scans

---

## Hoe gebruikt ik het?

**Commands**

- Version `python -m scansentinel version`
- Local Scan `python -m scansentinel scan --ip 127.0.0.1`
- range Scan `python -m scansentinel scan --ip 192.168.1.1-10`
- data export `python -m scansentinel scan --ip 127.0.0.1 --json resultaat.json`
- monitor mode `python -m scansentinel monitor --ip 127.0.0.1 --ports 22 80 443`


## Bronnen

https://docs.pytest.org/en/stable/
https://requests.readthedocs.io/en/latest/
https://pypi.org/project/pythonping/
https://docs.python.org/3/

https://docs.python.org/3/library/concurrent.futures.html
https://realpython.com/python3-object-oriented-programming/
https://docs.python.org/3/library/unittest.mock.html
https://docs.python.org/3/howto/argparse.html

### Contact

Voor vragen of suggesties: `github.com/DextenXD/ScanSentinel` (issues)

*Einde van document.*
