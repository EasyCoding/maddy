# This is a header-only library, but it install also cmake
# scripts to %%{_libdir}, so it cannot be noarch.
%global debug_package %{nil}

Name: maddy
Version: 1.0.3
Release: 2%{?dist}

License: MIT
Summary: C++ Markdown to HTML header-only parser library
URL: https://github.com/progsource/%{name}
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: %{name}-cmake-fixes.patch

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1
mkdir -p %{_target_platform}

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    ..
popd
%ninja_build -C %{_target_platform}

%install
%ninja_install -C %{_target_platform}

%files devel
%doc README.md
%license LICENSE AUTHORS
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}

%changelog
* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 08 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.3-1
- Initial SPEC release.
