#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dapl
Version  : 2.1.10
Release  : 3
URL      : http://downloads.openfabrics.org/dapl/dapl-2.1.10.tar.gz
Source0  : http://downloads.openfabrics.org/dapl/dapl-2.1.10.tar.gz
Summary  : A Library for userspace access to RDMA devices using OS Agnostic DAT APIs, proxy daemon for offloading RDMA
Group    : Development/Tools
License  : BSD-3-Clause CPL-1.0 GPL-2.0
Requires: dapl-bin
Requires: dapl-lib
Requires: dapl-doc
BuildRequires : rdma-core-dev

%description
Along with the OpenFabrics kernel drivers, libdat and libdapl provides a userspace
RDMA API that supports DAT 2.0 specification and IB transport extensions for
atomic operations and rdma write with immediate data.

%package bin
Summary: bin components for the dapl package.
Group: Binaries

%description bin
bin components for the dapl package.


%package dev
Summary: dev components for the dapl package.
Group: Development
Requires: dapl-lib
Requires: dapl-bin
Provides: dapl-devel

%description dev
dev components for the dapl package.


%package doc
Summary: doc components for the dapl package.
Group: Documentation

%description doc
doc components for the dapl package.


%package lib
Summary: lib components for the dapl package.
Group: Libraries

%description lib
lib components for the dapl package.


%prep
%setup -q -n dapl-2.1.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1506709013
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1506709013
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dapltest
/usr/bin/dtest
/usr/bin/dtestcm
/usr/bin/dtestsrq
/usr/bin/dtestx

%files dev
%defattr(-,root,root,-)
/usr/include/dat2/dat.h
/usr/include/dat2/dat_error.h
/usr/include/dat2/dat_ib_extensions.h
/usr/include/dat2/dat_platform_specific.h
/usr/include/dat2/dat_redirection.h
/usr/include/dat2/dat_registry.h
/usr/include/dat2/dat_vendor_specific.h
/usr/include/dat2/udat.h
/usr/include/dat2/udat_config.h
/usr/include/dat2/udat_redirection.h
/usr/include/dat2/udat_vendor_specific.h
/usr/lib64/libdaplofa.so
/usr/lib64/libdaploscm.so
/usr/lib64/libdaploucm.so
/usr/lib64/libdat2.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdaplofa.so.2
/usr/lib64/libdaplofa.so.2.0.0
/usr/lib64/libdaploscm.so.2
/usr/lib64/libdaploscm.so.2.0.0
/usr/lib64/libdaploucm.so.2
/usr/lib64/libdaploucm.so.2.0.0
/usr/lib64/libdat2.so.2
/usr/lib64/libdat2.so.2.0.0
