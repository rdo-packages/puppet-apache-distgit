%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-apache
%global commit e27004b9d7fda5506d28b6e7b8682a04168bdd21
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-apache
Version:        7.0.0
Release:        1%{?alphatag}%{?dist}
Summary:        Installs, configures, and manages Apache virtual hosts, web services, and modules.
License:        ASL 2.0

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
* Fri Mar 25 2022 RDO <dev@lists.rdoproject.org> 7.0.0-1.e27004bgit
- Update to post 7.0.0 (e27004b9d7fda5506d28b6e7b8682a04168bdd21)



