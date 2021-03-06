# Generated by Django 2.0.3 on 2018-03-31 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='asset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('hostname', models.CharField(max_length=64, unique=True, verbose_name='主机名')),
                ('network_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='外网IP')),
                ('inner_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='内网IP')),
                ('system', models.CharField(blank=True, max_length=128, null=True, verbose_name='系统版本')),
                ('cpu', models.CharField(blank=True, max_length=64, null=True, verbose_name='CPU')),
                ('memory', models.CharField(blank=True, max_length=64, null=True, verbose_name='内存')),
                ('disk', models.CharField(blank=True, max_length=256, null=True, verbose_name='硬盘')),
                ('bandwidth', models.IntegerField(blank=True, default='1', null=True, verbose_name='带宽')),
                ('platform', models.CharField(choices=[('阿里云', '阿里云'), ('AWS', 'AWS'), ('其他', '其他')], max_length=128, verbose_name='平台')),
                ('region', models.CharField(choices=[('香港', '香港'), ('东京', '东京')], max_length=128, verbose_name='区域')),
                ('manager', models.CharField(choices=[('何全', '何全'), ('其他', '其他')], max_length=128, verbose_name='负责人')),
                ('project', models.CharField(choices=[('项目1', '项目1'), ('项目2', '项目2'), ('项目3', '项目3'), ('其他', '其他')], max_length=128, verbose_name='项目')),
                ('Instance_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='实例ID')),
                ('buy_time', models.DateTimeField(blank=True, null=True, verbose_name='购买时间')),
                ('expire_time', models.DateTimeField(blank=True, null=True, verbose_name='到期时间')),
                ('ps', models.CharField(blank=True, max_length=1024, null=True, verbose_name='备注')),
                ('port', models.IntegerField(blank=True, default='22', null=True, verbose_name='登录端口')),
                ('is_active', models.BooleanField(default=True, verbose_name='激活')),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('utime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '资产管理',
                'db_table': 'asset',
                'permissions': {('read_asset', '只读资产管理')},
            },
        ),
        migrations.CreateModel(
            name='asset_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=64, unique=True, verbose_name='名称')),
                ('username', models.CharField(blank=True, default='root', max_length=64, null=True, verbose_name='用户名')),
                ('password', models.CharField(blank=True, max_length=256, null=True, verbose_name='密码')),
                ('private_key', models.FileField(blank=True, null=True, upload_to='upload/privatekey/%Y%m%d68057', verbose_name='私钥')),
                ('ps', models.CharField(blank=True, max_length=10240, null=True, verbose_name='备注')),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('utime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '资产用户',
                'verbose_name_plural': '资产用户',
                'db_table': 'asset_user',
                'permissions': {('read_asset_user', '只读资产用户')},
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='asset.asset_user', verbose_name='登录用户'),
        ),
    ]
