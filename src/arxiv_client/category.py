from __future__ import annotations

from enum import Enum
from typing import Optional


class Category(Enum):
    """
    All the categories in the arXiv subject taxonomy, mapped to their codes.
    
    See [Arxiv category taxonomy](https://arxiv.org/category_taxonomy)
    """
    def __new__(cls, value: object, description: Optional[str] = None) -> Category:
        """Allows for custom descriptions for each enum value"""
        obj = object.__new__(cls)
        obj._value_ = value
        obj.__doc__ = description
        return obj

    # Computer Science
    CS_AI = 'cs.AI', 'Computer Science - Artificial Intelligence'
    CS_AR = 'cs.AR', 'Computer Science - Hardware Architecture'
    CS_CC = 'cs.CC', 'Computer Science - Computational Complexity'
    CS_CE = 'cs.CE', 'Computer Science - Computational Engineering; Finance; and Science'
    CS_CG = 'cs.CG', 'Computer Science - Computational Geometry'
    CS_CL = 'cs.CL', 'Computer Science - Computation and Language'
    CS_CR = 'cs.CR', 'Computer Science - Cryptography and Security'
    CS_CV = 'cs.CV', 'Computer Science - Computer Vision and Pattern Recognition'
    CS_CY = 'cs.CY', 'Computer Science - Computers and Society'
    CS_DB = 'cs.DB', 'Computer Science - Databases'
    CS_DC = 'cs.DC', 'Computer Science - Distributed; Parallel; and Cluster Computing'
    CS_DL = 'cs.DL', 'Computer Science - Digital Libraries'
    CS_DM = 'cs.DM', 'Computer Science - Discrete Mathematics'
    CS_ET = 'cs.ET', 'Computer Science - Emerging Technologies'
    CS_FL = 'cs.FL', 'Computer Science - Formal Languages and Automata Theory'
    CS_GL = 'cs.GL', 'Computer Science - General Literature'
    CS_GR = 'cs.GR', 'Computer Science - Graphics'
    CS_GT = 'cs.GT', 'Computer Science - Game Theory'
    CS_HC = 'cs.HC', 'Computer Science - Human-Computer Interaction'
    CS_IR = 'cs.IR', 'Computer Science - Information Retrieval'
    CS_IT = 'cs.IT', 'Computer Science - Information Theory'
    CS_LG = 'cs.LG', 'Computer Science - Machine Learning'
    CS_LO = 'cs.LO', 'Computer Science - Logic in Computer Science'
    CS_MA = 'cs.MA', 'Computer Science - Multiagent Systems'
    CS_MM = 'cs.MM', 'Computer Science - Multimedia'
    CS_MS = 'cs.MS', 'Computer Science - Mathematical Software'
    CS_NA = 'cs.NA', 'Computer Science - Numerical Analysis'
    CS_NE = 'cs.NE', 'Computer Science - Neural and Evolutionary Computing'
    CS_NI = 'cs.NI', 'Computer Science - Networking and Internet Architecture'
    CS_OH = 'cs.OH', 'Computer Science - Other'
    CS_OS = 'cs.OS', 'Computer Science - Operating Systems'
    CS_PF = 'cs.PF', 'Computer Science - Performance'
    CS_PL = 'cs.PL', 'Computer Science - Programming Languages'
    CS_RO = 'cs.RO', 'Computer Science - Robotics'
    CS_SC = 'cs.SC', 'Computer Science - Symbolic Computation'
    CS_SD = 'cs.SD', 'Computer Science - Sound'
    CS_SE = 'cs.SE', 'Computer Science - Software Engineering'
    CS_SI = 'cs.SI', 'Computer Science - Social and Information Networks'
    CS_SY = 'cs.SY', 'Computer Science - Systems and Control'
    # Economics
    ECON_EM = 'econ.EM', 'Economics - Econometrics'
    ECON_GN = 'econ.GN', 'Economics - General Economics'
    ECON_TH = 'econ.TH', 'Economics - Theoretical Economics'
    # Electrical Engineering and Systems Science
    EESS_AS = 'eess.AS', 'Electrical Engineering and Systems Science - Audio and Speech Processing'
    EESS_IV = 'eess.IV', 'Electrical Engineering and Systems Science - Image and Video Processing'
    EESS_SP = 'eess.SP', 'Electrical Engineering and Systems Science - Signal Processing'
    EESS_SY = 'eess.SY', 'Electrical Engineering and Systems Science - Systems and Control'
    # Mathematics
    MATH_AC = 'math.AC', 'Mathematics - Commutative Algebra'
    MATH_AG = 'math.AG', 'Mathematics - Algebraic Geometry'
    MATH_AP = 'math.AP', 'Mathematics - Analysis of PDEs'
    MATH_AT = 'math.AT', 'Mathematics - Algebraic Topology'
    MATH_CA = 'math.CA', 'Mathematics - Classical Analysis and ODEs'
    MATH_CO = 'math.CO', 'Mathematics - Combinatorics'
    MATH_CT = 'math.CT', 'Mathematics - Category Theory'
    MATH_CV = 'math.CV', 'Mathematics - Complex Variables'
    MATH_DG = 'math.DG', 'Mathematics - Differential Geometry'
    MATH_DS = 'math.DS', 'Mathematics - Dynamical Systems'
    MATH_FA = 'math.FA', 'Mathematics - Functional Analysis'
    MATH_GM = 'math.GM', 'Mathematics - General Mathematics'
    MATH_GN = 'math.GN', 'Mathematics - General Topology'
    MATH_GR = 'math.GR', 'Mathematics - Group Theory'
    MATH_GT = 'math.GT', 'Mathematics - Geometric Topology'
    MATH_HO = 'math.HO', 'Mathematics - History and Overview'
    MATH_IT = 'math.IT', 'Mathematics - Information Theory'
    MATH_KT = 'math.KT', 'Mathematics - K-Theory and Homology'
    MATH_LO = 'math.LO', 'Mathematics - Logic'
    MATH_MG = 'math.MG', 'Mathematics - Metric Geometry'
    MATH_MP = 'math.MP', 'Mathematics - Mathematical Physics'
    MATH_NA = 'math.NA', 'Mathematics - Numerical Analysis'
    MATH_NT = 'math.NT', 'Mathematics - Number Theory'
    MATH_OA = 'math.OA', 'Mathematics - Operator Algebras'
    MATH_OC = 'math.OC', 'Mathematics - Optimization and Control'
    MATH_PR = 'math.PR', 'Mathematics - Probability'
    MATH_QA = 'math.QA', 'Mathematics - Quantum Algebra'
    MATH_RA = 'math.RA', 'Mathematics - Rings and Algebras'
    MATH_RT = 'math.RT', 'Mathematics - Representation Theory'
    MATH_SG = 'math.SG', 'Mathematics - Symplectic Geometry'
    MATH_SP = 'math.SP', 'Mathematics - Spectral Theory'
    MATH_ST = 'math.ST', 'Mathematics - Statistics Theory'
    # Physics
    # - Astrophysics
    ASTRO_PH_CO = 'astro-ph.CO', 'Astrophysics - Cosmology and Nongalactic Astrophysics'
    ASTRO_PH_EP = 'astro-ph.EP', 'Astrophysics - Earth and Planetary Astrophysics'
    ASTRO_PH_GA = 'astro-ph.GA', 'Astrophysics - Astrophysics of Galaxies'
    ASTRO_PH_HE = 'astro-ph.HE', 'Astrophysics - High Energy Astrophysical Phenomena'
    ASTRO_PH_IM = 'astro-ph.IM', 'Astrophysics - Instrumentation and Methods for Astrophysics'
    ASTRO_PH_SR = 'astro-ph.SR', 'Astrophysics - Solar and Stellar Astrophysics'
    # - Condensed Matter
    COND_MAT_DIS_NN = 'cond-mat.dis-nn', 'Condensed Matter - Disordered Systems and Neural Networks'
    COND_MAT_MES_HALL = 'cond-mat.mes-hall', 'Condensed Matter - Mesoscale and Nanoscale Physics'
    COND_MAT_MTRL_SCI = 'cond-mat.mtrl-sci', 'Condensed Matter - Materials Science'
    COND_MAT_OTHER = 'cond-mat.other', 'Condensed Matter - Other Condensed Matter'
    COND_MAT_SOFT = 'cond-mat.soft', 'Condensed Matter - Soft Condensed Matter'
    COND_MAT_STAT_MECH = 'cond-mat.stat-mech', 'Condensed Matter - Statistical Mechanics'
    COND_MAT_STR_EL = 'cond-mat.str-el', 'Condensed Matter - Strongly Correlated Electrons'
    COND_MAT_SUPR_CON = 'cond-mat.supr-con', 'Condensed Matter - Superconductivity'
    # - General Relativity
    GR_QC = 'gr-qc', 'General Relativity and Quantum Cosmology'
    # - High Energy Physics
    HEP_EX = 'hep-ex', 'High Energy Physics - Experiment'
    HEP_LAT = 'hep-lat', 'High Energy Physics - Lattice'
    HEP_PH = 'hep-ph', 'High Energy Physics - Phenomenology'
    HEP_TH = 'hep-th', 'High Energy Physics - Theory'
    # - Mathematical Physics
    MATH_PH = 'math-ph', 'Mathematical Physics'
    # - Nonlinear Sciences
    NLIN_AO = 'nlin.AO', 'Nonlinear Sciences - Adaptation and Self-Organizing Systems'
    NLIN_CD = 'nlin.CD', 'Nonlinear Sciences - Chaotic Dynamics'
    NLIN_CG = 'nlin.CG', 'Nonlinear Sciences - Cellular Automata and Lattice Gases'
    NLIN_PS = 'nlin.PS', 'Nonlinear Sciences - Pattern Formation and Solitons'
    NLIN_SI = 'nlin.SI', 'Nonlinear Sciences - Exactly Solvable and Integrable Systems'
    # - Nuclear Physics
    NUCL_EX = 'nucl-ex', 'Nuclear Experiment'
    NUCL_TH = 'nucl-th', 'Nuclear Theory'
    # - General Physics
    PHYSICS_ACC_PH = 'physics.acc-ph', 'Physics - Accelerator Physics'
    PHYSICS_AO_PH = 'physics.ao-ph', 'Physics - Atmospheric and Oceanic Physics'
    PHYSICS_APP_PH = 'physics.app-ph', 'Physics - Applied Physics'
    PHYSICS_ATM_CLUS = 'physics.atm-clus', 'Physics - Atomic and Molecular Clusters'
    PHYSICS_ATOM_PH = 'physics.atom-ph', 'Physics - Atomic Physics'
    PHYSICS_BIO_PH = 'physics.bio-ph', 'Physics - Biological Physics'
    PHYSICS_CHEM_PH = 'physics.chem-ph', 'Physics - Chemical Physics'
    PHYSICS_CLASS_PH = 'physics.class-ph', 'Physics - Classical Physics'
    PHYSICS_COMP_PH = 'physics.comp-ph', 'Physics - Computational Physics'
    PHYSICS_DATA_AN = 'physics.data-an', 'Physics - Data Analysis; Statistics and Probability'
    PHYSICS_ED_PH = 'physics.ed-ph', 'Physics - Physics Education'
    PHYSICS_FLU_DYN = 'physics.flu-dyn', 'Physics - Fluid Dynamics'
    PHYSICS_GEN_PH = 'physics.gen-ph', 'Physics - General Physics'
    PHYSICS_GEO_PH = 'physics.geo-ph', 'Physics - Geophysics'
    PHYSICS_HIST_PH = 'physics.hist-ph', 'Physics - History and Philosophy of Physics'
    PHYSICS_INS_DET = 'physics.ins-det', 'Physics - Instrumentation and Detectors'
    PHYSICS_MED_PH = 'physics.med-ph', 'Physics - Medical Physics'
    PHYSICS_OPTICS = 'physics.optics', 'Physics - Optics'
    PHYSICS_PLASM_PH = 'physics.plasm-ph', 'Physics - Plasma Physics'
    PHYSICS_POP_PH = 'physics.pop-ph', 'Physics - Popular Physics'
    PHYSICS_SOC_PH = 'physics.soc-ph', 'Physics - Physics and Society'
    PHYSICS_SPACE_PH = 'physics.space-ph', 'Physics - Space Physics'
    # - Quantum Physics
    QUANT_PH = 'quant-ph', 'Quantum Physics'
    # Quantitative Biology
    Q_BIO_BM = 'q-bio.BM', 'Quantitative Biology - Biomolecules'
    Q_BIO_CB = 'q-bio.CB', 'Quantitative Biology - Cell Behavior'
    Q_BIO_GN = 'q-bio.GN', 'Quantitative Biology - Genomics'
    Q_BIO_MN = 'q-bio.MN', 'Quantitative Biology - Molecular Networks'
    Q_BIO_NC = 'q-bio.NC', 'Quantitative Biology - Neurons and Cognition'
    Q_BIO_OT = 'q-bio.OT', 'Quantitative Biology - Other'
    Q_BIO_PE = 'q-bio.PE', 'Quantitative Biology - Populations and Evolution'
    Q_BIO_QM = 'q-bio.QM', 'Quantitative Biology - Quantitative Methods'
    Q_BIO_SC = 'q-bio.SC', 'Quantitative Biology - Subcellular Processes'
    Q_BIO_TO = 'q-bio.TO', 'Quantitative Biology - Tissues and Organs'
    # Quantitative Finance
    Q_FIN_CP = 'q-fin.CP', 'Quantitative Finance - Computational Finance'
    Q_FIN_EC = 'q-fin.EC', 'Quantitative Finance - Economics'
    Q_FIN_GN = 'q-fin.GN', 'Quantitative Finance - General Finance'
    Q_FIN_MF = 'q-fin.MF', 'Quantitative Finance - Mathematical Finance'
    Q_FIN_PM = 'q-fin.PM', 'Quantitative Finance - Portfolio Management'
    Q_FIN_PR = 'q-fin.PR', 'Quantitative Finance - Pricing of Securities'
    Q_FIN_RM = 'q-fin.RM', 'Quantitative Finance - Risk Management'
    Q_FIN_ST = 'q-fin.ST', 'Quantitative Finance - Statistical Finance'
    Q_FIN_TR = 'q-fin.TR', 'Quantitative Finance - Trading and Market Microstructure'
    # Statistics
    STAT_AP = 'stat.AP', 'Statistics - Applications'
    STAT_CO = 'stat.CO', 'Statistics - Computation'
    STAT_ME = 'stat.ME', 'Statistics - Methodology'
    STAT_ML = 'stat.ML', 'Statistics - Machine Learning'
    STAT_OT = 'stat.OT', 'Statistics - Other Statistics'
    STAT_TH = 'stat.TH', 'Statistics - Statistics Theory'