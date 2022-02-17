import click

# # 为 test-ns 下 label为 app=testdemo 的所有pod设置访问网络延时
# # space-capsule network-delay --time 3000 --offset 1000 --interface eth0 --local-port 8080,8081 --timeout 30
# # OPTION:
# ./space-capsule delay pod eth0 3000 testdelay -lport 8080 --labels app:bop
# --destination-ip string   目标 IP. 支持通过子网掩码来指定一个网段的IP地址, 例如 192.168.1.0/24. 则 192.168.1.0~192.168.1.255 都生效。你也可以指定固定的 IP，如 192.168.1.1 或者 192.168.1.1/32，也可以通过都号分隔多个参数，例如 192.168.1.1,192.168.2.1。
# --exclude-port string     排除掉的端口，默认会忽略掉通信的对端端口，目的是保留通信可用。可以指定多个，使用逗号分隔或者连接符表示范围，例如 22,8000 或者 8000-8010。 这个参数不能与 --local-port 或者 --remote-port 参数一起使用
# --exclude-ip string       排除受影响的 IP，支持通过子网掩码来指定一个网段的IP地址, 例如 192.168.1.0/24. 则 192.168.1.0~192.168.1.255 都生效。你也可以指定固定的 IP，如 192.168.1.1 或者 192.168.1.1/32，也可以通过都号分隔多个参数，例如 192.168.1.1,192.168.2.1。
# --interface string        网卡设备，例如 eth0 (必要参数)
# --local-port string       本地端口，一般是本机暴露服务的端口。可以指定多个，使用逗号分隔或者连接符表示范围，例如 80,8000-8080
# --offset string           延迟时间上下浮动的值, 单位是毫秒
# --remote-port string      远程端口，一般是要访问的外部暴露服务的端口。可以指定多个，使用逗号分隔或者连接符表示范围，例如 80,8000-8080
# --time string             延迟时间，单位是毫秒 (必要参数)
# --force                   强制覆盖已有的 tc 规则，请务必在明确之前的规则可覆盖的情况下使用
# --ignore-peer-port        针对添加 --exclude-port 参数，报 ss 命令找不到的情况下使用，忽略排除端口
# --timeout string          设定运行时长，单位是秒，通用参数


# # space-capsule undo  {experiment-name}
# space-capsule undo network-delay
from spacecapsule.executor import bash_executor
from spacecapsule.template import chaosblade_resource, chaosblade_resource_script


@click.command()
@click.argument('scope')
@click.argument('interface')
@click.argument('time')
@click.argument('experiment-name')
@click.option('-dip', '--destination-ip', 'destination_ip')
@click.option('-rport', '--remote-port', 'remote-port')
@click.option('-lport', '--local-port', 'local_port')
@click.option('--offset', 'offset')
@click.option('--timeout', 'timeout')
@click.option('--exclude-ip', 'exclude_ip')
@click.option('--exclude-port', 'exclude_port')
@click.option('--labels', 'labels')
@click.option('--namespace', 'namespace')
def delay(scope, interface, time, experiment_name, destination_ip, remote_port, local_port, offset, timeout,
          exclude_ip, exclude_port, labels, namespace):
    args = locals()
    args['action'] = 'delay'
    args['target'] = 'network'
    args['desc'] = 'package delay'
    args['matchers'] = [
        {
            'name': 'interface',
            'value': interface
        },
        {
            'name': 'time',
            'value': time
        },
        {
            'name': 'destination-ip',
            'value': destination_ip
        },
        {
            'name': 'destination-port',
            'value': remote_port
        },
        {
            'name': 'local-port',
            'value': local_port
        },
        {
            'name': 'offset',
            'value': offset
        },
        {
            'name': 'timeout',
            'value': timeout
        },
        {
            'name': 'exclude-ip',
            'value': exclude_ip
        },
        {
            'name': 'exclude-port',
            'value': exclude_port
        },
        {
            'name': 'labels',
            'value': labels
        },
        {
            'name': 'namespace',
            'value': namespace
        }
    ]
    # defects_info(args)
    bash_executor(chaosblade_resource_script, chaosblade_resource, rollback_args, 'chaosbladeResource-rollback.sh',
                  args)


@click.command()
@click.argument('scope')
@click.argument('interface')
@click.argument('percent')
@click.argument('experiment-name')
@click.option('-dip', '--destination-ip', 'destination_ip')
@click.option('-rport', '--remote-port', 'remote-port')
@click.option('-lport', '--local-port', 'local_port')
@click.option('--offset', 'offset')
@click.option('--timeout', 'timeout')
@click.option('--exclude-ip', 'exclude_ip')
@click.option('--exclude-port', 'exclude_port')
@click.option('--labels', 'labels')
@click.option('--namespace', 'namespace')
def loss(scope, interface, percent, experiment_name, destination_ip, remote_port, local_port, offset, timeout,
         exclude_ip, exclude_port, labels, namespace):
    args = locals()
    args['desc'] = 'package loss'
    args['action'] = 'loss'
    args['target'] = 'network'
    args['matchers'] = [
        {
            'name': 'interface',
            'value': interface
        },
        {
            'name': 'percent',
            'value': percent
        },
        {
            'name': 'destination-ip',
            'value': destination_ip
        },
        {
            'name': 'destination-port',
            'value': destination_port
        },
        {
            'name': 'local-port',
            'value': local_port
        },
        {
            'name': 'offset',
            'value': offset
        },
        {
            'name': 'timeout',
            'value': timeout
        },
        {
            'name': 'exclude-ip',
            'value': exclude_ip
        },
        {
            'name': 'exclude-port',
            'value': exclude_port
        },
        {
            'name': 'labels',
            'value': labels
        },
        {
            'name': 'namespace',
            'value': namespace
        }
    ]
    # defects_info(args)
    bash_executor(chaosblade_resource_script, chaosblade_resource, rollback_args, 'chaosbladeResource-rollback.sh',
                  args)


#
def delay_pod_calico_local_port(scope, interface, time, experiment_name, destination_ip, local_port,
                                offset, timeout,
                                exclude_ip, exclude_port, labels, namespace):
    args = locals()
    args['scope'] = 'pod'
    args['matchers'] = [
        {
            'name': 'interface',
            'value': "getResource"
        },
        {
            'name': 'time',
            'value': time
        },
        {
            'name': 'destination-ip',
            'value': destination_ip
        },
        {
            'name': 'remote-port',
            'value': local_port
        },
        {
            'name': 'offset',
            'value': offset
        },
        {
            'name': 'timeout',
            'value': timeout
        },
        {
            'name': 'exclude-ip',
            'value': exclude_ip
        },
        {
            'name': 'exclude-port',
            'value': exclude_port
        },
        {
            'name': 'labels',
            'value': labels
        },
        {
            'name': 'namespace',
            'value': namespace
        }
    ]
    bash_executor(chaosblade_resource_script, chaosblade_resource, rollback_args, 'chaosbladeResource-rollback.sh',
                  args)


def to_chaos_args(args):
    chaos_args = []
    chaos_args['scope'] = args['scope']
    chaos_args['desc'] = args['desc']
    chaos_args['action'] = args['action']
    chaos_args['target'] = args['target']
    return args


def rollback_args(args):
    return {}