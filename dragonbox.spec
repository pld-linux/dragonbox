Summary:	Dragonbox float-to-string conversion algorithm implementation
Summary(pl.UTF-8):	Implementacja algorytmu Dragonbox do zamiany liczb zmiennoprzecinkowych na łańcuchy znaków
Name:		dragonbox
Version:	1.1.3
Release:	1
License:	Apache v2.0 with LLVM Exceptions or Boost v1.0
Group:		Development/Libraries
#Source0Download: https://github.com/jk-jeon/dragonbox/releases
Source0:	https://github.com/jk-jeon/dragonbox/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	889dc00db9612c6949a4ccf8115e0e6a
URL:		https://github.com/jk-jeon/dragonbox
BuildRequires:	cmake >= 3.14
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	libstdc++-devel >= 6:7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# only static library, debuginfo not supported
%define		_enable_debug_packages	0

%description
This library is a reference implementation of Dragonbox in C++.

Dragonbox is a float-to-string conversion algorithm based on a
beautiful algorithm Schubfach
<https://drive.google.com/open?id=1luHhyQF9zKlM8yJ1nebU0OgVYhfC6CBN>,
developed by Raffaello Giulietti in 2017-2018.

%description -l pl.UTF-8
Ta biblioteka to referencyjna implementacja algorytmu Dragonbox w C++.

Dragonbox to algorytm konwersji liczb zmiennoprzecinkowych na łańcuchy
znaków oparty na pięknym algorytmie Schubfach
<https://drive.google.com/open?id=1luHhyQF9zKlM8yJ1nebU0OgVYhfC6CBN>,
stworzonym przez Raffaello Giulietti w 2017-2018.

%package devel
Summary:	Dragonbox float-to-string conversion algorithm implementation
Summary(pl.UTF-8):	Implementacja algorytmu Dragonbox do zamiany liczb zmiennoprzecinkowych na łańcuchy znaków
Group:		Development/Libraries
Requires:	libstdc++-devel >= 6:7

%description devel
This library is a reference implementation of Dragonbox in C++.

Dragonbox is a float-to-string conversion algorithm based on a
beautiful algorithm Schubfach
<https://drive.google.com/open?id=1luHhyQF9zKlM8yJ1nebU0OgVYhfC6CBN>,
developed by Raffaello Giulietti in 2017-2018.

%description devel -l pl.UTF-8
Ta biblioteka to referencyjna implementacja algorytmu Dragonbox w C++.

Dragonbox to algorytm konwersji liczb zmiennoprzecinkowych na łańcuchy
znaków oparty na pięknym algorytmie Schubfach
<https://drive.google.com/open?id=1luHhyQF9zKlM8yJ1nebU0OgVYhfC6CBN>,
stworzonym przez Raffaello Giulietti w 2017-2018.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE-Apache2-LLVM LICENSE-Boost README.md
%{_libdir}/libdragonbox_to_chars.a
%{_includedir}/dragonbox-%{version}
%{_libdir}/cmake/dragonbox-%{version}
