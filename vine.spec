#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x12A53B890119D176 (omer.drow@gmail.com)
#
Name     : vine
Version  : 1.1.4
Release  : 13
URL      : http://pypi.debian.net/vine/vine-1.1.4.tar.gz
Source0  : http://pypi.debian.net/vine/vine-1.1.4.tar.gz
Source99 : http://pypi.debian.net/vine/vine-1.1.4.tar.gz.asc
Summary  : Promises, promises, promises.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: vine-python3
Requires: vine-license
Requires: vine-python
BuildRequires : buildreq-distutils3
BuildRequires : case
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
vine - Python Promises
        =====================================================================
        
        |build-status| |coverage| |license| |wheel| |pyversion| |pyimp|

%package license
Summary: license components for the vine package.
Group: Default

%description license
license components for the vine package.


%package python
Summary: python components for the vine package.
Group: Default
Requires: vine-python3

%description python
python components for the vine package.


%package python3
Summary: python3 components for the vine package.
Group: Default
Requires: python3-core

%description python3
python3 components for the vine package.


%prep
%setup -q -n vine-1.1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532204058
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/vine
cp LICENSE %{buildroot}/usr/share/doc/vine/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/vine/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
