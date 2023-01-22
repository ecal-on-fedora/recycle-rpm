%global debug_package %{nil}
%global forgeurl https://github.com/steinwurf/recycle
%global tag 6.0.0

%forgemeta -i

Name:    recycle
Version: 6.0.0
Release: 1%{?dist}
Summary: Recycle is an implementation of a simple C++ resource pool.
URL:     %{forgeurl}
Source:  %{forgesource}
License: BSD-3-Clause

BuildRequires: g++
BuildRequires: cmake

%description
Recycle is an implementation of a simple C++ resource pool.

%package devel
Summary: Recycle header files for development

%description devel
Recycle header files for development

%prep
%forgesetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE.rst
%doc README.rst

%files devel
%{_includedir}/recycle/no_locking_policy.hpp
%{_includedir}/recycle/shared_pool.hpp
%{_includedir}/recycle/unique_pool.hpp

%changelog
* Sat Jan 21 2023 Leonardo Rossetti <lrossett@redhat.com> - 6.0.0-1
- First version being packaged
