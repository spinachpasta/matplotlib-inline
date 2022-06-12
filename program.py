from matplotlib.pyplot import figure
def main(wrapper):
    fig = figure()
    wrapper.add_figure(fig)
    ax = fig.gca()
    ax.plot([1,2,3,4])

    fig=figure()
    wrapper.add_figure(fig)
    ax=fig.gca()
    ax.plot([3,2,1,0])

    doesnotexist.append(aaa)

