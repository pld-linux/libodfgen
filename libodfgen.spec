#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Library to generate ODF documents from librevenge API calls
Summary(pl.UTF-8):	Biblioteka do generowania dokumentów ODF z wywołań API librevenge
Name:		libodfgen
Version:	0.1.3
Release:	1
License:	MPL v2.0 or LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz
# Source0-md5:	4e6e642609ddb62b13626aa6e7efe20f
URL:		http://libwpd.sourceforge.net/
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.11
BuildRequires:	librevenge-devel >= 0.0
BuildRequires:	libstdc++-devel >= 6:4.3
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to generate ODF documents from librevenge API calls.

%description -l pl.UTF-8
Biblioteka do generowania dokumentów ODF z wywołań API librevenge.

%package devel
Summary:	Header files for libodfgen library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libodfgen
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	librevenge-devel >= 0.0
Requires:	libstdc++-devel

%description devel
Header files for libodfgen library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libodfgen.

%package static
Summary:	Static libodfgen library
Summary(pl.UTF-8):	Statyczna biblioteka libodfgen
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libodfgen library.

%description static -l pl.UTF-8
Statyczna biblioteka libodfgen.

%package apidocs
Summary:	libodfgen API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libodfgen
Group:		Documentation

%description apidocs
libodfgen API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libodfgen.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# -stdc++11 for std::shared_ptr
CXXFLAGS="%{rpmcxxflags} -std=c++11"
%configure \
	%{?with_static_libs:--enable-static} \
	--disable-silent-rules \
	--with-sharedptr=c++11
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libodfgen-*.la
# packaged as %doc in -apidocs
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libodfgen

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libodfgen-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libodfgen-0.1.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libodfgen-0.1.so
%{_includedir}/libodfgen-0.1
%{_pkgconfigdir}/libodfgen-0.1.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libodfgen-0.1.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc docs/doxygen/html/*
