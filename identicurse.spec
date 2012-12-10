%define short_version 0.9

Name:           identicurse
Version:        0.9
Release:        1
Summary:        Curses based Status.net client
Group:          Networking/Other 
License:        GPLv3+
URL:            http://identicurse.net/
Source0:        http://identicurse.net/release/%{short_version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-setuptools, help2man
Requires:       python-setuptools, python-oauth

%description
A simple but powerful Identi.ca client with a curses-based UI.


%prep
%setup -q -n %{name}-%{short_version}

%build
%{__python} setup.py build
# We should use the pre-packaged version...
rm -rf build/lib/oauth/
# Statusnet is not it's own module (yet)
mv build/lib/statusnet/ build/lib/identicurse/


%install
%{__python} setup.py install --skip-build --root %buildroot
mv %{buildroot}/%{_prefix}/%{name}/* %buildroot/%{python_sitelib}/%{name}/

# Install the manpage
mkdir -p %buildroot/%{_mandir}/man1/
pushd %buildroot/%{python_sitelib}/%{name} && help2man -n %{name} --no-info --version-string=%{version} --no-discard-stderr "python __init__.py" | sed -e "s|__init__.py|identicurse|g" | sed -e "s|__INIT__.PY|IDENTICURSE|g" | sed -e "s|PYTHON||"| sed -e "s|python identicurse|identicurse|g" > %buildroot/%{_mandir}/man1/%{name}.1  && popd


%files
%doc CHANGELOG INSTALL LICENSE README conf/config.json
# For noarch packages: sitelib
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}-*.egg-info/
%{_bindir}/identicurse
%{_mandir}/man1/%{name}.1.xz


%changelog
* Mon Feb 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.9-1
+ Revision: 781003
- version update 0.9

* Wed Feb 08 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.8.2-1
+ Revision: 771855
- Group: fix
- imported package identicurse

