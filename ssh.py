from colab_ssh import launch_ssh_cloudflared, init_git_cloudflared
get_ipython().system_raw('pip install colab_ssh --upgrade')
launch_ssh_cloudflared(password="colab12")
print("password is colab12")
