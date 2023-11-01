%global srcname into-dbus-python

Name:           python-%{srcname}
Version:        0.06
Release:        2%{?dist}
Summary:        Transformer to dbus-python types

License:        ASL 2.0
URL:            https://github.com/stratis-storage/into-dbus-python
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
Facilities for converting an object that inhabits core Python types, e.g.,\
lists, ints, dicts, to an object that inhabits dbus-python types, e.g.,\
dbus.Array, dbus.UInt32, dbus.Dictionary based on a specified dbus signature.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-dbus-signature-pyparsing
BuildRequires:  python3-dbus
BuildRequires:  python3-hypothesis
BuildRequires:  python3-hs-dbus-signature
Requires:       python3-dbus-signature-pyparsing
Requires:       python3-dbus

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/into_dbus_python/
%{python3_sitelib}/into_dbus_python-*.egg-info/

%changelog
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Ilya Gradina <ilya.gradina@gmail.com> - 0.06-1
- Initial package
