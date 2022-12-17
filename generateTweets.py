!pip install -q gpt-2-simple
import gpt_2_simple as gpt2
sess = gpt2.start_tf_sess()
#upload checkpoint to /content/checkpoint/run1
gpt2.generate(sess, run_name='run1')
