Name:           bond
Summary:        Microsoft Bond Library
Version:        8.0.1
Release:        3%{?dist}
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Mariner
URL:            https://github.com/microsoft/bond
#Source0:       %{url}/archive/%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
Source1:        gbc-0.11.0.3-%{_arch}

BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  zlib-devel
BuildRequires:  boost-devel
BuildRequires:  ncurses-devel
BuildRequires:  rapidjson-devel
BuildRequires:  gmp-devel

%description
Bond is an open-source, cross-platform framework for working with schematized data.
It supports cross-language serialization/deserialization and powerful generic mechanisms
for efficiently manipulating data. Bond is broadly used at Microsoft in high scale services.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description devel
Development files for %{name}

%prep
%setup -q

%build
CMAKE_OPTS="\
    -DBOND_ENABLE_GRPC=FALSE \
    -DBOND_FIND_RAPIDJSON=TRUE \
    -DBOND_SKIP_CORE_TESTS=TRUE \
    -DBOND_SKIP_GBC_TESTS=TRUE \
    -DBOND_GBC_PATH=%{SOURCE1} \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
"

mkdir -v build
cd build
cmake $CMAKE_OPTS ..
make %{?_smp_mflags}

%install
cd build
make DESTDIR=%{buildroot} install
chmod 0755 %{buildroot}%{_bindir}/gbc

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%files devel
%{_includedir}/%{name}/*
%{_libdir}/%{name}/*

%changelog
*   Mon Oct 19 2020 Pawel Winogrodzki <pawelwi@microsoft.com> 8.0.1-3
-   License verified.
-   Added source URL.
-   Added 'Vendor' and 'Distribution' tags.
*   Tue May 19 2020 Jonathan Chiu <jochi@microsoft.com> 8.0.1-2
-   Add aarch64 support
*   Mon Apr 06 2020 Jonathan Chiu <jochi@microsoft.com> 8.0.1-1
-   Original version for CBL-Mariner.
