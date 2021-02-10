import tensorflow as tf





class DQN(object):
    def __init__(self)
        self.Action=tf.placeholder(tf.float32,[None,actions])
        self.State=tf.placeholder(tf.float32,[None,states])
        

    def Net(self):

        #layer 1
        w1=tf.constant_initlizer()
        


def learn(self, s, a, r, s_):
        self.check_state_exist(s_) 
        q_predict = self.q_table.loc[s, a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.loc[s_, :].max() #gamma是价值值的增长次数
        else:
            q_target = r  # 下个 state 是终止符
        self.q_table.loc[s, a] += self.lr * (q_target - q_predict)  # 更新时，lr是对状态价值进行加权的学习效率



class DeepQNetwork:
     def __init__(
            self,
            n_actions,
            n_features,  #n state
            learning_rate=0.01,
            reward_decay=0.9,
            e_greedy=0.9,
            replace_target_iter=300,
            memory_size=500,
            batch_size=32,
            e_greedy_increment=None,
            output_graph=False,
    ):
        self.n_actions = n_actions
        self.n_features = n_features
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon_max = e_greedy     # epsilon 的最大值
        self.replace_target_iter = replace_target_iter  # 更换 target_net 的步数
        self.memory_size = memory_size  # 记忆上限
        self.batch_size = batch_size    # 每次更新时从 memory 里面取多少记忆出来
        self.epsilon_increment = e_greedy_increment # epsilon 的增量
        self.epsilon = 0 if e_greedy_increment is not None else self.epsilon_max # 是否开启探索模式, 并逐步减少探索次数

        # 记录学习次数 (用于判断是否更换 target_net 参数)
        self.learn_step_counter = 0

        # 初始化全 0 记忆 [s, a, r, s_]
        self.memory = np.zeros((self.memory_size, n_features*2+2)) # 和视频中不同, 因为 pandas 运算比较慢, 这里改为直接用 numpy

        # 创建 [target_net, evaluate_net]
        self._build_net()

        # 替换 target net 的参数
        t_params = tf.get_collection('target_net_params')  # 提取 target_net 的参数
        e_params = tf.get_collection('eval_net_params')   # 提取  eval_net 的参数
        self.replace_target_op = [tf.assign(t, e) for t, e in zip(t_params, e_params)] # 更新 target_net 参数

        self.sess = tf.Session()

        # 输出 tensorboard 文件
        if output_graph:
            # $ tensorboard --logdir=logs
            tf.summary.FileWriter("logs/", self.sess.graph)

        self.sess.run(tf.global_variables_initializer())
        self.cost_his = []  # 记录所有 cost 变化, 用于最后 plot 出来观看
    def _build_net(self):
        # -------------- 创建 eval 神经网络, 及时提升参数 --------------
        self.s = tf.placeholder(tf.float32, [None, self.n_features], name='s')  # 用来接收 observation
        self.q_target = tf.placeholder(tf.float32, [None, self.n_actions], name='Q_target') # 用来接收 q_target 的值, 这个之后会通过计算得到
        with tf.variable_scope('eval_net'):
            # c_names(collections_names) 是在更新 target_net 参数时会用到
            c_names, n_l1, w_initializer, b_initializer = \
                ['eval_net_params', tf.GraphKeys.GLOBAL_VARIABLES], 10, \
                tf.random_normal_initializer(0., 0.3), tf.constant_initializer(0.1)  # config of layers

            # eval_net 的第一层. collections 是在更新 target_net 参数时会用到
            with tf.variable_scope('l1'):
                w1 = tf.get_variable('w1', [self.n_features, n_l1], initializer=w_initializer, collections=c_names)
                b1 = tf.get_variable('b1', [1, n_l1], initializer=b_initializer, collections=c_names)
                l1 = tf.nn.relu(tf.matmul(self.s, w1) + b1)

            # eval_net 的第二层. collections 是在更新 target_net 参数时会用到
            with tf.variable_scope('l2'):
                w2 = tf.get_variable('w2', [n_l1, self.n_actions], initializer=w_initializer, collections=c_names)
                b2 = tf.get_variable('b2', [1, self.n_actions], initializer=b_initializer, collections=c_names)
                self.q_eval = tf.matmul(l1, w2) + b2

        with tf.variable_scope('loss'): # 求误差
            self.loss = tf.reduce_mean(tf.squared_difference(self.q_target, self.q_eval))
        with tf.variable_scope('train'):    # 梯度下降
            self._train_op = tf.train.RMSPropOptimizer(self.lr).minimize(self.loss)

        # ---------------- 创建 target 神经网络, 提供 target Q ---------------------
        self.s_ = tf.placeholder(tf.float32, [None, self.n_features], name='s_')    # 接收下个 observation
        with tf.variable_scope('target_net'):
            # c_names(collections_names) 是在更新 target_net 参数时会用到
            c_names = ['target_net_params', tf.GraphKeys.GLOBAL_VARIABLES]

            # target_net 的第一层. collections 是在更新 target_net 参数时会用到
            with tf.variable_scope('l1'):
                w1 = tf.get_variable('w1', [self.n_features, n_l1], initializer=w_initializer, collections=c_names)
                b1 = tf.get_variable('b1', [1, n_l1], initializer=b_initializer, collections=c_names)
                l1 = tf.nn.relu(tf.matmul(self.s_, w1) + b1)

            # target_net 的第二层. collections 是在更新 target_net 参数时会用到
            with tf.variable_scope('l2'):
                w2 = tf.get_variable('w2', [n_l1, self.n_actions], initializer=w_initializer, collections=c_names)
                b2 = tf.get_variable('b2', [1, self.n_actions], initializer=b_initializer, collections=c_names)
                self.q_next = tf.matmul(l1, w2) + b2
