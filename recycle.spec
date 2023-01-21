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
%cmake -DCMAKE_INSTALL_PREFIX=_build

%install
%make_install
mkdir -p %{buildroot}%{_includedir}/recycle
install _build/include/recycle/no_locking_policy.hpp %{buildroot}%{_includedir}/recycle/no_locking_policy.hpp
install _build/include/recycle/shared_pool.hpp %{buildroot}%{_includedir}/recycle/shared_pool.hpp
install _build/include/recycle/unique_pool.hpp %{buildroot}%{_includedir}/recycle/unique_pool.hpp

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
