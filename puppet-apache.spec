%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-apache
%global commit 58207d395c313f5cd44c3c9d5df0ef7e1fb648a3
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-apache
Version:        1.11.0
Release:        1%{?alphatag}%{?dist}
Summary:        Installs, configures, and manages Apache virtual hosts, web services, and modules.
License:        Apache-2.0

URL:            https://github.com/puppetlabs/puppetlabs-apache

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-concat
Requires:       puppet >= 2.7.0

%description
Installs, configures, and manages Apache virtual hosts, web services, and modules.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/apache/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/apache/



%files
%{_datadir}/openstack-puppet/modules/apache/


%changelog
* Thu May 15 2017 Lukas Bezdicka <lbezdick@redhat.com> 1.11.0-1.58207d3git
- Newton bump to 1.11.0 (58207d395c313f5cd44c3c9d5df0ef7e1fb648a3)

* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 1.10.0-2.05a0aac.git
- Newton update 1.10.0 (05a0aac78092e46d544e03ad9adf796ae76f7ec2)

* Fri Sep 16 2016 Haikel Guemar <hguemar@fedoraproject.org> 1.10.0-1.c04e062.git
- Newton update 1.10.0 (c04e0620defb953a27cace6409e74ad1b708a2f4)

