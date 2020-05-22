root_map = {'amx': {'/GPFS/CENTRAL': '/nsls2/xf17id1'},
            'bmm': None,
            'chx': {'/XF11ID': '/nsls2/xf11id1-central',
                    '/XF11ID/data': '/nsls2/xf11id1-central/data',
                    '/nsls2/xf11id': '/nsls2/xf11id1-central',
                    '/nsls2/xf11id1': '/nsls2/xf11id1-central',
                    '/nsls2/xf11id1/data': '/nsls2/xf11id1-central/data'},
            'cms': {'/nsls2/xf11bm': '/nsls2/xf11bm',
                    '/GPFS/xf11bm': '/nsls2/xf11bm'},
            'csx': {'/GPFS/xf23id/xf23id1': '/nsls2/xf23id1/xf23id1',
                    '/GPFS/xf23id/xf23id2': '/nsls2/xf23id1/xf23id2'},
            'esm': {'/GPFS/xf23id':	'/nsls2/xf23id1',
                    '/direct/XF21ID1': '/nsls2/xf23id1'},
            'fmx': {'/GPFS/CENTRAL': '/nsls2/xf17id2'},
            'fxi': {'/NSLS2/xf18id1/DATA': '/nsls2/xf18id1/data',
                    '/NSLS2/xf18id1/DATA/Andor': '/nsls2/xf18id1/data/Andor',
                    '/NSLS2/xf18id1/DATA/detA1': '/nsls2/xf18id1/data/detA1'},
            'ios': {'/GPFS/xf23id/xf23id1': '/nsls2/xf23id1/xf23id1',
                    '/GPFS/xf23id/xf23id2': '/nsls2/xf23id1/xf23id2'},
            'isr': {'/GPFS/xf04id': '/nsls2/xf04id1'}, #/GPFS/xf04id -> /nsls2/xf04id1
            'iss': {'/GPFS/xf08id/': '/nsls2/xf08id', #/GPFS/xf08id -> /nsls2/xf08id
                    '/nsls2/xf08id': '/nsls2/xf08id',
                    '/nsls2/xf08id/data': '/nsls2/xf08id/data'},
            'ixs': None,
            'jpls': None,
            'lix': {'/GPFS/CENTRAL/XF16ID1/test/': None,
                    '/GPFS/xf16id': '/nsls2/xf16id1',                     #/GPFS/xf16id -> /nsls2/xf16id1
                    '/GPFS/xf16ide/exp_path/': '/nsls2/xf16id1/exp_path',
                    '/tmp/': None},
            'pdf': {'/SHARE/img': None,
                    '/nsls2/xf28id1': '/nsls2/xf28id1',
                    '/nsls2/xf28id1/data': '/nsls2/xf28id1/data',
                    '/nsls2/xf28id1/data/dex_data': '/nsls2/xf28id1/data/dex_data',
                    '/nsls2/xf28id1/data/pe1_data': '/nsls2/xf28id1/data/pe1_data',
                    '/tmp': None},
            'qas': {'/nsls2/xf07bm' : '/nsls2/xf07bm'},
            'rsoxs': {'/DATA/images': None,
                      '/DATA/images/data': None,
                      '/mnt/zdrive': None},
            'six': {'/XF02ID1': None,           # /XF02ID1 -> /direct/XF02ID1 which is empty.
                    '/nsls2/xf02id1': '/nsls2/xf02id1'},
            'smi': {'/GPFS/': None,
                    '/GPFS/xf12id1/data/MAXS/images': '/nsls2/xf12id2/MAXS/images',
                    '/data': '/nsls2/xf12id2/data' },
            'srx': {'/XF05IDD': '/nsls2/xf05id1-central/XF05ID1', # Guess
                    '/data': '/nsls2/xf05id1-central/data', # Guess
                    '/epicsdata': None,
                    '/nsls2/xf05id1': '/nsls2/xf05id1-central',
                    '/nsls2/xf05id1/XF05ID1': '/nsls2/xf05id1-central/XF05ID1',
                    '/nsls2/xf05id1/XF05ID1/dexela': '/nsls2/xf05id1-central/XF05ID1/dexela',
                    '/tmp': None},
            'tes': {'/nsls2/xf08bm/XF08BM': '/nsls2/xf08bm/data', # Bad guess
                    '/nsls2/xf08bm/data': '/nsls2/xf08bm/data'},
            'xfm': {'/mnt/xspress3/data-srv2': None, # Path has no data anymore.
                    '/nsls2/xf04bm/data': '/nsls2/xf04bm/data',
                    '/tmp/pe_img': None},
            'xfp': None,
            'xpd': {'/XF28IDC/XF28ID1': '/nsls2/xf28id2/',
                    '/XF28IDC/XF28ID1/pe1_data/GeRM': '/nsls2/xf28id2/pe1_data/GeRM',
                    '/direct/XF28ID1': None,
                    '/direct/XF28ID2': None,
                    '/nsls2/xf28id2': '/nsls2/xf28id2',
                    '/tmp': None},
            'xpdd': {'/data/bf_data': '/nsls2/xf28id2/bf_data',
                     '/epics': None,
                     '/mnt/ws3': None,
                     '/mnt/ws4': None,
                     '/mnt/ws4/XPDD_Data1': None,
                     '/nsls2': '/nsls2',
                     '/nsls2/xf28id2' : '/nsls2/xf28id2',
                     '/nsls2/xf28id2/bf_data': '/nsls2/xf28id2/bf_data',
                     '/nsls2/xf28id2/dex_data': '/nsls2/xf28id2/dex_data',
                     '/tmp/xpdsim_m2zab6q': None,
                     'F:\\dex_data': None,
                     'F:\\dex_data\\': None,
                     'Z:\\dex_data': None,
                     '\\nsls2\\xf28id2\\dex_data': None}}




roots = {'amx': ['', '/tmp', '/tmp/'],
 'bmm': ['/home/xspress3'],
 'chx': ['',
  '/XF11ID',
  '/XF11ID/data',
  '/nsls2/xf11id',
  '/nsls2/xf11id1',
  '/nsls2/xf11id1/data'],
 'cms': ['', '/', '/GPFS/xf11bm', '/nsls2/xf11bm'],
 'csx': ['', '/GPFS/xf23id/xf23id1', '/GPFS/xf23id/xf23id2'],
 'esm': ['', '/direct/XF21ID1'],
 'fmx': [''],
 'fxi': ['/',
  '/NSLS2/xf18id1/DATA',
  '/NSLS2/xf18id1/DATA/Andor',
  '/NSLS2/xf18id1/DATA/detA1',
  '/dev/shm'],
 'ios': ['', '/GPFS/xf23id/xf23id1', '/GPFS/xf23id/xf23id2'],
 'isr': ['/GPFS/xf04id'],
 'iss': ['', '/', '/GPFS/xf08id/', '/nsls2/xf08id', '/nsls2/xf08id/data'],
 'ixs': [],
 'jpls': ['/nsls2/jpls/data'],
 'lix': ['',
  '/',
  '/GPFS/CENTRAL/XF16ID1/test/',
  '/GPFS/xf16id',
  '/GPFS/xf16id/exp_path/',
  '/tmp/'],
 'pdf': ['/SHARE/img',
  '/nsls2/xf28id1',
  '/nsls2/xf28id1/data',
  '/nsls2/xf28id1/data/dex_data',
  '/nsls2/xf28id1/data/pe1_data',
  '/tmp'],
 'qas': ['/epics/',
  '/home/softioc/',
  '/home/softioc/tmp/',
  '/home/xf07bm/',
  '/nsls2/data/xf07bm/pb_data/',
  '/nsls2/xf07bm',
  '/nsls2/xf07bm/data',
  '/nsls2/xf07bm/data/pb_data',
  '/nsls2/xf07bm/data/pb_data/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/03/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/04/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/05/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/05/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/05/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/05/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/05/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/05/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/05/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/05/31/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/06/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/07/31/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/08/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/09/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/09/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/09/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/09/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/09/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/09/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/09/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/09/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/09/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/10/31/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/11/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2018/12/31/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/01/31/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/02/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/03/31/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/04/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/05/31/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/06/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/07/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/07/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/08/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/09/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/10/31/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/11/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2019/12/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/19/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/29/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/30/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/01/31/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/01/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/10/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/17/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/18/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/21/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/22/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/23/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/24/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/26/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/27/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/02/28/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/02/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/03/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/04/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/05/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/06/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/07/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/08/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/09/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/11/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/12/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/13/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/14/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/15/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/16/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/20/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/25/',
  '/nsls2/xf07bm/data/pizza_box_data/2020/03/27/',
  '/nsls2/xf0bm/data/pb_data',
  '/nsls2/xf0bm/data/pizza_box_data/2018/03/08/'],
 'rsoxs': ['/DATA/images', '/DATA/images/data', '/mnt/zdrive'],
 'six': ['/XF02ID1', '/nsls2/xf02id1'],
 'smi': ['/', '/GPFS', '/GPFS/xf12id1/data/MAXS/images', '/data'],
 'srx': ['',
  '/',
  '/XF05IDD',
  '/data',
  '/epicsdata',
  '/nsls2/xf05id1',
  '/nsls2/xf05id1/XF05ID1',
  '/nsls2/xf05id1/XF05ID1/dexela',
  '/tmp'],
 'tes': ['/nsls2/xf08bm/XF08BM', '/nsls2/xf08bm/data'],
 'xfm': ['/mnt/xspress3/data-srv2', '/nsls2/xf04bm/data', '/tmp/pe_img'],
 'xfp': [],
 'xpd': ['',
  '/',
  '/XF28IDC/XF28ID1',
  '/XF28IDC/XF28ID1/pe1_data/GeRM',
  '/direct/XF28ID1',
  '/direct/XF28ID2',
  '/nsls2/xf28id2',
  '/tmp'],
 'xpdd': ['/',
  '/data/bf_data',
  '/epics',
  '/mnt/ws3',
  '/mnt/ws4',
  '/mnt/ws4/XPDD_Data1',
  '/nsls2',
  '/nsls2/xf28id2',
  '/nsls2/xf28id2/bf_data',
  '/nsls2/xf28id2/dex_data',
  '/tmp/xpdsim_m2zab6q',
  'F:\\dex_data',
  'F:\\dex_data\\',
  'Z:\\dex_data',
  '\\nsls2\\xf28id2\\dex_data']}
